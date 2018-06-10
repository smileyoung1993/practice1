##q2

num = input("수를 입력하세요:")

try:
    num = int(num)

    if isinstance(num,int):
        if num % 2 == 0:
            print("짝수")
        else:
            print("홀수")
except ValueError:
    print("정수가 아닙니다.")
    