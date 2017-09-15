import sys

filename = sys.argv[1]
f = open(filename, 'r')
words[] = f.read().split()

letters = dict(a={"first": 0, "middle": 0, "last": 0}, b={"first": 0, "middle": 0, "last": 0},
               c={"first": 0, "middle": 0, "last": 0}, d={"first": 0, "middle": 0, "last": 0},
               e={"first": 0, "middle": 0, "last": 0}, f={"first": 0, "middle": 0, "last": 0},
               g={"first": 0, "middle": 0, "last": 0}, h={"first": 0, "middle": 0, "last": 0},
               i={"first": 0, "middle": 0, "last": 0}, j={"first": 0, "middle": 0, "last": 0},
               k={"first": 0, "middle": 0, "last": 0}, l={"first": 0, "middle": 0, "last": 0},
               m={"first": 0, "middle": 0, "last": 0}, n={"first": 0, "middle": 0, "last": 0},
               o={"first": 0, "middle": 0, "last": 0}, p={"first": 0, "middle": 0, "last": 0},
               q={"first": 0, "middle": 0, "last": 0}, r={"first": 0, "middle": 0, "last": 0},
               s={"first": 0, "middle": 0, "last": 0}, t={"first": 0, "middle": 0, "last": 0},
               u={"first": 0, "middle": 0, "last": 0}, v={"first": 0, "middle": 0, "last": 0},
               w={"first": 0, "middle": 0, "last": 0}, x={"first": 0, "middle": 0, "last": 0},
               y={"first": 0, "middle": 0, "last": 0}, z={"first": 0, "middle": 0, "last": 0})

for word in words:
    first_letter = word[0]
    last_letter = word[-1]
    middle_letters = word[1:-1]

    print(first_letter, middle_letters, last_letter)

    letters[first_letter]["first"] += 1
    letters[last_letter]["last"] += 1

    for ch in middle_letters:
        letters[ch]["middle"] += 1
print(letters)
