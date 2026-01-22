def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("必须输入正数！")
            else:
                return value
        except ValueError:
            print("只能输入数字！")

height = input_float('请输入身高（单位：m）：')
weight = input_float('请输入体重（单位：kg）：')

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f'BMI指数为{bmi:.2f}, 属于过轻。')
elif bmi < 25:
    print(f'BMI指数为{bmi:.2f}, 属于正常。')
elif bmi < 28:
    print(f'BMI指数为{bmi:.2f}, 属于过重。')
elif bmi < 32:
    print(f'BMI指数为{bmi:.2f}, 属于肥胖。')
else:
    print(f'BMI指数为{bmi:.2f}, 属于严重肥胖。')
