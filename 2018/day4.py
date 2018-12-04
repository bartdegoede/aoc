from collections import defaultdict
from datetime import datetime

if __name__ == '__main__':
    with open('day4.txt', 'r') as f:
        records = sorted(f.read().splitlines())

    guards = defaultdict(dict)
    times = defaultdict(int)

    for record in records:
        d, event = record.split('] ')
        d = datetime.strptime(d[1:], '%Y-%m-%d %H:%M')
        if 'Guard #' in event:
            guard_id = event.split()[1][1:]
        if 'falls asleep' in event:
            start = d.minute
        if 'wakes up' in event:
            end = d.minute
            times[guard_id] += (end - start)
            for i in range(start, end):
                if i not in guards[guard_id]:
                    guards[guard_id][i] = 0
                guards[guard_id][i] += 1

guard, time = max(times.items(), key=lambda x: x[1])
minute, count = max(guards[guard].items(), key=lambda x: x[1])
print(f'Guard * minute: {int(guard) * minute}')

most_minutes_asleep = 0
laziest_guard = None
sleepiest_minute = None
for guard, minutes in guards.items():
    minute_most_asleep = max(minutes, key=lambda x: minutes[x])
    if minutes[minute_most_asleep] > most_minutes_asleep:
        laziest_guard = guard
        sleepiest_minute = minute_most_asleep
        most_minutes_asleep = minutes[minute_most_asleep]

print(f'Guard * minute: {int(laziest_guard) * sleepiest_minute}')
