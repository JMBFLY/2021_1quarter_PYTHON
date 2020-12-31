def sum(a, b):
    return a+b


def HI():
    return 'hi'


def sumMany(*args):
    a = 1
    b = 10
    d = 0
    for c in args:
        d = d + c
    print("%d부터 %d까지의 합은 %d입니다." % (a, b, d))


a = 1
b = 2
c = sum(a, b)
print(c)

d = HI()
print(d)

many = sumMany(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(many)

#insert = input("입력해주세여 : ")
# print(insert)

print("뮤직이즈마이라이프")
print("뮤직 이즈 마이 라이프")
print("뮤직""이즈""마이""라이프")
print("뮤직 ""이즈 ""마이 ""라이프 ")
print("뮤직"+"이즈"+"마이"+"라이프")
print("뮤직", "이즈", "마이", "라이프")
