# https://py.checkio.org/en/mission/max-digit/

def max_digit(number: int) -> int:
    # your code here
    strNum = str(number)
    max = int(strNum[0])
    
    if len(strNum) == 1:
           return number
    else:
        for elem in strNum[1:]:
            print(elem)
            if int(elem) > max:
                max = int(elem)
           
        return max


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
