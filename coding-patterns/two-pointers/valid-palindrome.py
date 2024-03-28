# Check if a string is a valid palindrome

def is_palindrome(s):
    # List comprehension to filter out non-alphanumeric characters
    filtered_chars = [char.lower() for char in s if char.isalnum()]

    start = 0
    end = len(filtered_chars) - 1

    while start < end:
        if filtered_chars[start] != filtered_chars[end]:
            return False
        start += 1
        end -= 1
    return True


def main():

    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR", "A man, a plan, a canal: Panama"]
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        print("The input string is '", test_cases[i], "' and the length of the string is ", len(test_cases[i]), ".", sep='')
        print("Is it a palindrome?.....", is_palindrome(test_cases[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
