# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # Your code here
    results = []
    while( arrA and arrB):
        if arrA <= 1 and arrB <= 1:
            return results
        if arrA[0] < arrB[0]:
            results.append(arrA[0])
            arrA.pop(0)
        elif arrA[0] > arrB[0]:
            results.append(arrB[0])
            arrB.pop(0)
        
    if arrA:
        results += arrA
    if arrB:
        results +=arrB


    return results

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    #Give it a middle index, and then:
    middle_index = len(arr) // 2
    #split into two slices, left
    left_slice = arr[:middle_index]
    #and right
    right_slice = arr[middle_index:]
    
    left_sorted = merge_sort(left_slice)
    right_sorted = merge_sort(right_slice)

    return merge(left_sorted, right_sorted)

    #First, look at the first num in each array
    #Find the one that's smaller
    #Then, look at next pair of nums, leaving pointer at the larger of the 2 nums
    #so that we can compare it againt the next num


    # return arr
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

