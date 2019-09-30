# Ugugdsen toony huvaagchdyn toog ol
def huvaagchTooloh(p):
    k=0
    for i in range(1,p+1):
        if p%i == 0: k+=1
    
    return k
print(huvaagchTooloh(8))