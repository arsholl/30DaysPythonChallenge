#Exercises - Day 3
#Declare your age as integer variable
age = 26
#Declare your height as a float variable
height = 5.2
#Declare a complex number variable
complex_number = 6 + 54j
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base: "))
height = float(input("Enter height: "))
print("The area of a triangle is", 0.5 * base * height)
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
sideA = int(input("Enter side a: "))
sideB= int(input("Enter side b: "))
sideC = int(input("Enter side c: "))
print("The perimeter of the triangle is", sideA + sideB + sideC)
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter length: "))
width = int(input("Enter width: "))
print("The area of a rectangle is", length * width)
print("The perimeter of a rectangle is", 2 * (length + width))
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius = int(input("Enter radius: "))
print("The area of a circle is", pi * radius**2)
#Find the length of 'python' and 'jargon' and make a falsy comparison statement.
print(len("python"))
print(len("jargon"))
print("\t\t\t\tCONGRATULATIONS!")