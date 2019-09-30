# toony cifruudiin niilber
def cifruudiinNiilber(n):
    return sum(int(i) for i in str(n))
    # niilber = 0
    # for i in str(n):
    #     niilber = niilber + int(i)
    # return niilber
print(cifruudiinNiilber(int(input())))