val = int(input("Please enter a temperature: "))
unit = input("Please enter a temperature unit: ").upper()
conv = input("Conversion to: ").upper()

if conv == "C":
    if unit == "F":
        print(f"{val - 32 * 5 / 9 :.2f}")

    else:
        print(f"{val - 272.15 :.2f}")

if conv == "F":
    if unit == "C":
        print(f"{val * 9 / 5 + 32 :.2f}")

    else:
        print(f"{1.8 * (val -273.15) + 32 :.2f}")

if conv == "K":
    if unit == "C":
        print(f"{val + 273.15 :.2f}")

    else:
        print(f"{(val + 459.67) * 5 / 9 :.2f}")