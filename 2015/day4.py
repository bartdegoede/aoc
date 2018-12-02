from hashlib import md5

if __name__ == '__main__':
    seed = 'yzbqklnj'
    output = '1'
    i = 0
    while not output.startswith('000000'):
        i += 1
        output = md5(f'{seed}{i}'.encode('utf8')).hexdigest()
        if i % 1000 == 0:
            print(f'Processed {i} hashes (current hash {output})')

    print(f'First hash found for {i}')
