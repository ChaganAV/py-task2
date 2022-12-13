num = int(input("Введите трехзначное число: "))
sum = 0
rasr = 100
if 99 < num < 1000:
    while num > 0:
        sum+=num//rasr
        num = num%rasr
        rasr = rasr//10
else:
    print("Вы ввели неверное число :(")
print(sum)