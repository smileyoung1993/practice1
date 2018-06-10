# q 14
'''
숨겨진 카드의 수를 맞추는 게임입니다. 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는 게임입니다.
아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면 "더 높게",다시 75이라고 입력하면
"더 낮게" 라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다. 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.
'''
from random import randint

loof_out = 0

while True:
    print("수를 결정하였습니다. 맞추어 보세요")
    print("1-100")

    card_num = randint(1,100)
    for i in range(101):
        print(i+1,"번째 시도",'>>')
        say_num = input()
        '''
        try :
            if isinstance(say_num,int) == False:
                 print("숫자를 입력해주세요")
        except ValueError:
            continue
        '''
        if int(say_num) < card_num:
            print("더 높게")
            continue
        elif int(say_num) > card_num:
            print("더 낮게")
            continue
        elif int(say_num) == card_num:
            print("맞았습니다.")
            select = input("다시 하시겠습니까(y/n)")
            if select == 'n':
                loof_out = 1 # while루프 탈출변수
                break
            elif select == 'y':
                break

    if loof_out == 1: #루프 탈출변수가 1이면 while루프 탈출
        break

