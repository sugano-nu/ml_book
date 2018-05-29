import re
numlist = list()
hand = open('regex_sum_80211.txt')
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0:
        continue
    for x in stuff:
        numlist.append(int(x))
print(sum(numlist))
