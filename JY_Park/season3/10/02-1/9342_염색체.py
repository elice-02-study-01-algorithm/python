# 방법1
# 정규표현 패턴 오브젝트의 메소드로 실행
# re.compile()를 사용하면, 정규표현 패턴 문자열을 컴파일하여 정규표현 패턴 오브젝트를 작성할 수 있다.

'''
- 문자열의 앞 부분이 매치되는가를 체크, 추출 match()
- 선두에 한해서 매치하는지를 체크, 추출 search()
- 문자열 전부가 매치되는가를 체크 fullmatch()
- 매치된 부분 모두 리스트로 취득 findall()
- 매치된 부분 모두 이터레이터(iterator)로 취득 finditer()
- 매치된 부분을 치환 sub() subn()
- 정규표현 패턴으로 문자열을 분할 spilt()

^는 문자열의 처음을 의미하고, $는 문자열의 마지막을 의미한다.
'''
'''
+는 최소 1번 이상 반복될 때 사용한다. 
- match
정규식에 부합되므로 match 객체를 돌려준다.
부합되지 않으므로 None을 돌려준다.
'''

import re

# [A-F]{0,1}으로 표현가능 
t = int(input())
p = re.compile('^[A-F]?A+F+C+[A-F]?$')

for _ in range(t):
    word = input()
    m = p.match(word)
    if m:
        print('Infected!')
    else:
        print('Good')