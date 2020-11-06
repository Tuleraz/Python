fref = open("C:\Python\mbox-short3.txt")
cnt = 0
for line in fref:
    if line.startswith("From"):
        words = line.split()
        if len(words) < 2: continue
        if '@' not in words[1]: continue
        cnt += 1
        print(words[1])
print("There were %d lines in the file with From as the first word" %cnt)
