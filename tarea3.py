def busqueda_decreciente(A, x):
    low = 0
    high = len(A)-1
    middle = (low + high) // 2
    lower_index = len(A)
    while (low <= high):
            if x < A[middle]:                   #verify subarray to the right
                low = middle + 1
                middle = (low + high) // 2
            else:
                lower_index = middle               #verfiy subarray to the left
                high = middle - 1
                middle = (low + high) // 2
    return lower_index

print(busqueda_decreciente([8,5,5,2,1], 0))
