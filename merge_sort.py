#MERGE SORT


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0

    # Merge the two sorted halves
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # Collect any remaining elements
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

#--------------------------------------------------------------------------------------------------
#TYPE 2

def merge(l,low,mid,high):
    left=l[low:mid+1]
    right=l[mid+1:high+1]
    i=j=0
    t=low
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l[t]=left[i]
            t+=1
            i+=1
        else:
            l[t]=right[j]
            t+=1
            j+=1
    while i<len(left):
        l[t]=left[i]
        t+=1
        i+=1
    while j<len(right):
        l[t]=right[j]
        t+=1
        i+=1
        j+=1
    print(l)
    
def merge_sort(l,low,high):
    if low<high:
        mid=low+(high-low)//2
        print(mid,l[low:mid+1],l[mid+1:high+1])
        merge_sort(l,low,mid)
        print(mid)
        print(mid,l[low:mid+1],l[mid+1:high+1])
        merge_sort(l,mid+1,high)
        merge(l,low,mid,high)
    return

if __name__=="__main__":
    l=list(map(int,input().split()))
    low=0
    high=len(l)-1
    print(low,high)
    merge_sort(l,low,high)
    print(f"sorted array: {l}")
