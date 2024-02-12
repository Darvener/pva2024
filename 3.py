def is_palindrome(num_str):
    return num_str == num_str[::-1]

def nextPalindrome(from_num, radix, next):
    if not 2 <= radix <= 36:
        return 0
    
    num = from_num + 1
    max_val = 2**64 - 1
    while num <= max_val:
        num_str = ''
        n = num
        while n > 0:
            digit = n % radix
            if digit < 10:
                num_str = str(digit) + num_str
            else:
                num_str = chr(ord('A') + digit - 10) + num_str
            n //= radix
        if is_palindrome(num_str):
            next[0] = num
            return 1
        num += 1
    return 0

def main():
    try:
        from_num = int(input("Zadejte číslo: "))
        radix = int(input("Zadejte číselnou soustavu (2 až 36): "))
        if not 2 <= radix <= 36:
            print("Chybná číselná soustava.")
            return
        next_palindrome_num = [0]
        success = nextPalindrome(from_num, radix, next_palindrome_num)
        if success:
            print(f"Nejbližší > palindrom než {from_num} v číselné soustavě {radix} je: {next_palindrome_num[0]}")
        else:
            print("Nepodařilo se najít palindrom.")
    except ValueError:
        print("ERROR.")

if __name__ == "__main__":
    main()
