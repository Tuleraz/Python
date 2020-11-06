fname = "C:\Python\mbox-short.txt"
outd = dict()
try:
    fref = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fref:
    line.rstrip()
    words = line.split()
    if len(words) == 0: continue
    for word in words:
        outd[word] = ''
print(outd)
print('Itf' in outd)
