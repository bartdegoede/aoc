class Position(object):
    def __init__(self, x, y, z, name):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

    def __repr__(self):
        return '{} <x: {}, y: {}, z: {}>'.format(self.name, self.x, self.y, self.z)


class Particle(object):
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def step(self):
        for direction in ['x', 'y', 'z']:
            acceleration = getattr(self.a, direction)
            setattr(self.v, direction, getattr(self.v, direction) + acceleration)
            velocity = getattr(self.v, direction)
            setattr(self.p, direction, getattr(self.p, direction) + velocity)

    def distance(self):
        return sum([abs(getattr(self.p, i)) for i in ['x', 'y', 'z']])

    def __repr__(self):
        return 'Particle <{}, {}, {}>'.format(self.p, self.v, self.a)


if __name__ == '__main__':
    particles = {}
    with open('day20.txt', 'r') as f:
        for i, line in enumerate(f):
            points = line.strip().split(', ')
            position = Position(*[int(p) for p in points[0].strip('p=<').strip('>').split(',')], name='position')
            velocity = Position(*[int(p) for p in points[1].strip('v=<').strip('>').split(',')], name='velocity')
            acceleration = Position(*[int(p) for p in points[2].strip('a=<').strip('>').split(',')], name='acceleration')

            particle = Particle(position, velocity, acceleration)
            particles[i] = particle

    while True:
        min_distance = None
        closest_particle = None

        for i, particle in particles.iteritems():
            particle.step()
            if min_distance is None or particle.distance() < min_distance:
                closest_particle = i
                min_distance = particle.distance()

        print closest_particle, '-- break when this does not change anymore'
