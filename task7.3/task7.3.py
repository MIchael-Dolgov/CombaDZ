def check_rule(string) -> bool:
    if string.count(str(2)) == 3 and issymmetric(string):
        return True
    else:
        return False

def issymmetric(string) -> bool:
    for i in range()

#  В выборке невозможны симметричные числа
with open("task7.3.txt", "w") as file:
    cnt = 0
    for i in range(111222,888222):
        string = str(i)
        if (check_rule(string)):
                file.write(string + "\n")
                cnt += 1
    file.write(str(cnt))