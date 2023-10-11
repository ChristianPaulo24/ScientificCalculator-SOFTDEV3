import math
import statistics


def scientific_calculator():
    while True:
        print("Scientific Calculator")
        print("Operations: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Trigonometric Functions")
        print("8. Logarithmic Functions")
        print("9. Advanced Operations")
        print("10. Statistical Operations")
        print("0. Quit")

        choice = int(input("Enter Operation Choice: "))

        if choice == 0:
            print("Exiting the calculator.")
            break

        if choice == 1:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 + num2
            return result

        elif choice == 2:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 - num2
            return result

        elif choice == 3:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 * num2
            return result

        elif choice == 4:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                return result

        elif choice == 5:
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = math.pow(base, exponent)
            return result

        elif choice == 6:
            num = float(input("Enter a number: "))
            if num < 0:
                print("Cannot take the square root of a negative number.")
            else:
                result = math.sqrt(num)
                return result

        elif choice == 7:
            print("Trigonometric Functions:")
            print("1. Sine")
            print("2. Cosine")
            print("3. Tangent")

            trig_choice = int(input("Enter Trigonometric Function Choice: "))
            angle = float(input("Enter the angle in degrees: "))

            if trig_choice == 1:
                result = math.sin(math.radians(angle))
                return result
            elif trig_choice == 2:
                result = math.cos(math.radians(angle))
                return result
            elif trig_choice == 3:
                result = math.tan(math.radians(angle))
                return result
            else:
                print("Invalid trigonometric function choice.")

        elif choice == 8:
            print("Logarithmic Functions:")
            print("1. Natural Logarithm (base e)")
            print("2. Logarithm with base 10")

            log_choice = int(input("Enter Logarithmic Function Choice: "))
            num = float(input("Enter a number: "))

            if log_choice == 1:
                result = math.log(num)
                return result
            elif log_choice == 2:
                result = math.log10(num)
                return result
            else:
                print("Invalid logarithmic function choice.")

        elif choice == 9:
            print("Advanced Operations:")
            print("1. Factorial")
            print("2. Exponentiation (e^x)")
            print("3. Degrees to Radians Conversion")
            print("4. Radians to Degrees Conversion")
            print("5. Complex Number Operations")

            advanced_choice = int(input("Enter Advanced Operation Choice: "))

            if advanced_choice == 1:
                num = int(input("Enter a non-negative integer: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    result = math.factorial(num)
                    return result
            elif advanced_choice == 2:
                x = float(input("Enter the value for exponentiation (e^x): "))
                result = math.exp(x)
                return result
            elif advanced_choice == 3:
                degree_value = float(input("Enter degrees: "))
                radians = math.radians(degree_value)
                return radians
            elif advanced_choice == 4:
                radian_value = float(input("Enter radians: "))
                degrees = math.degrees(radian_value)
                return degrees
            elif advanced_choice == 5:
                real1 = float(input("Enter the real part of the first complex number: "))
                imag1 = float(input("Enter the imaginary part of the first complex number: "))
                real2 = float(input("Enter the real part of the second complex number: "))
                imag2 = float(input("Enter the imaginary part of the second complex number: "))
                complex_num1 = complex(real1, imag1)
                complex_num2 = complex(real2, imag2)

                print("Complex Number Operations:")
                print("1. Complex Addition")
                print("2. Complex Subtraction")
                print("3. Complex Multiplication")
                print("4. Complex Division")

                complex_operation = int(input("Enter Complex Operation Choice: "))

                if complex_operation == 1:
                    result = complex_num1 + complex_num2
                    return result
                elif complex_operation == 2:
                    result = complex_num1 - complex_num2
                    return result
                elif complex_operation == 3:
                    result = complex_num1 * complex_num2
                    return result
                elif complex_operation == 4:
                    if complex_num2 == 0:
                        print("Cannot divide by zero (complex division).")
                    else:
                        result = complex_num1 / complex_num2
                        return result
                else:
                    print("Invalid complex number operation choice.")

        elif choice == 10:
            print("Statistical Operations:")
            print("1. Mean")
            print("2. Median")
            print("3. Mode")
            print("4. Variance")
            print("5. Standard Deviation")

            stat_choice = int(input("Enter Statistical Operation Choice: "))

            data = input("Enter a list of numbers separated by spaces: ").split()
            data = [float(x) for x in data]

            if stat_choice == 1:
                result = statistics.mean(data)
                return result
            elif stat_choice == 2:
                result = statistics.median(data)
                return result
            elif stat_choice == 3:
                result = statistics.mode(data)
                return result
            elif stat_choice == 4:
                result = statistics.variance(data)
                return result
            elif stat_choice == 5:
                result = statistics.stdev(data)
                return result
            else:
                print("Invalid statistical operation choice.")

        else:
            print("Invalid choice. Please select a valid operation.")
            return None


# Call the scientific_calculator function and get the result
while True:
    result = scientific_calculator()
    if result is not None:
        print("Result:", result)
