# Convert string to integer (atoi)

def string_to_int(s: str) -> int:
	# Return 0 if string is empty
    if not s:
        return 0
    
    i = 0
    n = len(s)
    sign = 1
    result = 0
    
    # Ignore whitespace
    while i < n and s[i] == ' ':
        i += 1
        
    # Get sign
    if i < n:
        if s[i] == '-':
            sign = -1 
        if s[i] == '-' or s[i] == '+':
            i += 1
    
    # Process digits
    while i < n and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
    
    # Apply sign
    result *= sign
    
    # Clamp result to 32-bit signed integer range
    result = max(min(result, 2**31 - 1), -2**31)
    
    return result

def main():
    input_strings = ["25", "   -25", "999 with words", "words and 567", "-91283472332", "91283472332"]
  
    for i in range(len(input_strings)):
        print(i+1, ".\tInput string     : ", end="")
        print('"{0}"'.format(input_strings[i]))
        
        stoi = string_to_int(input_strings[i])
        
        print("\tConverted integer: ", stoi)
        print("-" * 100)

if __name__ == '__main__':
  main()

# (*) Clean up code above:
# Get sign
# if i < n:
#     if s[i] == '-':
#         sign = -1
#         i += 1
#     elif s[i] == '+':
#         i += 1


# This comparison would cause an overflow: result * 10 + digit > 2**31 - 1
# So, we use algebraic manipulation to rearrange the operands without performing actual computation.
# Checks for overflow at each iteration.
# while i < n and s[i].isdigit():    
#     if result > (2**31 - 1 - digit) // 10:
#         return sign * (2**31 - 1) if sign == 1 else sign * (2**31)
#     result = result * 10 + digit
#     i += 1
