#q11

def sum_num(num):
    total = 0
    for i in range(num+1):
        total += i
    return total

num = input()
print(sum_num(int(num)))