items = ['1','2','3','4','5','6','7','8']

#time difficulty: O(n^5)
with open('combs7.1.txt', 'w') as file:
    cnt = 0
    for item1 in items:
        for item2 in [it for it in items if it != item1]:
            for item3 in [it for it in items if it != item1 and it != item2]:
                for item4 in [it for it in items if it!= item1 and it!= item2 and it!= item3]:
                    for item5 in [it for it in items if it!= item1 and it!= item2 and it!= item3 and it!= item4]:
                        file.write(item1+item2+item3+item4+item5+"\n")
                        cnt+=1
    file.write("\ncnt: " + str(cnt))
# A^5_8 = 8!/(8-5)! = 8!/3! = 6720
