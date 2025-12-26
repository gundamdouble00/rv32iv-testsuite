import multiprocessing
import random

import config
from config import (
    HAZARD_SCORE,
    INSTRUCTION_SCORES,
    NEGATIVE_IMM_BONUS,
    PENALTY_PER_MISSING,
    POPULATION_SIZE,
    PROGRAM_LEN,
    SAME_OPERAND_SCORE,
)
from program.generator import (
    Program,
    generate_random_program,
)
from rv_instructions.v_extension.base_vector import ConfigurationSetting
from rv_types.instruction_type import type_of_ins
from rv_types.riscv_infor import class_of_instructions

population_size: int = 0
adaptive_mutation_rates = (config.MUTATION_RATE - 0.01) / config.NUM_GENERATIONS


def save_to_file(population: list[Program]):
    for i in range(min(12, len(population))):
        individual = population[i]

        with open(f"outputs/temp/rv_assembly{i}.s", "w") as f:
            for ins in individual.header:
                if ins[0] != "." and ins[len(ins) - 1] != ":":
                    f.write(f"    {ins}\n")
                else:
                    f.write(f"{ins}\n")
            f.write("\n")

            for ins in individual.to_assembly():
                f.write(f"    {ins}\n")

            f.write("\n")
            for ins in individual.footer:
                if ins[0] != "." and ins[len(ins) - 1] != ":":
                    f.write(f"    {ins}\n")
                else:
                    f.write(f"{ins}\n")


def initialization(population: list[Program]):
    inputs = [config.PROGRAM_LEN] * config.POPULATION_SIZE
    initial_population: list[Program] = []

    with multiprocessing.Pool() as pool:
        initial_population = pool.map(generate_random_program, inputs)

    return initial_population

    for _ in range(config.POPULATION_SIZE):
        new_program = generate_random_program(config.PROGRAM_LEN)
        population.append(new_program)


def calculate_fitness(individual: Program):
    if individual.fitness != -1.00:
        return

    individual.update_numbers_ins()

    fitness_score: float = 0.0
    for key, want in config.RV32.items():
        # Subtract if program doesn't have enough instructions in config.py
        actual = individual.count_ins[key]
        if want > actual:
            fitness_score -= PENALTY_PER_MISSING

        # Add score for instructions which in the program
        fitness_score += actual * INSTRUCTION_SCORES[key]

    for i in range(4, len(individual.body)):
        index_j = i - 1
        cur_ins = individual.body[i]
        while index_j >= 0:
            previous_ins = individual.body[index_j]
            operand = set()
            if previous_ins.des != "":
                operand.add(previous_ins.des)
            if previous_ins.src2 != "":
                operand.add(previous_ins.src2)
            if previous_ins.src1 != "":
                operand.add(previous_ins.src1)

            # Add score for hazard
            if (
                (cur_ins.des in operand)
                or (cur_ins.src2 in operand)
                or (cur_ins.src1 in operand)
            ):
                fitness_score += index_j * HAZARD_SCORE

            index_j -= 1

        # Add score if destination register is the same source registers
        if cur_ins.des in {cur_ins.src2, cur_ins.src1} and cur_ins.des != "":
            fitness_score += SAME_OPERAND_SCORE

        # Add score if program has immediate instructions
        if cur_ins.type == "i_i_type":
            if int(cur_ins.src3) < 0:
                fitness_score += NEGATIVE_IMM_BONUS

    individual.fitness = fitness_score


def tournament_selection(
    individuals: list[Program], k, num_selections
) -> list[Program]:
    selected_parents = []
    for _ in range(num_selections):
        tournament = random.sample(range(len(individuals)), k)
        winner = max(tournament, key=lambda i: individuals[i].fitness)
        selected_parents.append(individuals[winner])

    return selected_parents


def get_cfg_ins(individual: Program) -> list[int]:
    result = []
    temp_list = []
    for i in range(0, len(individual.body)):
        cur_ins = individual.body[i]
        if cur_ins.type != type_of_ins[ConfigurationSetting.__name__]:
            temp_list.append(cur_ins)
            continue

        if len(temp_list) != 0:
            if temp_list[0].type != type_of_ins[ConfigurationSetting.__name__]:
                cfg_obj = ConfigurationSetting("vsetvli", 0, 8.0, 32)
                cfg_obj.lmul = 8.0
                cfg_obj.lmul = 32

                temp1_list = [cfg_obj] + temp_list
                temp_list = temp1_list
            result.append(temp_list)
        temp_list = [cur_ins]

    result.append(temp_list)
    return result


