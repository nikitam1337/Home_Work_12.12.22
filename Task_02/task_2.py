# Напишите программу для.
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print(f'x y z проверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == ((not x) and (not y) and (not z)):
                print (f'{x} {y} {z} true')

