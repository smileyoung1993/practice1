#q8
#키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
total = 0
avg = 0.0
num_lst = []
# 5번 정수를 입력해준다.
for i in range(5):
    num = input()
    num_lst.append(num)
# 리스트에 저장된 숫자 문자열을 int형으로 total에 더해준다
for x in num_lst:
    total += int(x)
# 평균구하기
avg = total / len(num_lst)

print("평균: ",avg)
