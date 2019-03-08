color = ["red", "blue", "green"]
color.append("white") # color에 white 추가
color.extend(["black", "puple"]) # color에 새로운 리스트 추가
color.insert(0,"orange") # 0번째 인덱스에 orange 추가
print(color)
color.remove("white") # 리스트에서 white삭제
del color[0] # 0번째 주소 리스트 객체 삭제
print(color)
