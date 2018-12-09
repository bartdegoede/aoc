from collections import defaultdict
import heapq
import string

LETTERS = string.ascii_uppercase

class Elf(object):
    def __init__(self):
        self.task = None
        self.done = False
        self.working_time = 0

    def give_task(self, task):
        self.task = task
        self.done = False
        self.working_time = LETTERS.index(task) + 1 + 60

    @property
    def working(self):
        return self.working_time > 0

    def next(self):
        if self.working:
            self.working_time -= 1
            if self.working_time == 0:
                self.done = True


if __name__ == '__main__':
    with open('day7.txt', 'r') as f:
        instructions = f.read().strip().split('\n')

    successors = defaultdict(list)
    ancestors = defaultdict(list)
    for step in instructions:
        step = step.split()
        src, dst = step[1], step[7]

        successors[src].append(dst)
        ancestors[dst].append(src)

    queue = []
    sequence = []
    for step in set(successors.keys()) - set(ancestors.keys()):
        # heapq is a priority queue, meaning it'll keep the queue ordered from
        # smallest to biggest value
        heapq.heappush(queue, step)

    while queue:
        step = heapq.heappop(queue)
        sequence.append(step)
        for next_step in successors[step]:
            ancestors_ = ancestors[next_step]
            # if the next step is not yet in the sequence
            # AND all of the ancestors are already in the sequence
            # we should add this item to the queue (basically, it'll be added
            # once all the preceding characters have been added)
            if next_step not in sequence and all([a in sequence for a in ancestors_]):
                heapq.heappush(queue, next_step)

    print(f'The sequence of steps is {"".join(sequence)}')

    elves = [Elf() for _ in range(5)]
    queue = []
    sequence = []
    seconds = 0

    for step in set(successors.keys()) - set(ancestors.keys()):
        # heapq is a priority queue, meaning it'll keep the queue ordered from
        # smallest to biggest value
        heapq.heappush(queue, step)

    while len(sequence) < 26:
        available_elves = [elf for elf in elves if not elf.working]

        for elf in available_elves:
            if queue:
                task = heapq.heappop(queue)
                elf.give_task(task)

        for elf in elves:
            elf.next()
            if elf.done:
                sequence.append(elf.task)

                for next_step in successors[elf.task]:
                    ancestors_ = ancestors[next_step]
                    if next_step not in sequence and all([a in sequence for a in ancestors_]):
                        heapq.heappush(queue, next_step)
                elf.done = False

        seconds += 1

    print(f'Work took {seconds} seconds')
