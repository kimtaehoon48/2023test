import random

class Hang:
    def __init__(self):
        self.equipment_probabilities = {
            '브론즈': {'일반': 70, '고급': 20, '희귀': 9, '영웅': 1},
            '실버': {'일반': 60, '고급': 28, '희귀': 10, '영웅': 1.5},
            '골드': {'일반': 55, '고급': 30, '희귀': 12, '영웅': 3}
        }
        self.equipment_type_probabilities = {'무기': 30, '방어구': 40, '악세사리': 30}

    def play(self):
        print('항아리 확률:')
        for ariri, probabilities in self.equipment_probabilities.items():
            print(f'{ariri} 항아리 확률 = ', end='')
            for grade, probability in probabilities.items():
                print(f'{grade}:{probability}%', end=', ')
            print()
        
        while True:
            try:
                selection = input('항아리 등급을 선택해주세요 (브론즈/실버/골드): ')
                
                if selection in self.equipment_probabilities:
                    equipment_grade = None
                    
                    while equipment_grade is None:
                        for grade, probability in self.equipment_probabilities[selection].items():
                            percent = random.random()
                            if percent*100 <= probability:
                                equipment_grade = grade
                                break
                        
                        if equipment_grade is None:
                            percent = random.random()
                    equipment_type=None
                    while equipment_type is None:
                        for type, probability in self.equipment_type_probabilities.items():
                            equipment_type_percent=random.random()
                            if equipment_type_percent*100 <= probability:
                                equipment_type = type
                                break
                        if equipment_type is None:
                            equipment_type_percent = random.random()
                            
                    print(f'{selection} 항아리 뽑기 결과는!!!!!! {equipment_grade} - {equipment_type} 입니다!\n\n')
                elif selection == '그만':
                    print('게임을 종료합니다.')
                    break
                else:
                    print('올바른 등급을 입력하세요.')
            except ValueError:
                print('제대로된 숫자를 입력하세요')

if __name__ == "__main__":
    A = Hang()
    A.play()
