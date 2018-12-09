from collections import defaultdict

class Marble(object):
    def __init__(self, number):
        self.number = number
        self.next = None
        self.previous = None

def solve(players=438, marble_count=71626):
    scores = defaultdict(int)

    current_player = 0
    current_marble = Marble(0)
    current_marble.next = current_marble.previous = current_marble

    last_placed_marble = 0

    while last_placed_marble < marble_count:
        current_player = (current_player + 1) % players
        last_placed_marble += 1

        if last_placed_marble % 23 == 0:
            # magic for scores
            scores[current_player] += last_placed_marble
            seven_counter_clock_wise = current_marble.previous.previous.previous.previous.previous.previous.previous
            scores[current_player] += seven_counter_clock_wise.number
            current_marble = seven_counter_clock_wise.next
            seven_counter_clock_wise.previous.next = seven_counter_clock_wise.next
            seven_counter_clock_wise.next.previous = seven_counter_clock_wise.previous
        else:
            one_clock_wise = current_marble.next
            two_clock_wise = current_marble.next.next
            new_marble = Marble(last_placed_marble)

            one_clock_wise.next = new_marble
            new_marble.previous = one_clock_wise
            new_marble.next = two_clock_wise
            two_clock_wise.previous = new_marble
            current_marble = new_marble

    winning_elf = max(scores, key=lambda x: scores[x])
    print(f'Score of winning elf: {scores[winning_elf]}')

if __name__ == '__main__':
    # 438 players; last marble is worth 71626 points
    import time
    start = time.time()
    solve(marble_count=71626)
    end1 = time.time()
    print(f'Solving part 1 took {end1 - start} seconds')
    solve(marble_count=71626 * 100)
    print(f'Solving part 2 took {time.time() - end1} seconds')
