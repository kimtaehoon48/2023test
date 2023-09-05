import random
class Hang:
    def __init__(self):
        self.equipment_type = ['무기','방어구','악세사리','방어구','무기','방어구']
        self.select = None
    def play(self):
        print('브론즈 항아리 확률 = 일반:70%, 고급:20%, 희귀:9%, 영웅:1%')
        print('실버 항아리 확률 = 일반:60%, 고급:28%, 희귀:10.5%, 영웅:1.5%')
        print('골드 항아리 확률 = 일반:55%, 고급:30%, 희귀:12%, 영웅:3%')
        print('항아리 등급을 선택해주세요. 1번 브론즈 항아리, 2번 실버 항아리, 3번 골드 항아리 : ')
        while True:
            try:
                equipment_tpye = random.choice(self.equipment_type)
                self.select=int(input())
                if self.select == 1:
                    print('브론즈 항아리 뽑기 결과는!!!!!!\t' + self.hang_bronze()+equipment_tpye+'\n\n')
                elif self.select ==2:
                    print('실버 항아리 뽑기 결과는!!!!!!\t'+ self.hang_silver()+equipment_tpye+'\n\n')
                elif self.select ==3:
                    print('골드 항아리 뽑기 결과는!!!!!!\t'+ self.hang_gold()+equipment_tpye+'\n\n')
                elif self.select ==4:
                    print('그만하자....')
                    break
            except ValueError:
                self.select=int(input('제대로된 숫자를 입력해주세요'))
    def hang_bronze(self):
        percent=random.randint(1,1000)
        if 0< percent <= 700:
            return '일반'
        elif 700 < percent <= 900:
            return '고급'
        elif 900 < percent <= 990:
            return '희귀'
        elif 990 < percent <= 1000:
            return '영웅'
        
    def hang_silver(self):
        percent=random.randint(1,1000)
        if 0< percent <= 600:
            return '일반'
        elif 600 < percent <= 880:
            return '고급'
        elif 880 < percent <= 985:
            return '희귀'
        elif 985 < percent <= 1000:
            return '영웅'
        
    def hang_gold(self):
        percent=random.randint(1,1000)
        if 0< percent <= 550:
            return '일반'
        elif 550 < percent <= 850:
            return '고급'
        elif 850 < percent <= 970:
            return '희귀'
        elif 970 < percent <= 1000:
            return '영웅'
        
A=Hang()
A.play()