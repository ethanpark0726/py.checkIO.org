# https://py.checkio.org/en/mission/all-upper/

def is_all_upper(text: str) -> bool:
    # your code here
    if text.isupper():
        return True
    else:
        if len(text.strip(' ')) == 0 or text.replace(" ", "").isnumeric():
            return True
        else:
            return False


if __name__ == '__main__':

 

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
