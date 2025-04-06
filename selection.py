class selection:
    def selection(array):
        x = len(array)
        for i in range(x - 1):
            min = i
            for j in range(i + 1, x):
                if array[j] < array[min]:
                    min = j
        target = array.pop(min)
        array.insert(i, target)