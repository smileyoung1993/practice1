#q9

#문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

#입력> Java Programming!
#결과> !gnimmargorP avaJ

s = input("입력>")
s = ''.join(reversed(s))
#join은 문자열 만들때 쓰는데 s문자열을 리버스해서 다시 조인으로 문자열 만드는 듯
print("출력>",s)

