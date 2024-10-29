#x1+x2+x3 = 15

buketik = [0, 0, 0]
cnt = 0
for i in range(0, 16):
    for j in range(0, 16):
        for k in range(0, 16):
            buketik = [i, j, k]
            if (sum(buketik) == 15 and i%2 == 0 and j%2!=0 and k%2==0):
                cnt+=1
                print(buketik)

print(cnt)
