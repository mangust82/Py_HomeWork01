# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех  значений предикат.

X_list = [0, 1]
Y_list = [0, 1]
Z_list = [0, 1]
for x in X_list:
    for y in Y_list:
        for z in Z_list:
            print(f'not({x} or {y} or {z}) == (not({x}) and not({y}) and not({z}))')
            print(not(x or y or z) == (not(x) and not(y) and not(z)))
