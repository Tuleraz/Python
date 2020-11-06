fname = input("Enter filename: ")
if fname == '': fname = "C:\Python\mbox-short1.txt"
outd = dict()
try:
    fref = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fref:
    line.rstrip()
    words = line.split()
    if len(words) < 3: continue
    if '@' not in words[1]: continue
    outd[words[1]] = outd.get(words[1],0) + 1 
print(outd)

