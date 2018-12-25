UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)

DIRECTIONS = {
    '^': UP,
    'v': DOWN,
    '<': LEFT,
    '>': RIGHT
}

class Cart(object):
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.turn_idx = 0
        self.crashed = False

        self.straight = {UP: UP, DOWN: DOWN, LEFT: LEFT, RIGHT: RIGHT}
        self.left = {UP: LEFT, DOWN: RIGHT, LEFT: DOWN, RIGHT: UP}
        self.right = {UP: RIGHT, DOWN: LEFT, LEFT: UP, RIGHT: DOWN}
        self.forward_slash = {UP: RIGHT, DOWN: LEFT, LEFT: DOWN, RIGHT: UP}
        self.back_slash = {UP: LEFT, DOWN: RIGHT, LEFT: UP, RIGHT: DOWN}

    def step(self, grid):
        self.position = (self.position[0] + self.direction[0],
                         self.position[1] + self.direction[1])
        # find the char at the new position
        char = grid[self.position]
        if char == '+':
            turn = [self.left, self.straight, self.right][self.turn_idx % 3]
            self.direction = turn[self.direction]
            self.turn_idx += 1
        elif char == '/':
            self.direction = self.forward_slash[self.direction]
        elif char == '\\': # escape backslash
            self.direction = self.back_slash[self.direction]

    def collides_with(self, other_cart):
        return (self != other_cart and
                not self.crashed and
                not other_cart.crashed and
                self.position == other_cart.position)

    def __repr__(self):
        return f'Cart <{self.position[0]}, {self.position[1]}>'

if __name__ == "__main__":
    with open('day13.txt', 'r') as f:
        data = f.read().split('\n')

    grid = {}
    carts = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            grid[(x, y)] = char
            if char in DIRECTIONS:
                # create a cart
                carts.append(Cart(position=(x, y), direction=DIRECTIONS[char]))

    i = 0
    while True:
        # carts are moved from top to bottom, left to right
        carts = sorted(carts, key=lambda c: (c.position[1], c.position[0]))
        for cart in carts:
            cart.step(grid)
            for other_cart in carts:
                if cart.collides_with(other_cart):
                    cart.crashed = other_cart.crashed = True
                    part1 = part1 or cart.position

        # remove crashed carts
        carts = [cart for cart in carts if not cart.crashed]
        if len(carts) == 1:
            part2 = carts[0].position

    print(f'Position of first cart crash is {part1}')
    print(f'Position of the last cart is {part2}')v
