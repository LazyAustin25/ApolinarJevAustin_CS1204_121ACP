from collections import Counter

rol = input("Enter the roles: ")
map = input("Enter map: ")

def count_specific_characters(s):
    D_count = s.count('D')
    S_count = s.count('S')
    C_count = s.count('C')
    I_count = s.count('I')
    return D_count, S_count, C_count, I_count

D_count, S_count, C_count, I_count = count_specific_characters(rol)
rs = D_count + S_count + C_count + I_count

if map == "Haven":
    rc = (I_count // 2)
elif map == "Ascent":
    rc = (S_count // 2)
elif map == "Bind":
    rc = (C_count // 2)
else:
    rc = rs // 5

if ((rs // 5) - rc) <= 0:
    res = rs
else:
    res = rc

print(f"You can have {res} team/s for {map}")
