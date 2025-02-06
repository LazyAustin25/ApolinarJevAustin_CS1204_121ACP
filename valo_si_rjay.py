from collections import Counter
rol = str(input("Enter the roles: "))
map = str(input("Enter map: "))
def count_specific_characters(s):
    D_count = s.count('D')
    S_count = s.count('S')
    C_count = s.count('C')
    I_count = s.count('I')
    return D_count, S_count, C_count, I_count

string = rol
D_count, S_count, C_count, I_count = count_specific_characters(string)
print_counts(D_count, S_count, C_count, I_count)
