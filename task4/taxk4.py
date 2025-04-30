def read_file(namefile: str) -> list:
    arr: list = []
    with open(namefile, 'r') as f:
        for line in f:
            arr.append(int(line))
        arr.sort()
        return arr


def func(arr: list) -> int:
    size_arr = len(arr)
    count = 0
    if size_arr % 2 != 0:
        index = size_arr // 2
        med = arr[index]
        for num in arr:
            count += abs(med - num)
        return count
    else:
        two = [0, 0]
        index1 = (size_arr // 2) - 1
        index2 = size_arr // 2
        med1 = arr[index1]
        med2 = arr[index2]
        for num in arr:
            two[0] += abs(med1 - num)
            two[1] += abs(med2 - num)
        return min(two)


def main():
    arr: list = read_file('task4/file.txt')
    print(arr)
    print(func(arr))


if __name__ == '__main__':
    main()
