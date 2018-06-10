##q5

s = '''We encourage everyone to contribute to Python If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process.'''

s = s.strip().upper().replace('.','').replace(',','')
# 띄어쓰기를 제외한 앞뒤공백제거,대문자로 변환,'.',',' 를 제거

vocas = set(s.split(' ')) # 띄어쓰기를 기준으로 단어를 나누고 리스트로 변환후, 중복제거를 위해 set으로 만든다.
# 단어출력
print("실행 결과:")
for voca in vocas:
    print(voca)

vocas = list(vocas) # 인덱스로 해당 문자열을 비교하기 위해 중복제거된 set을 다시 list로 저장
print("\n")
# 해당문자열의 빈도수 체크하기.
print("각 단어의 빈도수 체크하기")
vocas_lst = s.split(' ') # 중복제거가 안되는 리스트로 저장
cnt= [ 0 for _ in range(len(vocas))] ## 빈도수 세는 리스트

for i in range(len(vocas)):
    for word in vocas_lst:
        if word == vocas[i]:
            cnt[i] += 1

    print(vocas[i],":",cnt[i],"개")
