print("Welcome to BMI Calculator")
print('Let\'s calculate your body mass index. Enter value in inches only not feet(if using inches as height) ')
unit = int(input('What unit system you want to use ? (m/kg or inches/pounds, just press 1 or 2 ):  '))
weight = float(input('Enter weight (just the digit): '))
height = float(input('Enter height (just the  digit): '))

bmi = 0
if unit == 1:
    bmi = bmi + float.__round__((weight / (height ** 2)), 2)
elif unit == 2:
    bmi = bmi + float.__round__((weight / (height ** 2)) * 703, 2)
else:
    print('You entered Invalid values')

print(bmi)
if bmi < 18.5:
    print('You are underweight!!! You should see a Nutritionist.')
elif 18.5 <= bmi <= 24.5:
    print('Congratulations!!! You have a healthy Body Mass Index. Keep Going.')
elif 24.5 < bmi <= 30:
    print('You are gaining weight!!! you should start doing exercise.')
elif 30 < bmi <= 56:
    print('You are Obese!!! You must see a dietician and gym instuctor.')
elif 56 < bmi < 100:
    print(' You are Obese!!! You need to see a Doctor and a surgery most probably!!!')
else:
    print('You entered Invalid value!!!')
