#  File: Palindrome.py

#  Description: A string is entered so that it can be converted into a palindrome by adding letters to the beginning of the string

#  Student Name: Vaishanvi Sathiyamoorthy

#  Student UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/01/2022

#  Date Last Modified: 10/01/2022

import sys
# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
    # The position of insertion and the position of the letter being inserted are determined
    index_positions = 0
    letter = -1
    # If the is_palindrome function returns true, the string will be returned
    # else, the string is converted to a list. the letter position from the string is inserted into the index position
    while True:
        if is_palindrome(str) == True:
            return str
        else:
            lst = list(str)
            lst.insert(index_positions, str[letter])
            str = ""
            for i in range(len(lst)):
                str += lst[i]
            index_positions += 1
            letter -= 1

# This function returns whether a word is a palindrome or not
# If the first letter does not equal the last letter of the string, the function returns false
def is_palindrome(str):
    if (str == ""):
        return True
    else:
        if (str[0] == str[-1]):
            word = str[1:-1]
            return is_palindrome(word)
        else:
            return False
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  assert smallest_palindrome("b") == "b"
  assert smallest_palindrome("bb") == "bb"
  assert smallest_palindrome("cd") == "dcd"
  assert smallest_palindrome("racecar") == "racecar"
  assert smallest_palindrome("abacm") == "mcabacm"

  return "all test cases passed"

def main():
    # run your test cases

    # print (test_cases())


    # read the data
    # while loop keeps going until an empty string is returned by readline
    data = sys.stdin
    line = data.readline().strip()
    while line != "":
        print(smallest_palindrome(line))
        line = data.readline().strip()

    # print the smallest palindromic string that can be made for each input

if __name__ == "__main__":
  main()
