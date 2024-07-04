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

def default_setting():
    spicy = 1500 #맵기
    salty = 2000 #짜기 (하루권장 나트륨 섭취량)
    kcal = 700 #한끼 섭취량
    return [spicy, salty, kcal]
    
def filtering(rule, menu):
    result = []
    print('Filtering Started!')
    print('---| 인원수 필터링 |---')
    result = people_filter(rule[1],menu)
    print('---| 가격 필터링 |---')
    result = price_filter(rule[2], result)
    print('---| 장소 필터링 |---')
    result = space_filter(rule[3],result)
    print('---| 맵기 필터링 |---')
    result = spicy_filter(rule[4],result)
    print('---| 건강식 필터링 |---')
    result = salty_filter(rule[5],result)
    print('---| 디저트 필터링 |---')
    result = sweety_filter(rule[6],result)
    print('---| 식사(국가)종류 필터링 |---')
    result = country_filter(rule[7],result)
    print('---| 밥/면 필터링 |---')
    result = riceORnoodle_filter(rule[8],result)
    print('---| 음식옵션 필터링 |---')
    result = foodOption_filter(rule[9],result)
    print('---| 칼로리 필터링 |---')
    result = kcal_filter(rule[10],result)
    
    if result == []:
        print('\n** 조건에 맞는 메뉴가 없습니다.')
    else:
        return result

    
def people_filter(rule, menu):
    result = []
    for i in range(len(menu)):
        if menu[i][1] == 0 or int(menu[i][1]) <= rule:
            print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
            result.append(menu[i])
    return result

def price_filter(rule, menu):
    result = []
    for i in range(len(menu)):
        if int(menu[i][2]) <= rule:
            print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
            result.append(menu[i])
    if result == []:
        print('조건에 맞는 메뉴가 없습니다.')
    return result

def space_filter(rule, menu):
    result = []
    for i in range(len(menu)):
        if menu[i][3] == 0 or int(menu[i][3]) == rule:
            print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
            result.append(menu[i])
    if result == []:
        print('조건에 맞는 메뉴가 없습니다.')
    return result

def spicy_filter(rule, menu):
    result = []

    # 맛설정 상관없음
    if rule == 0:
        for i in range(len(menu)):
            result.append(menu[i])
        print('( ** 모든 메뉴가 통과되었습니다. )')
        return result
        
    for i in range(len(menu)):
        # 순한맛 설정 (스코빌 1200)
        if rule == 1:
            print('순한맛으로 설정됨.\n')
            taste_rule = (int(menu[i][4]) <= 1200)
        # 보통맛 설정 (스코빌 2000)
        elif rule == 2:
            print('보통맛으로 설정됨.\n')
            taste_rule = (int(menu[i][4]) <= 2000)
        # 매운맛 설정 (-)
        elif rule == 3:
            print('매운맛으로 설정됨.\n')
            taste_rule = (int(menu[i][4]) > 2000)
        
        if taste_rule:
            print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
            result.append(menu[i])
    if result == []:
        print('조건에 맞는 메뉴가 없습니다.')
    return result

def salty_filter(rule, menu):
    # 건강식인지 확인.
    result = []
    if rule == 0:   # 상관없음 설정
        print('건강식 상관없음 설정됨.\n')
        for i in range(len(menu)):
                result.append(menu[i])
        print('( ** 모든 메뉴가 통과되었습니다. )')
        return result
    for i in range(len(menu)):
        # 건강식이면
        if rule == 1:
            print('건강식으로 설정됨.\n')
            salty_rule = (int(menu[i][5]) <= 900)
        # 건강식이 아니면        
        elif rule == 2:
            print('건강식 아님으로 설정됨.\n')
            salty_rule = (int(menu[i][5]) >= 900)
        if salty_rule:
            print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
            result.append(menu[i])
    if result == []:
        print('조건에 맞는 메뉴가 없습니다.')
    return result

def sweety_filter(rule, menu):
    result = []
    if rule == 0:
        print('디저트 아님으로 설정됨.\n')
        for i in range(len(menu)):
            if int(menu[i][7]) == 0:
                print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
                result.append(menu[i])
    if rule == 1:
        print('디저트로 설정됨.\n')
        for i in range(len(menu)):
            if int(menu[i][7]) == 1:
                print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
                result.append(menu[i])
    if result == []:
        print('조건에 맞는 메뉴가 없습니다.')
    return result

