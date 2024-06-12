#4장 문제 1
str = '20201231Thursday'
year = str[0:4]
print(year)
mmdd = str[4:8]
print(mmdd)
day = str[8:]
print(day)

#4장 문제 5
for i in range(6):
    for j in range(i):
        print("*", end="")
    print()