class countsort:
    def countsort(array):
        if len(array) < 2:
            return array
        max = max(array)
        count = [0] * (max + 1)
        for num in array:
            count[num] += 1
        sorted = []
        for value, freq in enumerate(count):
            sorted.extend([value] * freq)
        return sorted
    
    def vf(original, sorted):
        if sorted(original) and len(original) == len(sorted):
            return(sorted)