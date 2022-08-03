def summa(number_1: int, number_2: int) -> int:
    return number_1 + number_2


def difference(number_1: int, number_2: int) -> int:
    return number_1 - number_2


def multy(number_1: int, number_2: int) -> int:
    return number_1 * number_2


def quotient(number_1: int, number_2: int) -> float:
    if number_2 == 0:
        result = -1
    else:
        result = number_1 / number_2
    return result


def calculator(mode: int):
    print("enter two numbers")
    try:
        first_number = int(input())
        second_number = int(input())
    except ValueError:
        print("it is not integer\n")
    else:
        if mode == 1:
            print(summa(first_number, second_number), "\n")
        elif mode == 2:
            print(difference(first_number, second_number), "\n")
        elif mode == 3:
            print(multy(first_number, second_number), "\n")
        elif mode == 4:
            res = quotient(first_number, second_number)
            if res == -1:
                print("bad instruction\n")
            else:
                print(res, "\n")


if __name__ == '__main__':
    work = 0
    while work != 1:
        print("press '1' to calculate the sum")
        print("press '2' to calculate the difference")
        print("press '3' to calculate the multiplication")
        print("press '4' to calculate the quotient")
        print("press 'q' to exit")
        behavior = input()
        if behavior == 'q':
            work = 1
        else:
            modes = ['1', '2', '3', '4']
            flag = 0
            for i in modes:
                if behavior == i:
                    flag = 1
                    break
            if flag == 1:
                calculator(int(behavior))
            else:
                print("We doesn't know what need to do\n")
