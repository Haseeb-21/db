def sort(list):
    if len(list) > 1:
 
        # Finds middle point of array
        middle = len(list)//2
 
        # Splits array into two halves
        left_half = list[:middle]
        right_half = list[middle:]
 
        # Sorts the two halves
        sort(left_half)
        sort(right_half)
 
        i = 0
        j = 0 
        k = 0
 
        # Copies data into temporary arrays 
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1
 
 
        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1
 
        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1 
    return list
