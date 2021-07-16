
# Task 3 - Palindrome
def recursive_poli(str):
    """receives @str and returns True if a polindrome and False otherwise"""
    if len(str) == 0 or len(str) == 1:
        return True
    return recursive_poli(str[1:-1]) if str[0] == str[-1] else False

def palindrome(str):
    """ received a @str string and returns the couple @a ; bool, @b : int where
        @a indicates if a palindrome > 1 was found and @b indicating its size"""
    a = False
    b = 0
    for size in range(2,len(str) + 1):
        for offset in range(len(str)- size + 1):
            substring = str[offset:offset+size]
            ans = recursive_poli(substring)
            if ans and len(substring) > b:
                a, b = True, len(substring)
    return a, b


def tests():
    tests = [("abbabbc",True,5),("abbabc",True,4),("abcdefg",False,0),("bascccca",True,4),("abacdefg",True,3),("aaabbcacacacccca",True,7)]
    for i in range(len(tests)):
        str = tests[i][0]
        exa = tests[i][1]
        exb = tests[i][2]
        a, b = palindrome(str)
        print(f"Test {i}: input: {str}\t (got: {a},{b} | ex: {exa},{exb})   ->\t {a == exa and b == exb}")
  
def main():
	tests()
    
main()