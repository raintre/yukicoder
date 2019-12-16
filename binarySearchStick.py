def read_data():
    N_ = int(input())
    L_ = list(map(int, input().split()))
    K_ = int(input())
    return N_, L_, K_

def binarySearch(N, L, K):
    left = 0
    right = max(L)
    for x in range(100):
        piv = 0
        mid = (right + left) / 2
        for l in L:
            piv += l // mid
        if piv >= K:
            left = mid
        else:
            right = mid
    return (right + left) / 2

N, L, K = read_data()
print(binarySearch(N, L, K))
