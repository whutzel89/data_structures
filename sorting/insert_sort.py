def insertion_sort(unsorted):
    n = len(unsorted)
    i = 1
    while i < n:
        current = unsorted[i]
        j = i - 1
        while j>= 0 and unsorted[j] > current:
            unsorted[j+1] = unsorted[j]
            j = j -1
        unsorted[j+1] = current
        i = i + 1

    return unsorted

if __name__ == "__main__":
    sorted = insertion_sort([21,54,123,9234,1,23124,1,1])
    print(sorted)
    
