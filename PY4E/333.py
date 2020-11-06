fhand = open('C:\Python\mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) < 2 : continue
    if words[0] != 'From' : continue
    print(words[2])
