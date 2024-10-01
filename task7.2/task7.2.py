def check_rule(string) -> bool:
    have3 = False
    have2 = False
    have1_1 = False
    have1_2 = False
    if(string.count(str(9)) > 0): return False
    for i in range(1,9):
        if(string.count(str(i)) == 3 and not(have3)):
            have3 = True
        elif(string.count(str(i)) == 3 and have3):
            return False
        elif(string.count(str(i)) == 2 and not(have2)):
            have2 = True
        elif(string.count(str(i)) == 2 and have2):
            return False
        elif(string.count(str(i)) == 1 and (not(have1_1) or not(have1_2))):
            if(have1_1):
                have1_2 = True
            else:
                have1_1 = True
        elif(string.count(str(i)) == 1 and (have1_1 and have1_2)):
            return  False
    return have3 and have2 and have1_2 and have1_1


#  В выборке невозможны симметричные числа
with open("task7.2.txt", "w") as file:
    cnt = 0
    for i in range(1112234,9998876):
        string = str(i)
        if (check_rule(string)):
                file.write(string + "\n")
                cnt += 1
    file.write(str(cnt))