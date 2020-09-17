'''
Define a function that finds the lenght of the longest
substring that is a palindrome
'''

test_cases = ['tacocat', '1234321', '12345678', 'hola aloh', 'abc', '011lo']

def longest_palindrome_lenght(n, s):
    '''
    n: s's lenght
    s: string
    '''
    if n < 2:
        #strings of zero or one chars are palindromes
        return n
    if n == 2:
        if s[0] == s[1]:    #it's a palindrome'
            return n
        else:
            return n-1

    if s[0] == s[-1]:   #the extremes are good
        return 2 + longest_palindrome_lenght(n-2, s[1:-1])
    return max(longest_palindrome_lenght(n-1, s[1:]),
               longest_palindrome_lenght(n-1, s[:-1]))

for s in test_cases:
    print(longest_palindrome_lenght(len(s), s))
