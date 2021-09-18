def sel_sort(L):
    n = len(L)
    for i in range(n-1,-1,-1):
        max_idx = i
        for j in range(i-1,-1,-1):
            if L[j] > L[max_idx]:
                max_idx = j
        L[i], L[max_idx] = L[max_idx], L[i]

L = [2,4,6,8,1,3,5,7,9]
sel_sort(L)

print(L)

        
