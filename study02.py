i = 10
j = 20

if i == 10:
    print("10이야")
elif i == 20:
    print("20이야")
else:
    print("10이 아니야")

if j == 10:
    print("맞아")
else:
    pass  # pass가 정말 아무것도 하고 싶지 않지만 넣어야할때만 쓸뿐 이것이 break랑은 다르다
    print("글쎄")
print('hi')

a = 0
while a < 11:
    print("메렁 ")
    a += 1

str = "신나는 여행"
for b in str:
    print(b)

for b in range(0, 10):
    print(str)

for c in range(0, 10):
    if c >= 5:
        break
    else:
        print(c)

for d in range(0, 10):
    if d % 2 == 0:
        continue
    else:
        print(d)
