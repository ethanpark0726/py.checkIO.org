# https://py.checkio.org/en/mission/the-most-frequent/

def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    # your code here
    a = set(data)
    temp = dict()
    
    for elem in a:
        temp[elem] = data.count(elem)
    
    for key, value in temp.items():
        if max(temp.values()) == value:
            return key


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")