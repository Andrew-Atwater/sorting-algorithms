class quicksort:
    def find_piv(array):
        if len(array) < 2:
            return array
        pivot = array[0]