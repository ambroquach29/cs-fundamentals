# This problem can be solved using the 2-pointer technique as well.

def add_binary(a: str, b: str) -> str:
    # Get the max length between 2 strings 
    # then fill the left of both string with 0s
    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)
    
    carry, result = 0, ''
    
    for i in reversed(range(n)):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1
        
        #Append result to string after using carry to compute addition
        result = ('1' if carry % 2 == 1 else '0') + result
        
        # Compute the carry: 1 -> carry = 0; 2 -> carry = 1
        # carry = 0 if carry < 2 else 1
        carry //= 2
        
        
    if carry == 1:
        result = '1' + result
            
    return result

def main():
    str1_list = ["1100", "1010100", "10101", "1111", "10101100110010101"]
    str2_list = ["0011", "0100011", "01010", "11111", "1011001010110010100"]

    for i in range(len(str1_list)):
        print(str(i+1) + ".\tFirst input string:  ",str1_list[i])
        print("\tSecond input string: ",str2_list[i])
        
        print("\tBinary Sum:          ", add_binary(str1_list[i],str2_list[i]))
        print('-'*100);
  
if __name__ == '__main__':
    main()
