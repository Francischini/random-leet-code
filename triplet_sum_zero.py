# O(n^3) time complexity
def triplet_sum_zero(arr):
    sample_arr = []
    total = 0

    for i in range(len(arr)):
        j = i+1
        while j < len(arr):
            k = j+1
            while k < len(arr):
                sample_arr.append(arr[i])
                sample_arr.append(arr[j])
                sample_arr.append(arr[k])
                if sum(sample_arr) == 0:
                    print("sample_arr:", sample_arr)
                    total += 1
                    sample_arr = []
                else:
                    sample_arr = []
                k += 1
            j += 1
        
    print("TOTAL: ", total)


arr = [-1,0,1,2,-1,-4]
triplet_sum_zero(arr)

