import json


def read_values(namefile: str) -> dict[int, str]:
    with open(namefile, 'r') as f:
        data: dict = json.load(f)
        result: dict = {}
        for item in data['values']:
            result[item['id']] = item['value']
        return result


def read_tests(namefile: str) -> dict:
    with open(namefile, 'r') as f:
        data: dict = json.load(f)
        return data


def fill_tests(test: dict, result: dict[int, str]):
    test_id = test.get('id')
    if test_id in result:
        test['value'] = result[test_id]
    if 'values' in test:
        for child in test['values']:
            fill_tests(child, result)


def main():
    values = read_values('task3/values.json')
    tests_data = read_tests('task3/tests.json')

    for test in tests_data['tests']:
        fill_tests(test, values)

    with open('task3/report.json', 'w', encoding='utf-8') as f:
        json.dump(tests_data, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
