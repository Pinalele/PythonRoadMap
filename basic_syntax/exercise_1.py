name = input('Introduce your name:')
print(name)
temp = float(input('Introduce temperature in celsius:'))
print(temp)



fahrenheit = temp * 1.8 + 32
kelvin = temp + 273.15

print(f'Hello ' + name + '! ' + str(temp) +' ºC = ' + str(fahrenheit) +' ºF ' + '= ' + str(kelvin) + ' ºK')

if temp < 0:
    print("Ice")
elif 0 >= temp <= 15:
    print("Freeze")
elif 16 >= temp <= 25:
    print("cool")
else:
    print("Hot")