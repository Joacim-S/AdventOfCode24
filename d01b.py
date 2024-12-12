with open(f'inputs/d1.txt') as input:
  data = input.read().split('\n')

left = {}
right = {}
total = 0

for row in data:
  if row:
    split_row = row.split('   ')

    if (split_row[0]) not in left:
      left[(split_row[0])] = 0
    if split_row[1] not in right:
      right[split_row[1]] = 0

    left[(split_row[0])] += 1
    right[split_row[1]] += 1

for key, val in left.items():
  if key in right:
    total += val * int(key) * right[key]

print(total)