from collections import Counter
import sys

filename = sys.argv[1]
f = open(filename, 'r')
x = f.read().strip()
lines=[]
for line in x:
        line = line.strip() #strip spaces else space will come as a character
        if line:
            lines.append(line)

print(Counter(lines).most_common(5))
