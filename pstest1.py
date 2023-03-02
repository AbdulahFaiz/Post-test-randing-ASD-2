import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)


my_list = [random.randint(1, 100) for i in range(12)]
print("Random list:", my_list)

while True:
    print ("\n[1] = quick sort\n[2] = merge sort")
    pilihan = input("Silahkan pilih metode sorting yang ingin anda gunakan : ")
    if  pilihan == "1":
        sorted_list = quick_sort(my_list.copy())
        print("\nSorted list menggunakan quick sort :\n",sorted_list)
        break
    elif    pilihan == "2":
        merge_sort(my_list)
        print("\nSorted list menggunakan merge sort :\n",my_list)
        break
    else:
        print("Invalid")