def is_sorted(input_arr: list) -> bool:
    return all(int(input_arr[i]) <= int(input_arr[i + 1]) for i in range(len(input_arr) - 1)) or \
        all(int(input_arr[i]) >= int(input_arr[i + 1]) for i in range(len(input_arr) - 1))


def valid_increment(a: int, b: int) -> bool:
    diff = a - b
    return abs(diff) > 0 and abs(diff) <= 3


def read_input() -> int:
    safe_report = 0
    with open("input.txt", "r") as input_file:
        for line in input_file:
            tokens = line.split()

            if not is_sorted(tokens):
                continue

            for i in range(len(tokens) - 1):
                if not valid_increment(int(tokens[i]), int(tokens[i + 1])):
                    break
            else:
                safe_report += 1

        return safe_report


if __name__ == "__main__":
    safe_reports = read_input()
    print(safe_reports)
    
