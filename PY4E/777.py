outlist = []
while True:
    inum = input("Enter a number:")
    if not inum.isdecimal():
        if "done" in inum: break
        print("this is not a number")
        continue
    outlist.append(float(inum))
print(outlist)
print("Maximum: %g" % max(outlist))
print("Minimum: %g" % min(outlist))
