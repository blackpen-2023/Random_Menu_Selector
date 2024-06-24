import csv
import random

def read_data():
    f = open("Logic_TEST/MenuList.csv", "r")
    reader = csv.reader(f)
    result = []
    for row in reader:
        result.append(row)
    return result
        
def show_menu(menu):
    print('( 메뉴	인원	가격	배달/홀	맵기	짜기	달기	한/중/일/양	밥/면	국물/볶음/찜/구이/다이어트	칼로리	참고처	곁들임 )')
    for i in range(1, len(menu)):
        for j in range(0,len(menu[i])):
            print(menu[i][j], end='    \t')
        print()        

MenuList = read_data()
show_menu(MenuList)

people = int(input('몇명이서? (숫자만) : '))
price = int(input('얼마정도? (숫자만) : '))
space = input('(배달/집/상관없음) : ')
if space == '상관없음':
    space = 0
elif space == '배달':
    space = 1
elif space == '홀':
    space = 2  
else:
    space = 'Error'  
spicy = input('(순한맛/보통맛/매운맛) : ')
if spicy == '순한맛':
    spicy = 0
elif spicy == '보통맛':
    spicy = 3
elif spicy == '매운맛':
    spicy = 4
else:
    spicy = 'Error' 
salty = input('건강식 (예/아니오) : ')
if salty == '예':
    salty = 0
elif salty == '아니오':
    salty = 1
else:
    salty = 'Error' 
sweety = input('달달한 거 (예/아니오) : ')
if sweety == '예':
    sweety = 1
elif sweety == '아니오':
    sweety = 0
else:
    sweety = 'Error' 
country = input('(한식/중식/일식/양식) 공백기준 중복선택 가능 : ').split(' ')
if type(country) == list and len(country) > 1:
    print('국가 중복선택됨')
elif country[0] == '한식':
    country[0] = 1
elif country[0] == '중식':
    country[0] = 2
elif country[0] == '일식':
    country[0] = 3
elif country[0] == '양식':
    country[0] = 4
else:
    country = 'Error' 
rice = input('밥/면 : ')
if rice == '밥':
    rice = 0
elif rice == '면':
    rice = 1
else:
    rice = 'Error' 
food_type = input('(국물/볶음/찜/구이/다이어트) 공백기준 중복선택 가능 : ').split(' ')
if type(food_type) == list and len(food_type) > 1:
    print('타입 중복선택됨')
elif food_type[0] == '국물':
    food_type[0] = 1
elif food_type[0] == '볶음':
    food_type[0] = 2
elif food_type[0] == '찜':
    food_type[0] = 3
elif food_type[0] == '구이':
    food_type[0] = 4
elif food_type[0] == '다이어트':
    food_type[0] = 5
else:
    food_type = 'Error' 
kcal = int(input('칼로리 제한(숫자만) : '))

print(f'{people}, {price}, {space}, {spicy}, {salty}, {sweety}, {country}, {rice}, {food_type}, {kcal}')

