#q10

menu = input("선택 :")

# dict = {key:value}
menu_dit = {'오뎅':300,'순대':400,'만두':500}
# menu에 따라서 메뉴 dict에서 가격값이 나온다.

print('{0}:{1}'.format(menu, menu_dit[menu]),"원", end=" ")
