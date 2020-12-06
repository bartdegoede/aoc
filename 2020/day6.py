with open('day6.txt', 'r') as f:
    questions = f.read().split('\n\n')

counts = sum([len(set(question.replace('\n', ''))) for question in questions])
print(f'There are {counts} questions')

counts = sum([len(set.intersection(*map(set, question.strip().split('\n')))) for question in questions])
print(f'There are {counts} questions')
