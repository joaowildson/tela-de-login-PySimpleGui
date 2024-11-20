import PySimpleGUI as sg
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entrar')]
]

janela = sg.Window('tela de login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'joao' and valores['senha'] == '12345':
            print('fucionou')