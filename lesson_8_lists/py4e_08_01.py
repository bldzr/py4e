#define chop and middle functions   
def chop(t):
    del t[0]
    del t[len(t)-1]

def middle (t):
    return t[1:len(t)-1]

t = [1, 2, 3, 4, 5, 6, 7]

chop(t)
middle(t)

print(t)