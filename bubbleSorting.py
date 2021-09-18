def bubble_sort(L):
    n = len(L)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if(L[j] > L[j+1]):
                L[j],L[j+1] = L[j+1], L[j]

L = [1,3,5,7,9,2,4,6,8]
bubble_sort(L)

print(L)