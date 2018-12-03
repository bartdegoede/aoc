from collections import defaultdict

def parse_claim(claim):
    claim = claim.split()
    claim_id = claim[0]
    x, y = map(int, claim[2].split(':')[0].split(','))
    w, h = map(int, claim[3].split('x'))
    return claim_id, x, y, w, h

if __name__ == '__main__':
    with open('day3.txt', 'r') as f:
        claims = f.read().strip().split('\n')

    # for every occupied coordinate, keep track of a list
    # with claims that contain that coordinate
    claim_map = defaultdict(list)
    # part2: we need to keep track of which claims have overlap
    overlapping = {}
    for claim in claims:
        claim_id, x, y, w, h = parse_claim(claim)
        overlapping[claim_id] = set()
        for i in range(x, x + w):
            for j in range(y, y + h):
                # if we have seen this coordinate claimed before
                if claim_map[(i, j)]:
                    for overlapping_claim in claim_map[(i, j)]:
                        # add the other claims to overlap with this one
                        overlapping[overlapping_claim].add(claim_id)
                        # add the overlapping claims to the claim_id
                        overlapping[claim_id].add(overlapping_claim)

                claim_map[(i, j)].append(claim_id)

    two_or_more_claims = 0
    for coordinate, claims in claim_map.items():
        if len(claims) > 1:
            two_or_more_claims += 1
    print(f'There are {two_or_more_claims} square inches claimed more than once')
    for claim, overlapping_claims in overlapping.items():
        if len(overlapping_claims) == 0:
            print(f'Claim {claim} does not overlap with any other')
            break
