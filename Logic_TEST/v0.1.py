import csv
import random

def read_data():
    f = open("Logic_TEST/MenuList.csv", "r")
    reader = csv.reader(f)
    result = []
    rows = list(reader)
    for i in range(2, len(rows)):
        result.append(rows[i])
    return result
        
def show_menu(menu):
    for i in range(len(menu)):
        for j in range(len(menu[i])):
            print(menu[i][j], end='\t|')
        print()

def input_filter(name, rule, isSplit=None,):
    if isSplit != None:
        data = input(f'{name} : ').split(isSplit)
    else:
        data = input(f'{name} : ')
    if type(data) == list:
        if len(data) > 1:
            print('중복선택됨')
        else:
            for i in range(len(rule)):
                if data[0] == rule[i]:
                    data[0] = i   
    else:
        for i in range(len(rule)):
            if data == rule[i]:
                data = i
    return data 

def set_value():
    people = int(input('몇명이서? (숫자만) : '))
    price = int(input('얼마정도? (숫자만) : '))
    space = input_filter('(상관없음/배달/홀)', ['상관없음','배달','홀'])
    spicy = input_filter('(순한맛/보통맛/매운맛)', ['순한맛','보통맛','매운맛'])
    salty = input_filter('건강식 (예/아니오)', ['예','아니오'])
    sweety = input_filter('달달한거 (예/아니오)', ['예','아니오'])
    country = input_filter('(상관없음/한식/중식/일식/양식) 공백기준 중복선택 가능', ['상관없음', '한식','중식','일식','양식'], ' ')
    rice = input_filter('(상관없음/밥/면)', ['상관없음', '밥','면'])
    food_type = input_filter('(상관없음/국물/볶음/찜/구이/다이어트) 공백기준 중복선택 가능', ['상관없음', '국물','볶음','찜','구이', '다이어트'], ' ')
    kcal = int(input('칼로리 제한(숫자만) : '))
    print(f'{people}, {price}, {space}, {spicy}, {salty}, {sweety}, {country}, {rice}, {food_type}, {kcal}')
    result = [None,people,price,space,spicy,salty,sweety,country,rice,food_type,kcal,None]
    return result

def filtering(rule, menu):
    result = []
    print('Filtering Started!')
    result = people_(rule[1],menu)    
    
def people_(rule, menu):
    result = []
    for i in range(len(menu)):
        if menu[i][1] == 0 or int(menu[i][1]) > rule:
            print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
            result.append(menu[i])
    return result
MenuList = read_data()
show_menu(MenuList)
#filter = set_value()
filter = [None,1,5000,0,0,1,0,2,2,0,1000,None]
filtering(filter, MenuList)