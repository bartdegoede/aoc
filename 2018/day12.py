def age(rules, state, generations):
    for generation in range(generations):
        min_plant = min(state)
        max_plant = max(state)
        max_length = max_plant - min_plant + 7

        pots = ''
        for i in range(min_plant - 4, max_plant + 5):
            if i in state:
                pots += '#'
            else:
                pots += '.'
        state = []
        for i in range(2, max_length):
            if rules[pots[i-2:i+3]]:
                state.append(i - 4 + min_plant)

    return sum(state)

if __name__ == "__main__":
    with open('day12.txt', 'r') as f:
        data = f.read().splitlines()
    initial_state, notes = data[0], data[2:]
    initial_state = [i for i, plant in enumerate(initial_state[15:]) if plant == '#']
    rules = {}
    for note in notes:
        rule, plant = note.split(' => ')
        rules[rule] = plant == '#'

    plants = age(rules, initial_state, generations=20)
    print(f'There are {plants} plants after 20 generations')

    # after 96 generations, we add 32 plants every generation; this is a
    # very manual and visual inspection
    # for i in range(0, 1000):
    #     plants = age(rules, initial_state, generations=i)
    #     next_gen = age(rules, initial_state, generations=i+1)
    #     print(i, plants, next_gen-plants)
    gen_100 = age(rules, initial_state, generations=100)
    plants = gen_100 + ((50000000000 - 100) * 32)
    print(f'There are {plants} plants after 50000000000 generations')
