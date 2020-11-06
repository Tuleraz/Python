fref = open('c:\Python\mbox-short.txt')
out = []
for line in fref:
    words = line.split()
    for word in words:
        if word not in out:
            out.append(word)
out.sort()     
print(out)
