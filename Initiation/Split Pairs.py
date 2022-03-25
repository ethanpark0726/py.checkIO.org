# https://py.checkio.org/en/mission/split-pairs/

def split_pairs(a):
    # your code here
    temp = list()
    if len(a) <= 2:
        if len(a) == 0:
            return a
        elif len(a) == 2:      
            temp.append(a)
            return temp
        elif len(a) == 1:
            temp.append(a[0] + '_')
            
            return temp
    else:
        div = len(a)
    
        if div % 2 == 0:
            for i in range(0, div, 2):
                temp.append(a[i:i+2])      
            print(temp)
            return temp
        else:
            for i in range(0, int(div / 2) + 1, 2):
                
                temp.append(a[i:i+2])
                
            temp.append(a[-1] + "_")
            print(temp)
            return temp


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('BC')) == ['BC']
    print("Coding complete? Click 'Check' to earn cool rewards!")
