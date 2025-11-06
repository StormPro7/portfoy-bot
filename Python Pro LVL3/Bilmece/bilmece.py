# 1'den 100'e kadar cift olmayan 3'un katlari

for i in range(1,101):
    if i % 3 == 0 and not i % 2 == 0:
        print(i)