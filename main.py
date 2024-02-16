def hex_to_decimal(hex_value):
    try:
        decimal_value = int(hex_value, 16)
        return decimal_value
    except ValueError:
        return "Invalid hexadecimal value"

def hex_to_binary(hex_value):
    try:
        binary_value = bin(int(hex_value, 16))[2:]
        return binary_value
    except ValueError:
        return "Invalid hexadecimal value"

def main():
    hex_value = input("Enter a hexadecimal number: ")
    decimal_value = hex_to_decimal(hex_value)
    binary_value = hex_to_binary(hex_value)
    print(f"The decimal value of {hex_value} is {decimal_value}")
    print(f"The binary value of {hex_value} is {binary_value}")

if __name__ == "__main__":
    main()
