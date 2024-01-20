#Exercise 1: Calculate the multiplication and sum of two numbers
#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def product_or_sum():
    first_number = int(input("Enter the first number:"))
    second_number = int(input("Enter the second number:"))

    product = first_number * second_number
    sum = first_number + second_number

    if product <=1000:
        print ("The result is", product)

    else:
         print ("The result is", sum)

product_or_sum()

