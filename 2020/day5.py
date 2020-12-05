def seat_id(ticket):
    row = int(ticket[0:7].replace('F', '0').replace('B', '1'), 2)
    seat = int(ticket[7:].replace('L', '0').replace('R', '1'), 2)
    return row, seat

with open('day5.txt', 'r') as f:
    tickets = [ticket.strip() for ticket in f.readlines()]

rows_columns = [seat_id(ticket) for ticket in tickets]
# we're missing just one seat id in a linear set, so just subtract
seat_ids = set([row * 8 + seat for row, seat in rows_columns])
all_seat_ids = set(range(min(seat_ids), max(seat_ids)))

print(f'Max seat id: {max(seat_ids)}')
print(f'Missing seat id: {all_seat_ids - seat_ids}')
