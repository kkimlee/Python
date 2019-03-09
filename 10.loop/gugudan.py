print("구구단 몇단을 계산할까요?")
number = input()
print("구구단 " + number + "단을 계산합니다")
for i in range(1,10):
    result = int(number)*i
    print (number, "X", i, "=", result)
    # + 사용시 int값과 str값을 연산할수 없다는 오류가 나옴!
