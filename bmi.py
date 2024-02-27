def main():
    measure_sys = int(
        input(
            """Select Measuring System:
                    0 -> Metric System
                    1 -> Imperial System
                    input = """
        )
    )

    if measure_sys == 0:
        height = int(input("Height (cm)= ")) / 100
        weight = int(input("Weight (Kg)= "))
        print("BMI = ", bmi_calculator(measure_sys, weight, height))

    elif measure_sys == 1:
        height = int(input("Height (inches)= "))
        weight = int(input("Weight (punds)= "))
        print("BMI = ", bmi_calculator(measure_sys, weight, height))

    else:
        print("Invalid Input")
        return

    print(
        """Comparison Table:
<18.5   \tUnder Weight
18.5-24.9 \tNormal
25-29.9 \tOver Weight
30-34.9 \tObesity(Class 1)
35-39.9 \tObesity(Class 2)
>40     \tExtreme Obesity"""
    )

    return


def bmi_calculator(measure_sys, weight, height):
    bmi = weight / (height * height)

    if measure_sys == 1:
        bmi = bmi * 703

    return round(bmi, 2)


main()