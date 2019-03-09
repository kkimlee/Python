print("변환할 10진수 입력")

decimal = int(input())
result = ""

while (decimal > 0):
    remainder = decimal % 2 # 10진수를 2로 나눈 나머지
    decimal = decimal // 2 # 10진수를 2로 나눈 몫 int형
    result = str(remainder) + result
print (result)
