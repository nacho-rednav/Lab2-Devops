num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the average
average = (num1 + num2 + num3) / 3

# Display the result
print("The average of {}, {}, and {} is: {:.2f}".format(num1, num2, num3, average))

def largest_and_smallest(num1, num2, num3):
    numb = [num1, num2, num3]
    large = max(numb)
    small = min(numb)
    return large, small

large, small = largest_and_smallest(num1, num2, num3)
print("Largest:", large)
print("Smallest:", small) 