# Too anhny too esehiig shalgah
def huvaagchTooloh(p):
    k=0
    for i in range(1,p+1):
        if p%i == 0: k+=1
    
    return k
def anhnyToo(p):
    if huvaagchTooloh(p) == 2:
        return True
    else:
        return False

print(anhnyToo(int(input())))