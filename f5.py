# too palendrom eseh
def palendromToo(n):
    return int(str(n)[::-1]) == n
print(palendromToo(int(input())))