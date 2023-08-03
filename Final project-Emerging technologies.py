print("Welcome to the Calculator")

print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
print("Press 5 for modulas")
print("Press 6 for square")
print("Press 7 for logarithm")
print("Press 8 for natural exponent")
print("Press 9 for trignometric values")
print("Press 10 for factorial")
print("Press 11 for area of circle")
print("Press 12 for area of square")

x = int(input("The number you pressed is: "))

if x == 1:
    print("ADDITION")
    print("--------")
    a = float(input("Enter number 1 = "))
    b = float(input("Enter number 2 = "))
    w = a+b
    print("The addition of",a, "and" ,b, "is" ,w)
elif x == 2:
    print("SUBTRACTION")
    print("-----------")
    a = float(input("Enter number 1 = "))
    b = float(input("Enter number 2 = "))
    r = a-b
    print("The subtrcation of",a, "and" ,b, "is" ,r)
elif x == 3:
    print("MULTIPLICATION")
    print("--------------")
    a = float(input("Enter number 1 = "))
    b = float(input("Enter number 2 = "))
    u = a*b
    print("The multiplication of",a, "and" ,b, "is" ,u)
elif x == 4:
    print("DIVISION")
    print("--------")
    a = float(input("Enter number 1 = "))
    b = float(input("Enter number 2 = "))
    p = a/b
    print("The division of",a, "and" ,b, "is" ,p)
elif x == 5:
    print("MODULAS")
    print("-------")
    a = float(input("Enter number 1 = "))
    b = float(input("Enter number 2 = "))
    t = a%b
    print("The modulas of",a, "and" ,b, "is" ,t)
elif x == 6:
    print("SQUARE")
    print("------")
    a = float(input("Enter number = "))
    h = a*a
    print("The square of", a, "is", h)
elif x == 7:
    import math


    def log_calculator():
        print("Logarithm Calculator")
        print("--------------------")

        base = float(input("Enter the base (a positive number greater than 0): "))
        if base <= 0:
            print("Error: Base must be a positive number greater than 0.")
            return

        num = float(input("Enter the number (a positive number greater than 0): "))
        if num <= 0:
            print("Error: Number must be a positive number greater than 0.")
            return

        result = math.log(num, base)
        print(f"The logarithm of {num} with base {base} is: {result:.4f}")


    if __name__ == "__main__":
        log_calculator()
elif x == 8:
    import math


    def natural_exponent_calculator():
        print("Natural Exponent Calculator")
        print("---------------------------")

        x = float(input("Enter the value of x: "))

        result = math.exp(x)
        print(f"The natural exponent of {x} is: {result:.4f}")


    if __name__ == "__main__":
        natural_exponent_calculator()
elif x == 9:
    import math


    def trigonometric_calculator():
        print("Trigonometric Calculator")
        print("------------------------")

        angle_degrees = float(input("Enter the angle in degrees: "))
        angle_radians = math.radians(angle_degrees)  # Convert degrees to radians

        sin_value = math.sin(angle_radians)
        cos_value = math.cos(angle_radians)
        tan_value = math.tan(angle_radians)

        print(f"Sine of {angle_degrees} degrees is: {sin_value:.4f}")
        print(f"Cosine of {angle_degrees} degrees is: {cos_value:.4f}")
        print(f"Tangent of {angle_degrees} degrees is: {tan_value:.4f}")


    if __name__ == "__main__":
        trigonometric_calculator()
elif x == 10:
    print("FACTORIAL")
    print("---------")


    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    if __name__ == "__main__":
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Error: Please enter a non-negative integer.")
        else:
            result = factorial(num)
            print(f"The factorial of {num} is: {result}")
elif x == 11:
    print("AREA OF CIRCLE")
    print("--------------")
    import math

    def circle_area(radius):
        return math.pi * radius ** 2


    if __name__ == "__main__":
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius < 0:
                print("Error: Radius cannot be negative.")
            else:
                area = circle_area(radius)
                print(f"The area of the circle with radius {radius} is: {area:.4f}")
        except ValueError:
            print("Error: Please enter a valid number for the radius.")
elif x == 12:
    print("AREA OF SQUARE")
    print("--------------")


    def square_area(side_length):
        return side_length * side_length


    # Example usage:
    side_length = float(input("Enter the side of square: "))
    area = square_area(side_length)
    print("The area of the square with side length", side_length, "is", area)

else:
    print("Enter a valid option")