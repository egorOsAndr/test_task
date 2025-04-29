def func(n: int, m: int) -> str:
    arr: list[int] = [i + 1 for i in range(n)]
    answer: list = []
    index: int = 0
    while True:
        answer.append(arr[index])
        index = (index - 1 + m) % n
        if arr[index] == 1:
            break
    answer_str: list[str] = map(lambda x: str(x), answer)
    return ''.join(answer_str)


def main():
    n: int = int(input())
    m: int = int(input())
    print(func(n, m))


if __name__ == '__main__':
    main()
