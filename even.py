import sys

script_name = sys.argv[0]


numbers = [int(num) for num in sys.argv[1:]]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Numbers List:", numbers)
print("Count of Even Numbers:", even_count)
print("Count of Odd Numbers:", odd_count)
