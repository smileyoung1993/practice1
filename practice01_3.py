##q3

s = '/usr/local/bin/python'
# 문자열의 1번째 인덱스를 부터 시작, / 를 기준으로 나누고 , 를 삽입한 후(split은 리스트) 문자열로 만들다.
print(','.join(s[1:].split('/')))

# 오른쪽(/)을 기준으로 나눈다 rsplit , 나눈 뒤 문자열로 출력
print(','.join(s.rsplit('/', 1)))


