num = int(input("Enter a number: "))
original_num = num
reverse_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
if original_num == reversed_num:
    print(" it is a palindrome number.")
else:
    print(" not a palindrome number.")
