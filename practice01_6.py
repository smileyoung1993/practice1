##q6

'''
주어진 리스트에서 3의 배수의 개수=> 6
주어진 리스트에서 3의 배수의 합=> 150
'''

cnt = 0
sum = 0

num = input()
num_lst = ''.join(num).split()
thr_lst = []

for x in num_lst:
    if int(x) % 3 == 0:
        thr_lst.append(x)
        cnt += 1

for y in thr_lst:
    sum += int(y)

print("주어진 리스트에서 3 의 배수의 개수=>",cnt)
print("주어진 리스트에서 3 의 배수의 합=>",sum)

