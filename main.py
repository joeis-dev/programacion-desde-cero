score_fulanito = 90
score_manganito = 60

# equals
isExcellent = score_fulanito == 100
print(f"Fulanito obtuvo una calificacion de excelencia?... {isExcellent}!")

# not equals
print(f"Fulanito y Manganito obtuvieron la misma calificacion?... {score_fulanito != score_manganito}")

## greater than
print(f"Manganito obtuvo una calificacion mayor que Fulanito?... {score_manganito > score_fulanito}")

# less than
print(f"Fulanito obtuvo una calificacion menor que Manganito?... {score_fulanito < score_manganito}")

# greater than or equal to
print(f"Manganito aprobo la materia?... {score_manganito >= 60}")

# less than or equal to
print(f"Manganito necesita cursos de regularizacion?... {score_manganito <= 60}")
