import sys

s = input("Write sentences: ")
symb = input("Write search symbol: ")[0]

i = 0
count = 0
sl = []

while i < len(s):
    if symb == s[i]:
        print(f"Symbol '{symb}' found on {i} position")
        count += 1
    i += 1

if count == 0:
    print(f"Symbol '{symb}' not found")
