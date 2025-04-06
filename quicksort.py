def sort(array):
    def quicksort(array):
        if len(array) < 2:
            return array
        pivot = array[len(array)//2]
        left = [x for x in array if x < pivot]
        middle = [y for y in array if y == pivot]
        right = [z for z in array if z > pivot]
        return quicksort(left) + quicksort(middle) + quicksort(right)
    return quicksort(array)
    
def vf(original, result):
    if sorted(original) and len(original) == len(result):
        return(result)
     