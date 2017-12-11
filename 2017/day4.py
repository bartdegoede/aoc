

if __name__ == '__main__':
    valid_phrases = 0
    with open('day4.txt', 'r') as f:
        for line in f.readlines():
            words = [''.join(sorted(w)) for w in line.split()]
            if len(words) == len(set(words)):
                valid_phrases += 1
    print valid_phrases
