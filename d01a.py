with open(f'inputs/d1.txt') as input:
  data = input.read().split('\n')

left = []
right = []
total = 0

for row in data:
  if row:
    split_row = row.split('   ')
    left.append(int(split_row[0]))
    right.append(int(split_row[1]))
  
left.sort()
right.sort()

for (l, r) in zip(left, right):
  total += abs(l-r)

print(total)