# q12

cnt = 1;
num_lst = []
print('369게임 시작!!')

for cnt in range(100):
    num_lst.append(str(cnt))

## num_lst에 들어간 원소가 str 타입인지 점검
#print(type(num_lst[0]))

# 리스트의 원소를 꺼내오면서 문자 3,6,9를 리스트의 문자가 포함할 때 출력
for num in num_lst:
    if '3' in num or '6' in num or '9' in num:
        print(num,'짝','\n')

