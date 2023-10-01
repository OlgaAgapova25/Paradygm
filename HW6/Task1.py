# Бинарный поиск

lst = [1, 3, 5, 6, 9, 12, 14]
value = 14

i_mid = len(lst) // 2
i_min = 0
i_max = len(lst) - 1

while lst[i_mid] != value and i_min <= i_max:
    if value > lst[i_mid]:
        i_min = i_mid + 1
    else:
        i_max = i_mid - 1
    i_mid = (i_min + i_max) // 2

if i_min > i_max:
    print("No value")
else:
    print(f"Index of the value is {i_mid}")