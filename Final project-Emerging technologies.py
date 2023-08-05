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
print("Press 12 for pound to kilogram")
print("Press 13 for centimeter to inches")
print("Press 14 for celsius to fahrenheit")
print("Press 15 for square feet to acres")
print("Press 16 for sugar to calories")
print("Press 17 for kilometers to miles")
print("Press 18 for square root")

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
    print("POUND TO KILOGRAM ")
    print("-----------------")


    def pounds_to_kilograms(pounds):
        kilograms = pounds * 0.45359237
        return kilograms


    pounds = float(input("Enter weight in pounds: "))
    kilograms = pounds_to_kilograms(pounds)
    print(f"{pounds} pounds is approximately {kilograms:.2f} kilograms")

elif x == 13:
    print("CENTIMETER TO INCHES")
    print("--------------------")


    def cm_to_inches(cm):
        inches = cm / 2.54
        return inches


    cm = float(input("Enter length in centimeters: "))
    inches = cm_to_inches(cm)
    print(f"{cm} centimeters is approximately {inches:.2f} inches")

elif x == 14:
    print("CELSIUS TO FAHRENHIET")
    print("--------------------")


    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit


    # Example usage:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius is approximately {fahrenheit:.2f} degrees Fahrenheit")
elif x == 15:
    print("SQUARE FEET TO ACRES")
    print("--------------------")


    def square_feet_to_acres(square_feet):
        acres = square_feet / 43560
        return acres

    square_feet = float(input("Enter area in square feet: "))
    acres = square_feet_to_acres(square_feet)
    print(f"{square_feet} square feet is approximately {acres:.4f} acres")

elif x == 16:
    print("SUGAR TO CALORIES")
    print("--------------------")


    def sugar_to_calories(sugar_grams):
        calories = sugar_grams * 4
        return calories

    sugar_grams = float(input("Enter the amount of sugar in grams: "))
    calories = sugar_to_calories(sugar_grams)
    print(f"{sugar_grams} grams of sugar is approximately {calories:.2f} calories")

elif x == 17:
    print("KILOMETERS TO MILES")
    print("--------------------")


    def kilometers_to_miles(kilometers):
        miles = kilometers * 0.621371
        return miles


    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers_to_miles(kilometers)
    print(f"{kilometers} kilometers is approximately {miles:.2f} miles")

elif x == 18:
    print("SQUARE ROOT")
    print("-----------")
    number = float(input("Enter a number: "))
    square_root = number ** 0.5
    print(f"The square root of {number} is {square_root:.2f}")

else:
    print("Enter a valid option")
