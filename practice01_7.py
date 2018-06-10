#q7

money = input("돈을 입력하세요: ")
my_money = [50000,10000,5000,1000,500,100,50,10,5,1]
cnt=[0 for _ in range(10)]#돈 개수
remain = [0 for _ in range(10)]#나머지돈

# remain list의 첫번째 원소를 int로 잡으면
# for loof안의 두번재 원소부터는 int
for i in range(8):
    if i == 0:
        cnt[i] = int(int(money) / int(my_money[i]))
        remain[i] = int(int(money) % int(my_money[i]))
    remain[i+1]= remain[i] % int(my_money[i+1])

for i in range(9):
    cnt[i+1] = int(remain[i] / int(my_money[i+1]))
    print(my_money[i],"원 :",cnt[i])
    if i == 8: # 1원까지 출력을 위해
        print(my_money[i+1],"원 :",cnt[i+1])