# int를 float변환
int_a = 10
print(int_a)

int_a = float(10)
print(int_a)

int_b = 3
print (int_a / int_b)
# float를 int변환
float_a = 10.7
float_b = 10.3

float_a = int(float_a)
float_b = int(float_b)
print(float_a+float_b)

print(float_a)
print(float_b)

# 숫자와 문자열 변환
char_a = '76.3'
float_c = float(char_a)

print(char_a) # char형 문자열
print(float_c) # float형 숫자

# print(char_a+float_c)
# float형과 char형 덧셈 불가 에러 발생

char_a = float(char_a)
float_c = char_a
print(char_a + float_c)

char_a = str(char_a)
float_c = str(float_c)
print(char_a + float_c)
