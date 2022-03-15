from random import random, randint


def generate_random_dna_string():
    string_length = int(random() * 100)
    random_output_string = ''

    while string_length != int(random() * 100):
        letter_picker = random()
        if letter_picker <= .25:
            random_output_string = random_output_string + 'A'
        elif .25 < letter_picker <= .5:
            random_output_string = random_output_string + 'C'
        elif .5 < letter_picker <= .75:
            random_output_string = random_output_string + 'G'
        elif .75 < letter_picker <= 1:
            random_output_string = random_output_string + 'T'

    return random_output_string


def string_with_most_a(most_a_string_1, most_a_string_2):
    a_count_1 = 0
    a_count_2 = 0

    for i in most_a_string_1:
        if i.upper() == 'A':
            a_count_1 += 1

    for i in most_a_string_2:
        if i.upper() == 'A':
            a_count_2 += 1

    if a_count_1 > a_count_2:
        return most_a_string_1
    elif a_count_2 > a_count_1:
        return most_a_string_2
    elif a_count_1 == a_count_2:
        equal_chooser = random()
        if equal_chooser <= .5:
            return most_a_string_1
        else:
            return most_a_string_2


def dna_mutator(mutation_input_string):
    mutation_output_string = ''

    for i in mutation_input_string:
        if random() < .1:
            letter_picker = random()
            if letter_picker <= .25:
                mutation_output_string = mutation_output_string + 'A'
            elif .25 < letter_picker <= .5:
                mutation_output_string = mutation_output_string + 'C'
            elif .5 < letter_picker <= .75:
                mutation_output_string = mutation_output_string + 'G'
            elif .75 < letter_picker <= 1:
                mutation_output_string = mutation_output_string + 'T'
        else:
            mutation_output_string = mutation_output_string + i.upper()

    return mutation_output_string


def evolve(evolve_string1, evolve_string_2):
    survivor_1 = string_with_most_a(evolve_string1, evolve_string_2)
    survivor_2 = survivor_1

    mutated_survivor_1 = dna_mutator(survivor_1)
    mutated_survivor_2 = dna_mutator(survivor_2)

    return [mutated_survivor_1, mutated_survivor_2]


population = []

population.append(generate_random_dna_string())
population.append(generate_random_dna_string())

generation_count = int(input('How many generations would you like to run through? '))
while generation_count > 0:
    winners = evolve(population[randint(0, len(population) - 1)], population[randint(0, len(population) - 1)])
    population.append(winners[0])  # Adds winners to population
    population.append(winners[1])
    generation_count -= 1

print_length = len(population)
print_count = 0
while print_count < print_length:
    print(population[print_count])
    print_count += 1
