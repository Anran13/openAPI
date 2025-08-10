class BMI:
    def __init__(self, height:float, weight:float):
        self.height = height
        self.weight = weight
        
    def get_BMI(self)->float:
        return round(self.weight/((self.height/100)**2), 2)

    def get_status(self, bmi:float)->str:
        status = ""
        if bmi >= 35 :
            status = '重度肥胖'
        elif bmi >= 30 :
            status = '中度肥胖'
        elif bmi >= 27 :
            status = '輕度肥胖'
        elif bmi >= 24 :
            status = '過重'
        elif bmi >= 18.5 :
            status = '正常範圍'
        else :
            status = '過輕'
        return status

def main():
    while(True):
        try:
            height = float(input("Please enter your height(cm):"))
            weight = float(input("Please enter your weight(kg):"))
            test = BMI(height=height, weight=weight)
            break
        except Exception:
            print("The format is wrong, please enter again!")
    
    bmi = test.get_BMI()
    status = test.get_status(bmi)
    print(f'BMI = {bmi}')
    print(f'The status is {status}')

if __name__ == '__main__':
    main()