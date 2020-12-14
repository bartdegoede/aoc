class Ship:
    def __init__(self):
        self.current_direction = 'E'
        self.position = (0, 0)
        self.waypoint_position = (10, 1)

        self.wind_directions = ['N', 'E', 'S', 'W']

        self.instructions = {
            'E': self.east,
            'F': self.forward,
            'L': self.left,
            'N': self.north,
            'R': self.right,
            'S': self.south,
            'W': self.west
        }

    @property
    def distance_from_origin(self):
        return abs(self.position[0]) + abs(self.position[1])

    def move(self, instruction, waypoint=False):
        command = instruction[0]
        value = int(instruction[1:])
        self.instructions[command](value, waypoint=waypoint)

    def north(self, v, waypoint=False):
        if waypoint:
            self.waypoint_position = (self.waypoint_position[1], self.waypoint_position[1] + v)
        else:
            self.position = (self.position[0], self.position[1] + v)

    def south(self, v, waypoint=False):
        if waypoint:
            self.waypoint_position = (self.waypoint_position[1], self.waypoint_position[1] - v)
        else:
            self.position = (self.position[0], self.position[1] - v)

    def west(self, v, waypoint=False):
        if waypoint:
            self.waypoint_position = (self.waypoint_position[0] - v, self.waypoint_position[1])
        else:
            self.position = (self.position[0] - v, self.position[1])

    def east(self, v, waypoint=False):
        if waypoint:
            self.waypoint_position = (self.waypoint_position[0] + v, self.waypoint_position[1])
        else:
            self.position = (self.position[0] + v, self.position[1])

    def forward(self, v, waypoint=False):
        if waypoint:
            x = self.position[0] + self.waypoint_position[0] * v
            y = self.position[1] + self.waypoint_position[1] * v
            self.position = (x, y)
        else:
            self.instructions[self.current_direction](v)

    def right(self, v, waypoint=False):
        v = v // 90
        if waypoint:
            for _ in range(v):
                x = self.waypoint_position[1]
                y = -self.waypoint_position[0]
                self.waypoint_position = (x, y)
        else:
            self.current_direction = self.wind_directions[(self.wind_directions.index(self.current_direction) + v) % len(self.wind_directions)]

    def left(self, v, waypoint=False):
        v = v // 90
        if waypoint:
            for _ in range(v):
                x = -self.waypoint_position[1]
                y = self.waypoint_position[0]
                self.waypoint_position = (x, y)
        else:
            self.current_direction = self.wind_directions[(self.wind_directions.index(self.current_direction) - v) % len(self.wind_directions)]

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[0] - b[0])

with open('day12.txt', 'r') as f:
    instructions = [line.strip() for line in f.readlines()]

# instructions = ['F10', 'N3', 'F7', 'R90', 'F11']
ship = Ship()
for instruction in instructions:
    ship.move(instruction)

ship2 = Ship()
for instruction in instructions:
    ship2.move(instruction, waypoint=True)
print(ship.distance_from_origin)
print(ship2.distance_from_origin)
