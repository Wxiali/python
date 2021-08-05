import PySimpleGUI as sg


def calc_bmi(h, w):
    try:
        h, w = float(h), float(w)
        bmi = round(w / h ** 2, 1)
        if bmi < 18.5:
            standard = '体重过轻！'
        elif 18.5 <= bmi <= 23.9:
            standard = '体重正常！'
        elif 24.0 <= bmi <= 27.9:
            standard = '体重过重，注意饮食！'
        else:
            standard = '体重肥胖，注意饮食！'
    except (ValueError, ZeroDivisionError):
        return None
    else:
        return f'BMI: {bmi}, {standard}'


layout = [[sg.Text('身高(单位：m )'), sg.InputText(size=(15,))],
          [sg.Text('体重(单位：kg)'), sg.InputText(size=(15,))],
          [sg.Button('计算 BMI', key='submit')],
          [sg.Text('', key='bmi', size=(20, 2))],
          [sg.Quit('退出', key='q')]]

window = sg.Window('BMI计算', layout, font='微软雅黑')

while True:
    event, value = window.Read()
    if event == 'submit':
        bmi = calc_bmi(value[0], value[1])
        if bmi:
            window.Element('bmi').Update(bmi, text_color='black')
        else:
            window.Element('bmi').Update('输入有误！', text_color='red')
    elif event == 'q':
        break

window.Close()
