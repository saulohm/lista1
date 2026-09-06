def converter_celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperature_celsius = float(input("Digite a temperatura em Celsius: "))

print(f"A temperatura em Fahrenheit é: {converter_celsius_para_fahrenheit(temperature_celsius)}")