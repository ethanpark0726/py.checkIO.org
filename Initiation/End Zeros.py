# https://py.checkio.org/en/mission/end-zeros/

def end_zeros(num: int) -> int:
    # your code here
    num = str(num)[::-1]
    cnt = 0
    for elem in num:
        if elem == '0':
            cnt += 1
        else:
            break
    return cnt


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")