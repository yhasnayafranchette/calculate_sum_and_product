#Exercise 1: Calculate the multiplication and sum of two numbers
#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

#input first and second number
def product_or_sum():
    first_number = int(input("Enter the first number:"))
    second_number = int(input("Enter the second number:"))

#Calculate the product of first and second number
    product = first_number * second_number

#Calculate sum of the first and second number
    sum = first_number + second_number

#If the product is less than or equal to 1000, display product. If false, display sum
    if product <=1000:
        print ("The result is", product)

    else:
         print ("The result is", sum)

product_or_sum()

