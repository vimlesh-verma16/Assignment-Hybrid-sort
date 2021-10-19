def hybrid(A,n):
    comp = 0
    swaps = 0
    alreadySorted=False
    swapped=False
    for i in range(n//2):
        small = i
        for j in range(i,n-i-1):
            if not alreadySorted:
                comp += 1
                if(A[j]>A[j+1]):
                    swaps += 1
                    A[j+1],A[j] = A[j],A[j+1]
                    swapped = True
            comp += 1
            if(A[j]<A[small]):
                small = j
        if small!=i:
            swaps += 1
            A[small],A[i] = A[i],A[small]
        if not swapped:
            alreadySorted=True
    
    print(A)
    print(comp,swaps)
a=[0,1,5,3,4,2]
hybrid(a,len(a))