# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers smaller than the length of L,
whose value is input by the user, and outputs two lists:
- a list M consisting of L's middle element, followed by L's first element,
  followed by L's last element, followed by L's second element, followed by
  L's penultimate element...;
- a list N consisting of L[0], possibly followed by L[L[0]], possibly followed by
  L[L[L[0]]]..., for as long as L[L[0]], L[L[L[0]]]... are unused, and then,
  for the least i such that L[i] is unused, followed by L[i], possibly followed by
  L[L[i]], possibly followed by L[L[L[i]]]..., for as long as L[L[i]], L[L[L[i]]]...
  are unused, and then, for the least j such that L[j] is unused, followed by L[j],
  possibly followed by L[L[j]], possibly followed by L[L[L[j]]]..., for as long as
  L[L[j]], L[L[L[j]]]... are unused... until all members of L have been used up.
'''


import sys
from random import seed, randrange


try:
    arg_for_seed, length = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length = int(arg_for_seed), int(length)
    if arg_for_seed < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randrange(length) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)
M = []
N = []

# Replace this comment with your code
# mid_e = length//2
# M list
if length ==0:
    M = []
elif length ==1:
    M = L
elif length ==2:
    M = L[::-1]
else:
    begin = 0
    last = length - 1
    M_tag = 0
    M.append(L[length//2])

    while last != begin :
        M.append(L[begin])
        M.append(L[last])
        begin += 1
        last -= 1
        if begin == last - 1 :
            M.append(L[begin])
            break

# N list
temp = []
for i in range (0, len(L)):
    temp.append(L[i])
index = 0

for i in range(0, len(L)):
    if temp[index] != -1:
        N.append(temp[index])
    else:
        for i in range(0,len(L)):
            if temp[i] != -1:
                index = i
                break;
        N.append(temp[index])
            
        
    temp_index = temp[index]
    temp[index] = -1
    index = temp_index
    
    
print('\nHere is M:')
print('  ', M)
print('\nHere is N:')
print('  ', N)
print('\nHere is L again:')
print('  ', L)


