import sys

#print(sys.argv)
filename = sys.argv[1]
f = open(filename, 'r')
x = f.read().split()
temp=[]
dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for word in x:
  temp=len(word)
  if temp in dict:
    dict[temp]+=1

for k,v in sorted(dict.items()):
    print(k, v)
