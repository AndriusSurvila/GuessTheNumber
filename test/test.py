# I
print("---NOT---") # инверсия (отрицание) ¬A --- Ā => !A 
print(not (2 > 1)) # not true => false
print(not (2 < 1)) # not false => true

# II
print("---AND---") # конъюнкция (умножение) A ∧ B --- A * B --- AB => A & B
print((1 < 2) and (2 < 1)) # true and false => false
print((1 > 2) and (1 < 2)) # false and true => false
print((1 < 2) and (2 > 1)) # true and true => true
print((1 > 2) and (2 < 1)) # false and false => false

# III
print("---OR---") # дизъюнкция (сложение) A ∨ B --- A + B --- AB => A | B
print((1 < 2) or (2 < 1)) # true or false => true
print((1 > 2) or (2 > 1)) # false or true => true
print((1 < 2) or (2 > 1)) # true or true => true
print((1 > 2) or (2 < 1)) # false or false => false


print("--------------")
print(not (2 > 1) or (2 < 1) and (1 < 2)) # false or false and true => false