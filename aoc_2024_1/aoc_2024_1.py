from typing import Tuple, List


def read_input() -> Tuple[List[str], List[str]]:
    with open("input.txt", "r") as input_file:
        input_arr = input_file.readlines()
        list1, list2 = [], []
        for i in input_arr:
            list1.append(i.split()[0])
            list2.append(i.split()[1])

        return list1, list2


def qsort_list(input: list) -> list:
    if len(input) < 2:
        return input

    else:
        pivot = input[0]
        less = [i for i in input[1:] if i < pivot]
        equal = [i for i in input if i == pivot]
        greater = [i for i in input[1:] if i > pivot]

    return qsort_list(less) + equal + qsort_list(greater)


def get_distance() -> int:
    list1, list2 = read_input()
    sorted1 = qsort_list(list1)
    sorted2 = qsort_list(list2)
    distance = 0

    for i in range(len(sorted1)):
        distance += abs(int(sorted1[i]) - int(sorted2[i]))

    return distance


if __name__ == "__main__":
    distance = get_distance()
    print(distance)
