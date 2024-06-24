#############################################
                                        
#              머먹지 로직 테스트 v0                    
                                         
#############################################

# 사용자 맞춤형 필터링 옵션 ( 인원수, 가격, 배달/방문 등 )
# 대화형 필터설정 인공지능 탑재
# 추천된 메뉴에 대한 만족도를 추천 메커니즘에 반영
# 사용자 특성을 분석하는 인공지능으로 만족도 예측
# 다이어트 맞춤형 메뉴추천 기능

# 필터종류 : 인원수(혼밥/2인/4인이상) / 가격 / (배달/방문) / 맵기 / 짜기 / 달기 / (한/중/일/양) / (밥/면) / (국물/볶음/찜/구이/다이어트) / 칼로리

#############################################
# < 음식 샘플 >

# 짜장면(불짜장면) : 모두 가능 / 6000~8000원 / 모두 가능 / 둘다 / 조금 짬 / 안 담 / 중식 / 면 / 볶음 / 800kcal
# 족발(불족발) : 2인이상 추천 / 20000~40000원 / 모두 가능 / 둘다 / 조금 짬 / 안 담 / 한식, 중식 / 밥 / 구이 / 700kcal
# 라면(매운라면 포함) : 모두 가능 / 1000원 / 모두 가능 / 둘다 / 조금 짬 / 안 담 / 한식 / 면 / 국물 / 450kcal
# 라멘 : 모두 가능 / 10000원~ / 모두 가능 / 둘다 / 조금 짬 / 안 담 / 일식 / 면 / 국물 / 400kcal
# 기영이 : 2인이상 / 0원 / 배달추천 / 안 매움 / 짤 것 같음 / 안 담 / 한식(?) / 밥..? / 구이 / 10000kcal
#############################################
people = 0
price = 0
space = 0
spicy = 0
salty = 0
sweety = 0
where = 0
rice = 0
type = 0
kcal = 0
# < Logic >

# 메뉴들을 딕셔너리로 저장시킬때
짜장면 = {'name':'짜장면', '인원수':0, '가격':6000, '배달방문':0, '맵기':4, '짜기':1, '달기':0, '국가':2, '밥면':2, '음식유형':2}
족발 = {'name':'족발', '인원수':2, '가격':20000, '배달방문':0, '맵기':4, '짜기':1, '달기':0, '국가':'12', '밥면':1, '음식유형':'24'}
라면 = {'name':'라면', '인원수':0, '가격':1000, '배달방문':0, '맵기':4, '짜기':1, '달기':0, '국가':1, '밥면':2, '음식유형':1}
라멘 = {'name':'라멘', '인원수':0, '가격':10000, '배달방문':0, '맵기':4, '짜기':1, '달기':0, '국가':3, '밥면':2, '음식유형':1}

menuDict = {'짜장면':[0, 6000, 0, 4, 1, 0, 2, 1, 2],
            '족발':[2,20000,0,4,1,0,12,1,24],
            '라면':[0,1000,0,4,1,0,1,2,1],
            '라멘':[0,10000,0,4,1,0,3,2,1]}

# 메뉴들을 리스트로 저장시킬때
menuList = [['짜장면',[0,6000,0,2,0,2,1,2]],
            ['족발',[2,20000,0,4,0,12,1,24]],
            ['라면',[0,1000,0,4,1,0,1,2,1]],
            ['라멘',[0,10000,0,4,1,0,3,2,1]]
            ]

#############################################
def openMenu(file):
        f = open(file, 'r')
        lines = f.readlines()
        for line in lines:
            line = line.strip()  # \n 제거
            print(line)
        f.close()   
        
class MenuSelector:
    def __init__(self, menu_list):
        name = ''
        age = 0
        people = 0
        price = 0
        space = 0
        spicy = 0
        salty = 0
        sweety = 0
        where = 0
        rice = 0
        type = 0
        kcal = 0 

    def setting_start(self):
        print('필터설정을 시작합니다.')
        self.people = 0
        self.price = 0
        self.space = 0
        self.spicy = 0
        self.salty = 0
        self.sweety = 0
        self.where = 0
        self.rice = 0
        self.type = 0
        self.kcal = 0
        print(1)
    
#############################################
#       테스트 코드

#openMenu("Logic_TEST/Menu.txt")

test = MenuSelector(openMenu("Logic_TEST/Menu.txt"))
test.setting_start()