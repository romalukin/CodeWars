#The same as 'simple_fraction_to_mixed_number_converter.py', but without any libraries. It's veeeeeeeeeeeeeery slow 

def mixed_fraction(s):
    s = list(map(int, s.split('/')))
    div = []
    negative_result = ''
    k = 0

# check for negative result
    if s[0]/s[1] < 0:
        negative_result = '-'
    elif s[0] == 0 and s[1] != 0:
        return '0'

# get the floor 
    if abs(s[0]) >= abs(s[1]):
        k = abs(s[0]) // abs(s[1])
        s[0] = abs(s[0]) - k * abs(s[1])
        if abs(k) == 1 and s[0] == 0:
            return '{}{}'.format(negative_result, str(k))
        if s[0] == 0:
            return '{}{}'.format(negative_result, str(k))
        

# make the fraction easier
    for i in range(1, abs(s[0]+1)):
        if (s[0]/i).is_integer() and (s[1]/i).is_integer():
            div.append([abs(s[0]//i), abs(s[1]//i)])
    div = min(div)

#result
    if k != 0 and len(div) != 0:
        return '{}{} {}/{}'.format(negative_result, str(k), str(div[0]), str(div[1]))
    elif k == 0 and len(div) != 0:
        return '{}{}/{}'.format(negative_result, str(div[0]), str(div[1]))

from sys import argv

a = argv[1]
b = '-2688680/-4184384'
print(mixed_fraction(a))