# toon daraallyn ih bolon bagyn bair solih
def swap(n):
    ih = n.index(max(n))
    baga = n.index(min(n))
    n[ih], n[baga] = min(n), max(n)
    return n
n=input().split()
print(swap(n))