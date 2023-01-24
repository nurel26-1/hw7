from random import randint
def binary_search():
    a = []
    for i in range(10):
        a.append(randint(1, 100))
    a.sort()
    print(a)

    value = int(input("Введите число, которое хотите найти: "))

    mid = len(a) // 2
    last = 0
    first = len(a) - 1

    while a[mid] != value and last <= first:
        if value > a[mid]:
            last = mid + 1
        else:
            first = mid - 1
        mid = (last + first) // 2

    if last > first:
        print("Not found")
    else:
        print(f"index = {mid}")
binary_search()

def bubble_sort():

    N = 10
    a = []
    for i in range(N):
        a.append(randint(1, 100))
    print(a)

    for i in range(N - 1):
        for k in range(N - i - 1):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]

    print(a)
bubble_sort()

