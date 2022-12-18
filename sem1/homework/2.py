# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

predicate = 0, 1
for x in predicate:
    for y in predicate:
        for z in predicate:
            print(not (x or y or z) == (not x) and (not y) and (not z))