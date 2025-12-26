import random
import time

from ga.main_ga import genetic_algorithm


def main():
    seed_number = input("Input seed number: ")
    seed_offset = int(seed_number)
    random.seed(seed_offset)
    starting_time = time.time()
    genetic_algorithm()
    ending_time= time.time()

    print(ending_time - starting_time)

    print("Generate programs successful!!!")


if __name__ == "__main__":
    main()
