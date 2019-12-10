if __name__ == '__main__':
    with open('day8.txt', 'r') as f:
        data = f.read().strip()

    width = 25
    height = 6

    layer_size = 25*6

    zeroes_layer = None
    cnt = 26
    layers = []
    for i in range(0, len(data), layer_size):
        layer = data[i:i+layer_size]
        layers.append(layer)
        if layer.count('0') < cnt:
            cnt = layer.count('0')
            zeroes_layer = layer

    print(f'Part 1: {zeroes_layer.count("1") * zeroes_layer.count("2")}')

    img = layers[0]
    for layer in layers[1:]:
        img = [layer[p] if img[p] == '2' else img[p] for p in range(width * height)]

    for i in range(height):
         print(''.join(img[i*width:(i+1) * width]).replace('0', ' ').replace('1', 'x'))
