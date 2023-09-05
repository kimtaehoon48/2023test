import random

class Game:
    def __init__(self):
        self.A = None
        self.B = None
        self.C=None
        print('게임을 시작하겠습니다~~')
        self.getdata()

        while True:
            self.inputdata()
            self.C = self.result()
            if self.C == True:
                break

    def getdata(self):
        self.A=random.randrange(1,101)
    def inputdata(self):
        try:
            self.B=int(input('1부터 100 사이 숫자를 입력해주세요'))
        except:
            self.B=int(input('1부터 100 사이 숫자만~~~ 입력해주세요~~~'))
            self.inputdata()
    def result(self):
        if self.A>self.B:
            print(f'{self.B} 보다 숫자가 커야합니다.')
            return False
        elif self.A<self.B:
            print(f'{self.B} 보다 숫자가 작아야합니다.')
            return False
        elif self.A==self.B:
            print('정답입니다.') 
            return True

Game()