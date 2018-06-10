#q 13
'''
a. 입력 받은 숫자가 홀수인 경우에는, 0 부터 입력 값까지 홀수의 합을 출력합니다.
- 예제 : 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 )
b. 입력 받은 숫자가 짝수인 경우에는, 0 부터 입력 값까지 짝수의 합을 출력합니다.
    - 예제 : 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )
'''

def sum_odd(num):
    i=1
    odd_sum = 0
    for i in range(num+1):
        if(i % 2 != 0):
            odd_sum += i
    return odd_sum

def sum_even(num):
    i=1
    even_sum = 0
    for i in range(num+1):
        if(i % 2 == 0):
            even_sum += i
    return even_sum

num = input("숫자를 입력하세요: ")

if int(num) %2 != 0:
    print("결과 값  : ",sum_odd(int(num)))
else:
    print("결과 값  : ",sum_even(int(num)))

