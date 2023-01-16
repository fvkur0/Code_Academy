from itertools import permutations
answer = ''.join(list(permutations('0123456789'))[999999])
print(answer)