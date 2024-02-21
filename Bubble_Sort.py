arr = [9, 8, 8, 1, 2, 4, 6, 5]

for i in range(len(arr)):
    check = False
    for j in range(len(arr) - 1):
        if arr[j + 1] < arr[j]:
            check = True
            temp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = temp
    if check == False:
        break
    print(i, arr)
