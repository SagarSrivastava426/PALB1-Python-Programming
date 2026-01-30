arr = [1, 4, 3, 5, 8, 6]

min = arr[0]
max = arr[0]

i = 1
while i < len(arr):
    if arr[i] < min:
        min = arr[i]
    if arr[i] > max:
        max = arr[i]
    i += 1

print([min, max])
