fruits = {
    'summerfruits':{
        '사과' : 'apple',
        '수박' : 'watermelon',
        '자두' : 'plum'
    },
    'spiringfruits': {
        '딸기' : 'strawberry',
        '오렌지': 'orange',
        '체리' : 'cherry'
    }
    }
# print(f'fruits: {fruits}')
# ======>변수를 포함한 딕셔너리 값 전체 출력
# print(fruits)
# =======>변수를 제외한 딕셔너리의 전체값 출력

# print(fruits.keys())
# print(fruits['spiringfruits']['딸기'])
# =======>특정 값 출력-springfruit 딕셔너리 안 딸기(Strawberry)의 벨류값
# print(fruits['spiringfruit'].keys())
# =======>springfruit의 키에 해당하는 사과, 수박, 자두를 출력
# print(fruits['spiringfruit'].values())
# =======>springfruit의 벨류에 해당하는 strawberry, watermelon, plum을 출력
# print(fruits['spiringfruit'].items())
# =======>springfruit의 아이템값에 해당하는 (딸기, strawberry)의 값을 가져온다.
# print(type(fruits) =======> 딕셔너리의 타입은 dictionary이다. 


#조회
# print(f"apple : {fruits['summerfruits']['사과']}")
#특정값 조회 
# print(f'type(fruit): {type(fruits["summerfruit"])}')

#추가

fruits['summerfruits']['포도'] = 'grape'
print(f'summerfruits: {fruits['summerfruits']}')
'''
복합 딕셔너리에서 정보 추가하는 방법
토이프로젝트에서의 memberAccountDb[uId]['uPw'] 라는 코드와 구성이 같다.
가장 상부에 있는 딕셔너리의 이름만 앞에 쓸 수 있는 듯 하다.
가장 앞에있는 딕셔너리의 이름 + 추가하고자하는 딕셔너리의 이름 + 추가하고자 하는 정보의 키와 벨류값
'''

#수정
fruits['summerfruits']['수박'] = 