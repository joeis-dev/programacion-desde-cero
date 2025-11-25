fulanito_car_gas = 18
manganito_car_gas = 25

# Fulanito on his way to his work
fulanito_car_gas -= 12

# Manganito on his way to his college
manganito_car_gas -= 7

#1
print(f"Terminaron con la misma cantidad de gasolina?... {fulanito_car_gas == manganito_car_gas}")

#2
print(f"El auto de Fulanito tiene mas gasolina que el de Manganito?... {fulanito_car_gas >= manganito_car_gas}")

#3
print(f"El auto de Manganito tenia menos gasolina que el de Fulanito antes de iniciar su recorrido?... {manganito_car_gas <= manganito_car_gas}")

#4
print(f"Fulanito debe cargar gasolina?... {fulanito_car_gas <= 10}")

#5
print(f"Manganito debe cargar gasolina?... {manganito_car_gas <= 15}")