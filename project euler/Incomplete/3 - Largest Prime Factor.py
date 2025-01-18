"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

number = int(input("What is the number: "))
primelist = []

for i in range (2, number):
    if number%i==0:
        primelist.append(i)
        
print(primelist)