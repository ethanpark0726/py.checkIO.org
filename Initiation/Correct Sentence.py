# https://py.checkio.org/en/mission/correct-sentence/

def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    length = len(text)
    prefix = text[0]
    if prefix.isupper() == False:
        correctText = text[0].upper()
    else:
        correctText = prefix
    
    if text[length - 1] == '.':
        correctText = correctText + text[1:]
    else:
        correctText = correctText + text[1:] + '.'
    return correctText


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
