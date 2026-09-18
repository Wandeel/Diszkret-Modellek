## Írj programot, amely a természetes számok egy adott halmazában megkeresi a tökéletes számokat!

S = {2,3,4,6,124}

def perfect_numbers(s):
  numbers = set()
  for elem in s:
    sum = 0
    for i in range(1, elem):
      if elem % i == 0:
        sum += i
    if elem == sum:
      numbers.add(elem)
  return numbers

assert perfect_numbers({6787, 4719}) == set()
assert perfect_numbers({6721, 1218, 677, 6, 5737, 6897, 4599, 2426, 28, 2143}) == {28, 6}
assert perfect_numbers({6, 7752, 3598, 7344, 4601, 28}) == {28, 6}
assert perfect_numbers({8128, 1027, 719, 496, 5715}) == {8128, 496}
assert perfect_numbers({8128, 4291, 3850, 1134, 978, 5427, 28}) == {8128, 28}
assert perfect_numbers({7841, 6, 3018, 496, 5971, 7414, 2301}) == {496, 6}
assert perfect_numbers({812, 4853}) == set()
assert perfect_numbers({6, 1415, 1839, 496, 6231, 27, 7388, 7710}) == {496, 6}
assert perfect_numbers({7208, 6108}) == set()
assert perfect_numbers({8128, 496, 6306}) == {8128, 496}
print("OK!")

#run
print("Perfect numbers of ", S, ": ", perfect_numbers(S))