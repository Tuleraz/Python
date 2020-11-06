def chop(Li):
    if len(Li) > 1:
        del Li[len(Li)-1]
        del Li[0]
    return None
a = [3]
chop(a)
print(a)

def middle(t):
    if len(t) > 1:
        return t[1:len(t)-1]
    else:
        return t
b = [7]
print(middle(b))

