import random

class Game:
    def __init__(self):
        self.target=random.randint(1,100)
        print('게임을 시작하겠습니다.')
    
    def play(self):
        while True:
            guess = self.get_user_input()
            if guess == self.target:
                print('정답입니다.')
                break
            elif guess > self.target:
                print(f'{guess}보다 작아야합니다.')
            elif guess < self.target:
                print(f'{guess}보다 커야합니다.')
    
    def get_user_input(self):
        try:
            guess = int(input('1부터 100사이의 숫자를 입력하세요: '))
            if 1<= guess <= 100:
                return guess
            else:
                print('1부터 100까지 숫자만 입력하세요.')
        except:
            print('올바른 숫자를 입력하세요')