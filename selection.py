class selection:
    def sort(array):
        if len(array) < 2:
            return array
        x = len(array)
        for i in range(x - 1):
            min = i
            for j in range(i + 1, x):
                if array[j] < array[min]:
                    min = j
            array[i], array[min] = array[min], array[i]
        return array
    def vf(original, sorted):
        if sorted(original) and len(original) == len(sorted):
            return(sorted)