def execute_crossover(parent1: Program, parent2: Program):
    offspring1 = Program()
    offspring2 = Program()

    cfg_ins = []
    if config.RV32[type_of_ins[ConfigurationSetting.__name__]] > 0:
        cfg_ins.extend(get_cfg_ins(parent1))
        cfg_ins.extend(get_cfg_ins(parent2))
    else:
        for i in range(PROGRAM_LEN):
            if random.random() < 0.5:
                offspring1.body.append(parent1.body[i])
                offspring2.body.append(parent2.body[i])
            else:
                offspring1.body.append(parent2.body[i])
                offspring2.body.append(parent1.body[i])

        calculate_fitness(offspring1)
        calculate_fitness(offspring2)

        offspring1.header = parent1.header
        offspring1.footer = parent1.footer

        offspring2.header = parent2.header
        offspring2.footer = parent2.footer

        return [offspring1, offspring2]

    random.shuffle(cfg_ins)
    for ins in cfg_ins:
        offspring1.body.extend(ins)
        if len(offspring2.body) >= PROGRAM_LEN:
            break

    random.shuffle(cfg_ins)
    for ins in cfg_ins:
        offspring2.body.extend(ins)
        if len(offspring2.body) >= PROGRAM_LEN:
            break

    offspring1.body = offspring1.body[:PROGRAM_LEN]
    offspring2.body = offspring2.body[:PROGRAM_LEN]
    calculate_fitness(offspring1)
    calculate_fitness(offspring2)

    offspring1.header = parent1.header
    offspring1.footer = parent1.footer

    offspring2.header = parent2.header
    offspring2.footer = parent2.footer

    return [offspring1, offspring2]


def crossover(parents: list[Program]):
    len_of_parents: int = len(parents)
    offsprings: list[Program] = []

    for _ in range(len_of_parents):
        temp = random.random()
        if temp < config.CROSSOVER_RATE:
            index1 = random.randint(0, len_of_parents - 1)
            index2 = random.randint(0, len_of_parents - 1)
            offsprings.extend(execute_crossover(parents[index1], parents[index2]))

    return offsprings


def execute_mutation(rv_ins):
    if rv_ins.type == type_of_ins[ConfigurationSetting.__name__]:
        return rv_ins

    riscv_class = class_of_instructions[rv_ins.name]
    if rv_ins.type[0] == "i":
        return riscv_class(rv_ins.name, rv_ins.index)

    try:
        riscv_obj = riscv_class(rv_ins.name, rv_ins.index, rv_ins.lmul, rv_ins.sew)
    except ValueError:
        return rv_ins
    else:
        return riscv_obj


def mutation(offsprings: list[Program], cur_generation: int):
    cur_mut_rate = config.MUTATION_RATE - cur_generation * adaptive_mutation_rates
    for i in range(len(offsprings)):
        for j in range(len(offsprings[i].body)):
            if random.random() < cur_mut_rate:
                offsprings[i].body[j] = execute_mutation(offsprings[i].body[j])
                calculate_fitness(offsprings[i])


def genetic_algorithm():
    population: list[Program] = []
    population = initialization(population)
    # initialization(population)
    save_to_file(population)

    return

    for individual in population:
        calculate_fitness(individual)

    # temp_population: list[Program] = []
    for generation_cnt in range(config.NUM_GENERATIONS):
        # Sort the population in decreasing order of fitness_score
        population = sorted(population, key=lambda x: x.fitness, reverse=True)

        # Generate new offsprings for new generation
        new_generation = []

        # Perform Elitism, that mean 10% of fittest population
        # goes to the next generation
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        # Individuals will mate to produce offspring
        selected_parents = tournament_selection(population, 2, int(POPULATION_SIZE / 2))
        offsprings = crossover(selected_parents)

        # Execute mutation
        mutation(offsprings, generation_cnt)

        offsprings.extend(selected_parents)
        new_generation.extend(offsprings)
        new_generation = new_generation[:POPULATION_SIZE]

        population = new_generation

    save_to_file(population)
