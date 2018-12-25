def step(scores, elf1, elf2):
    s = scores[elf1] + scores[elf2]
    if s >= 10: # max score will be 9 + 9 = 18
        scores.append(1)
    scores.append(s % 10)
    # move elves
    elf1 = (elf1 + scores[elf1] + 1) % len(scores)
    elf2 = (elf2 + scores[elf2] + 1) % len(scores)
    return elf1, elf2

if __name__ == "__main__":
    recipes = 147061
    scores = [3, 7]
    elf1, elf2 = 0, 1

    while len(scores) < recipes + 10:
        elf1, elf2 = step(scores, elf1, elf2)

    print(f'Score of the 10 recipes after {recipes} is {"".join(map(str, scores[recipes:recipes+10]))}')

    digits = list(map(int, str(recipes)))
    # reset scores and elves
    scores = [3, 7]
    elf1, elf2 = 0, 1
    while True:
        elf1, elf2 = step(scores, elf1, elf2)
        if scores[-len(digits)-1:-1] == digits:
            appeared_recipes = len(scores) - len(digits) - 1
            break
        if scores[-len(digits):] == digits:
            appeared_recipes = len(scores) - len(digits)
            break
    print(f'There appear {appeared_recipes} recipes on the board')