def country_filter(rule, menu):
    result = []
    if '상관없음' in rule:
        print('국가(한중일양)상관없음 설정됨.\n')
        for i in range(len(menu)):
            result.append(menu[i])
        print('( ** 모든 메뉴가 통과되었습니다. )')
        return result
    if '한식' in rule:
        print('한식으로 설정됨.\n')
        for i in range(len(menu)):
            if menu[i][8] == '한식':
                print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
                result.append(menu[i])
    if '중식' in rule:
        print('중식으로 설정됨.\n')
        for i in range(len(menu)):
            if menu[i][8] == '중식':
                print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
                result.append(menu[i])
    if '양식' in rule:
        print('양식으로 설정됨.\n')
        for i in range(len(menu)):
            if menu[i][8] == '양식':
                print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
                result.append(menu[i])
    if '일식' in rule:
        print('일식으로 설정됨.\n')
        for i in range(len(menu)):
            if menu[i][8] == '일식':
                print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
                result.append(menu[i])
    if result == []:
        print('조건에 맞는 메뉴가 없습니다.')
    return result
    
def riceORnoodle_filter(rule, menu):
    result = []
    
    if rule == 0:   # 상관없음 설정
        print('밥/면 상관없음 설정됨.\n')
        for i in range(len(menu)):
                result.append(menu[i])
        print('( ** 모든 메뉴가 통과되었습니다. )')
        return result
    for i in range(len(menu)):
        # 밥이면
        if rule == 1:
            print('밥으로 설정됨.\n')
            riceNoodle_rule = (int(menu[i][9]) == 1)
        # 면이면        
        elif rule == 2:
            print('면으로 설정됨.\n')
            riceNoodle_rule = (int(menu[i][9]) == 2)
        if riceNoodle_rule:
            print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
            result.append(menu[i])
    if result == []:
        print('조건에 맞는 메뉴가 없습니다.')
    return result

def foodOption_filter(rule, menu):
    result = []
    if rule == 0:
        print('음식종류 상관없음 설정됨.\n')
        for i in range(len(menu)):
            result.append(menu[i])
        print('( ** 모든 메뉴가 통과되었습니다. )')
        return result
    if '국물' in rule:
        print('국물로 설정됨.\n')
        for i in range(len(menu)):
            if '국물' in menu[i][10]:
                print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
                result.append(menu[i])
    if '볶음' in rule:
        print('볶음으로 설정됨.\n')
        for i in range(len(menu)):
            if '볶음' in menu[i][10]:
                print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
                result.append(menu[i])
    if '구이' in rule:
        print('구이으로 설정됨.\n')
        for i in range(len(menu)):
            if '구이' in menu[i][10]:
                print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
                result.append(menu[i])
    if '찜' in rule:
        print('찜으로 설정됨.\n')
        for i in range(len(menu)):
            if '한식' in menu[i][10]:
                print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
                result.append(menu[i])
    if '다이어트' in rule:
        print('다이어트로 설정됨.\n')
        for i in range(len(menu)):
            if '다이어트' in menu[i][10]:
                print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
                result.append(menu[i])
    if result == []:
        print('조건에 맞는 메뉴가 없습니다.')
    return result

def kcal_filter(rule, menu):
    result = []
    if rule == 0:   # 상관없음 설정
        print('칼로리 상관없음 설정됨.\n')
        for i in range(len(menu)):
                result.append(menu[i])
        print('( ** 모든 메뉴가 통과되었습니다. )')
        return result
    for i in range(len(menu)):
        if int(menu[i][9]) <= rule:
            print(f'{menu[i][0]} 메뉴가 통과되었습니다.')
            result.append(menu[i])
    if result == []:
        print('조건에 맞는 메뉴가 없습니다.')
    return result
    

def DiceFunc(menu, loop):
    dice=[]                      
    for i in range(loop):
        a = random.randint(1,menu)       
        while a in dice :      
            a = random.randint(1,menu)
        dice.append(a)
    return dice
            
def randomDice(menu, loop):
    dice = DiceFunc(len(menu), loop)
    result = []
    for i in range(loop):
        result.append(menu[dice[i]-1])
    return result
        
def print_result(result):
    print('필터링된 메뉴로는 ', end='')
    if len(result) == 1:
        print(f'{result[0][0]} ',end='')
    else:
        for i in range(len(result)-1):
            print(f'{result[i][0]}, ',end='')
        print(f'{result[len(result)-1][0]} ',end='')
    print('을(를) 추천합니다.')

MenuList = read_data()
show_menu(MenuList)
#filter = set_value()
filter = [None,4,80000,0,2,0,0,['한식','중식'],0,['국물'],0]
print(filter)
# 공란 / 인원수 / 기격 / 장소 / (순한맛 보통맛 매운맛) / 건강식 / 디저트 / 식사종류(한중일양) / (밥, 면) / (국물, 볶음, 찜, 구이, 다이어트) / 칼로리
FilteredMenus = filtering(filter, MenuList)
print(FilteredMenus)
print(f'선택할 수 있는 메뉴는 총 {len(FilteredMenus)}개 입니다.')
loop = int(input('몇개의 음식을 추천할까요?(숫자만입력) : '))
if loop > len(FilteredMenus):
    print('필터링된 결과의 메뉴수보다 많습니다.')
else:
    print_result(result = randomDice(FilteredMenus, loop))