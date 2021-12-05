from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    @classmethod
    def from_string(cls, string):
        x, y = map(int, string.split(','))
        return cls(x=x, y=y)


@dataclass(frozen=True)
class Line:
    start: Point
    end: Point

    @classmethod
    def from_string(cls, string):
        start, end = map(Point.from_string, string.split(' -> '))
        return cls(start=start, end=end)

    @property
    def is_vertical(self):
        return self.start.x == self.end.x

    @property
    def is_horizontal(self):
        return self.start.y == self.end.y

    @property
    def is_diagonal(self):
        return abs(self.start.x - self.end.x) == abs(self.start.y - self.end.y)

    @property
    def points(self):
        if self.is_horizontal:
            step = 1 if self.start.x < self.end.x else -1
            return [Point(x=i, y=self.start.y) for i in range(self.start.x, self.end.x + step, step)]
        if self.is_vertical:
            step = 1 if self.start.y < self.end.y else -1
            return [Point(x=self.start.x, y=i) for i in range(self.start.y, self.end.y + step, step)]
        if self.is_diagonal:
            step_x = 1 if self.start.x < self.end.x else -1
            step_y = 1 if self.start.y < self.end.y else -1
            # whoa this came from copilot
            return [Point(x=i, y=j) for i, j in zip(range(self.start.x, self.end.x + step_x, step_x), range(self.start.y, self.end.y + step_y, step_y))]


def filter_lines(lines, filters):
    return list(filter(filters, lines))


def count_points(lines):
    points = Counter([point for line in lines for point in line.points])
    return len([point for point in points if points[point] > 1])


if __name__ == '__main__':
    with open('day5.txt', 'r') as f:
        data = f.read().strip().split('\n')

    lines = [Line.from_string(line) for line in data]

    filtered_lines = filter_lines(lines, lambda line: line.is_horizontal or line.is_vertical)
    print(f'Part 1: {count_points(filtered_lines)}')

    filtered_lines = filter_lines(lines, lambda line: line.is_horizontal or line.is_vertical or line.is_diagonal)
    print(f'Part 2: {count_points(filtered_lines)}')
