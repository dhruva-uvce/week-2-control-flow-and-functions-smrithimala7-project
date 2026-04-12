# Q08. Sum of Digits (while loop)
#
# Ask the user for a positive integer.
# Print the sum of its digits using a while loop.
#
# Sample Input:   Enter a number: 9876
# Sample Output:  Sum of digits of 9876 = 30

n=int(input("Enter a number: "))
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)
