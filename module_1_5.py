#2#
immutable_var = "Мама", "Отец", "Брат", "Я"
print(immutable_var)
#3#
#immutable_var = "Мама", "Отец", "Брат", "Я"
#immutable_var [3] = ["Мария"]
#print(immutable_var)
#Этот код не сработает, так как он находится в кортеже, если надо поменять значение, то значение надо переименовать в список, и после уже вводить изменения#

immutable_var = ["Мама", "Отец", "Брат", "Я"]
immutable_var [3] = "Мария"
print(immutable_var)


#4#
mutable_list = ["Змеи","крокодил", "слон", "ящерица"]
print(mutable_list)
#вводим изменения в список#
mutable_list = ["Змеи","крокодил", "слон", "ящерица"]
mutable_list [2] = "черепаха"
print(mutable_list)

#Просто пыталась разобраться, как можно убрать слово из списка#
immutable_var = (["мама", "папа"], "брат")
immutable_var [0][0] = "родители"
immutable_var [0][1] = ""
print(immutable_var)