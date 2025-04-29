from collections import namedtuple

Circle = namedtuple('Circle', ['x0', 'y0', 'r'])
Point = namedtuple('Point', ['x', 'y'])


def read_file1(name: str) -> Circle:
    with open(name, 'r') as f:
        s: str = f.read()
        lines: list = s.splitlines()
        x0, y0 = map(float, lines[0].split())
        r: float = float(lines[1])
        return Circle(x0, y0, r)


def read_file2(name: str) -> list[Point]:
    with open(name, 'r') as f:
        arr: list[Point] = []
        for line in f:
            x, y = map(float, line.split())
            arr.append(Point(x, y))
        return arr


def func(circle: Circle, arr: list[Point]):
    result: list[int] = []
    for pair in arr:
        equation = (pair.x - circle.x0) ** 2 + (pair.y - circle.y0) ** 2
        if equation < circle.r ** 2:
            result.append(1)
        # float может иногда не правильно округлять добавил такую проверку, 
        if abs(equation - circle.r ** 2) < 1e-6:
            result.append(0)
        else:
            result.append(2)
    for _ in result:
        print(_)


def main():
    c = read_file1('file1.txt')
    p = read_file2('file2.txt')
    func(c, p)


if __name__ == '__main__':
    main()
