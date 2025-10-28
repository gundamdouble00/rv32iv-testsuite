import random

import config
from program.generator import (
    Program,
    generate_random_program,
)
from rv_instructions.integer.b_type import BTypeIns
from rv_instructions.integer.base_integer import BaseIntegerIns
from rv_instructions.integer.i_type import ITypeIns
from rv_instructions.integer.j_type import JTypeIns
from rv_instructions.integer.r_type import RTypeIns
from rv_instructions.integer.s_type import STypeIns
from rv_instructions.integer.u_type import UTypeIns
from types.integer_info import (
    r_type,
    i_type,
    j_type,
    b_type,
    s_type,
    u_type,
)

population_size: int = 0
adaptive_mutation_rates = (config.MUTATION_RATE - 0.01) / config.NUM_GENERATIONS


def save_to_file(filename: str, final_program: Program):
    with open(filename, "w") as f:
        f.write("initialization:\n")
        for i in range(0, 32):
            f.write(f"    addi x{i}, x0, {random.randint(-2048, 2047)}\n")

        f.write("main:\n")
        for ins in final_program.to_assembly():
            f.write(f"    {ins}\n")


def save_to_file_test(filename: str, programs: list[Program]):
    with open(filename, "w") as f:
        for individual in programs:
            for ins in individual.to_assembly():
                f.write(f"{ins}\n")
            f.write("\n")


def initialization(population: list[Program]):
    for _ in range(config.POPULATION_SIZE):
        new_program = generate_random_program(config.PROGRAM_LEN)
        population.append(new_program)


def calculate_fitness(individual: Program):
    if individual.fitness_score != -1:
        return

    name_set = set()
    des_set = set()
    src1_set = set()
    src2_set = set()
    src3_set = set()

    r_type_cnt: int = 0
    i_type_cnt: int = 0
    j_type_cnt: int = 0
    b_type_cnt: int = 0
    s_type_cnt: int = 0
    u_type_cnt: int = 0

    for rv_ins in individual.instructions:
        if rv_ins.name != "":
            name_set.add(rv_ins.name)
        if rv_ins.des != "":
            des_set.add(rv_ins.des)
        if rv_ins.src1 != "":
            src1_set.add(rv_ins.src1)
        if rv_ins.src2 != "":
            src2_set.add(rv_ins.src2)
        if rv_ins.src3 != "":
            src3_set.add(rv_ins.src3)

        if rv_ins.type == "r_type":
            r_type_cnt += 1
        if rv_ins.type == "i_type":
            i_type_cnt += 1
        if rv_ins.type == "j_type":
            j_type_cnt += 1
        if rv_ins.type == "b_type":
            b_type_cnt += 1
        if rv_ins.type == "s_type":
            s_type_cnt += 1
        if rv_ins.type == "u_type":
            u_type_cnt += 1

    length_of_indi = len(individual)
    individual.fitness_score = (
        len(name_set)
        + len(des_set)
        + len(src1_set)
        + len(src2_set)
        + len(src3_set)
        + (r_type_cnt / length_of_indi)
        + (i_type_cnt / length_of_indi)
        + (j_type_cnt / length_of_indi)
        + (b_type_cnt / length_of_indi)
        + (s_type_cnt / length_of_indi)
        + (u_type_cnt / length_of_indi)
    )


def tournament_selection(
    individuals: list[Program], k, num_selections
) -> list[Program]:
    for individual in individuals:
        calculate_fitness(individual)

    selected_parents = []
    for _ in range(num_selections):
        tournament = random.sample(range(len(individuals)), k)
        winner = max(tournament, key=lambda i: individuals[i].fitness_score)
        selected_parents.append(individuals[winner])

    return selected_parents


def two_point_crossover(parent1: Program, parent2: Program):
    temp1 = random.randint(1, len(parent1))
    temp2 = random.randint(1, len(parent1))
    begin_point = min(temp1, temp2)
    end_point = max(temp1, temp2)

    offspring1 = (
        parent1.instructions[:begin_point]
        + parent2.instructions[begin_point:end_point]
        + parent1.instructions[end_point:]
    )
    offspring2 = (
        parent2.instructions[:begin_point]
        + parent1.instructions[begin_point:end_point]
        + parent2.instructions[end_point:]
    )

    offspring1_obj = Program(offspring1)
    offspring2_obj = Program(offspring2)
    calculate_fitness(offspring1_obj)
    calculate_fitness(offspring2_obj)
    return [offspring1_obj, offspring2_obj]


def uniform_crossover(parent1: Program, parent2: Program):
    offspring1 = []
    offspring2 = []

    for i in range(len(parent1.instructions)):
        rand_val = random.random()
        if rand_val < 0.5:
            offspring1.append(parent1.instructions[i])
            offspring2.append(parent2.instructions[i])
        else:
            offspring1.append(parent2.instructions[i])
            offspring2.append(parent1.instructions[i])

    offspring1_obj = Program(offspring1)
    offspring2_obj = Program(offspring2)
    calculate_fitness(offspring1_obj)
    calculate_fitness(offspring2_obj)
    return [offspring1_obj, offspring2_obj]


def crossover(parents: list[Program]):
    len_of_parents: int = len(parents)
    offsprings: list[Program] = []

    for _ in range(len_of_parents):
        temp = random.random()
        if temp < config.CROSSOVER_RATE:
            temp = random.random()
            index1 = random.randint(0, len_of_parents - 1)
            index2 = random.randint(0, len_of_parents - 1)

            # print(f"index1: {index1}")
            # print(f"index2: {index2}")
            # print(f"len(parents[index1]): {len(parents[index1])}")
            # print(f"len(parents[index2]): {len(parents[index2])}")

            if temp < 0.5:
                offsprings += two_point_crossover(parents[index1], parents[index2])
            else:
                offsprings += uniform_crossover(parents[index1], parents[index2])

    return offsprings


def execute_mutation(rv_ins: BaseIntegerIns):
    if rv_ins.type == "r_type":
        return RTypeIns(random.choice(r_type))
    elif rv_ins.type == "i_type":
        return ITypeIns(random.choice(i_type))
    elif rv_ins.type == "j_type":
        return JTypeIns(random.choice(j_type))
    elif rv_ins.type == "b_type":
        return BTypeIns(random.choice(b_type))
    elif rv_ins.type == "s_type":
        return STypeIns(random.choice(s_type))
    else:
        return UTypeIns(random.choice(u_type))


def mutation(offsprings: list[Program], cur_generation: int):
    cur_mut_rate = config.MUTATION_RATE - cur_generation * adaptive_mutation_rates
    for i in range(len(offsprings)):
        for j in range(len(offsprings[i].instructions)):
            if random.random() < cur_mut_rate:
                offsprings[i].instructions[j] = execute_mutation(
                    offsprings[i].instructions[j]
                )
                calculate_fitness(offsprings[i])


def genetic_algorithm():
    population: list[Program] = []
    initialization(population)

    for generation_cnt in range(config.NUM_GENERATIONS):
        selected_parents = tournament_selection(population, 2, int(len(population) / 2))
        offsprings = crossover(selected_parents)
        mutation(offsprings, generation_cnt)

        temp = population + offsprings
        temp = sorted(temp, key=lambda x: x.fitness_score, reverse=True)
        new_generation = []
        for i in range(config.POPULATION_SIZE):
            new_generation.append(temp[i])

        population = new_generation

    for i in range(len(population)):
        if i == 12:
            break
        save_to_file(f"outputs/temp/rv_assembly{i}.s", population[i])
