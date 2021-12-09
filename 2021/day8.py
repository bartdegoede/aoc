if __name__ == '__main__':
    with open('day8.txt', 'r') as f:
        data = f.read().strip().split('\n')

    # data = [
    #     'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    #     'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
    #     'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
    #     'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
    #     'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
    #     'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
    #     'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
    #     'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
    #     'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
    #     'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'
    # ]

    total = 0
    for row in data:
        inp, outp = row.split(' | ')
        nums = list(map(len, outp.split()))
        total += sum([nums.count(num) for num in (2, 4, 3, 7)])

    print(f'Part 1: {total}')

    # Part 2
    total = 0
    for row in data:
        number_to_segment = {}
        patterns, outp = row.split(' | ')
        # 1, 4, 7 and 8 can be determined based on the length of the segment
        for pattern in patterns.split():
            pattern = set(pattern)
            pattern_length = len(pattern)

            if pattern_length == 2:
                number_to_segment[1] = pattern
            elif pattern_length == 4:
                number_to_segment[4] = pattern
            elif pattern_length == 3:
                number_to_segment[7] = pattern
            elif pattern_length == 7:
                number_to_segment[8] = pattern

        for pattern in patterns.split():
            # 0, 6 and 9 each consist of 6 segments
            # 2, 3 and 5 each consist of 5 segments
            # based on the already decoded values, we can determine which the others are
            # https://www.reddit.com/r/adventofcode/comments/rc0ucn/2021_day_8_part_2_my_logic_on_paper_based_on_sets/
            pattern = set(pattern)
            pattern_length = len(pattern)

            # 0, 6 and 9 each consist of 6 segments
            if pattern_length == 6:
                # 1, 4 and 7 are all subsets of 9
                if (number_to_segment[1] | number_to_segment[4] | number_to_segment[7]).issubset(pattern):
                    number_to_segment[9] = pattern
                # 1 and 7 are both subsets of 0, but 4 is not
                elif (number_to_segment[1] | number_to_segment[7]).issubset(pattern) and not number_to_segment[4].issubset(pattern):
                    number_to_segment[0] = pattern
                # otherwise it has to be 6
                else:
                    number_to_segment[6] = pattern
            # 2, 3 and 5 each consist of 5 segments
            elif pattern_length == 5:
                # the "corner" of 4 is the only pattern that matches 5
                if (number_to_segment[4] - number_to_segment[1]).issubset(pattern):
                    number_to_segment[5] = pattern
                # 1 and 7 both fit into 3, but not 2 or 5
                elif (number_to_segment[1] | number_to_segment[7]).issubset(pattern):
                    number_to_segment[3] = pattern
                # otherwise it has to be 2
                else:
                    number_to_segment[2] = pattern

        decoder = {}
        for number, segment in number_to_segment.items():
            decoder[''.join(sorted(segment))] = number

        output_number = ''
        for val in outp.split():
            output_number += str(decoder[''.join(sorted(val))])
        total += int(output_number)

    print(f'Part 2: {total}')
