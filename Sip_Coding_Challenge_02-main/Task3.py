string = 'hi dee hi how are you mr dee'
words = string.split()
counter = {}

for i in words:
    if i in counter:
        counter [i] +=1
    else:
        counter[i] = 1
print(counter)
