str = "I love you"
reverse = ""
for char in str:
    # str의 첫번째 인덱스 부터 char에 대입
    reverse = char + reverse
    # reverse의 첫번째 인덱스값이 밀려나면서 계속 대입됨
    # "I" -> " I" -> "l I" -> "ol I".....
print (reverse)
