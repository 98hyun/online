import re

p=re.compile("ca.e")
# .은 하나의 문자를 의미 > cafe, cave, cate, .. | (x) cagge 
# ^ 문자열의 시작 : (^de)  > desc desk  | afde(x)
# $ 문자열의 끝 : (se$) > case ssse agafse | segg (x) 

m=p.match('case') # 매칭이 안되면 error

def print_match(m):
    if m:
        print(m.group()) # 이걸로 시작하면
        print(m.string) # 받은 문자열
        print(m.start()) # 일치하는 문자열의 시작 index
        print(m.end()) # 일치하는 문자열의 끝 index 
        print(m.span()) # 일치하는 문자열의 시작과 끝 index
    else:
        print('none')
# print_match(m)

m=p.search('good care') # 문자열에 포함되나?
# print(m.group())

lst=p.findall('careless good cafe')

print(lst)

# 1. p=re.compile(원하는형태) 컴파일 init
# 2. m=p.match(비교하고 싶은 문자) 처음부터 찾는것.
# 3. m=p.search(비교할 문자) 그안에서 찾는것.
# 4. m=p.findall(비교할 문자) list 형태로 반환.