country = input('(한식/중식/일식/양식) 공백기준 중복선택 가능 : ').split(' ')
if type(country) == list and len(country) > 1:
    print(1)