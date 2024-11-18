"""
1.1 Feladat
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, 
és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. 
A vizsgálat eredményéről tájékoztassa a program a felhasználót, 
és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!
"""

# Ha a szín nem szerepel a listában, egészítsd ki a listát a színnel, majd printeld is ki az új listát!

szinek = ['piros','kék', 'zöld', 'sárga', 'lila', 'fekete', 'fehér']

megadott_szin = input('Adj meg egy színt: ')

# if megadott_szin in szinek:
#     print(f"A megadott szín, {megadott_szin} szerepel a listában")
# else:
#     print(f"A megadott szín, {megadott_szin} NEM szerepel a listában")
#     szinek.append(megadott_szin)
#     print(f"Az új lista kiegészítve: {szinek}")

# Töröld a megadott színt a listából:
if megadott_szin in szinek:
    szinek.remove(megadott_szin)
else:
    print(f'Nincs a listában ilyen elem: {megadott_szin}')
print(szinek)