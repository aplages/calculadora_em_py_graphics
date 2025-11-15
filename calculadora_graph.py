''' Programa que executa uma calculadora SIMPLES com interface em graphics.
É possível clicar nos botões ou digitar pelo teclado, exceto o botão clicável "LIMPA" (apenas pela tela) e a função "apagar" (apenas pelo "BackSpace" do teclado) 
        *obs: preguiça, farei posteriormente
Por enquanto é apenas uma calculadora extremamente simples, portando:
    - Não aceita mais de uma operação ao mesmo tempo (mas é possível fazer outra usando o resultado da anterior)
    - Aceita apenas SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO e DIVISÃO para operações
    - Como não aceita mais de uma operação, tabém não aceita mais que 1 operador por operação, portanto, não coloque mais do que 1 operador
        *mas caso isso aconteça, ele considera apenas o primeiro operador, o que vem depois vira apenas um número, descartando qualquer operador que estiver no meio.
'''
from time import sleep
import graphics as gf
lim_larg = 400 # estabelece uma largura pra janela
lim_alt = 500 # estabelece uma altura pra janela

def escreve_visor(win, coords, texto):
    # cria uma variavel caixa de texto para ser utilizada no visor da calculadora
    operX = ((coords[0]) + (coords[2]))/2
    operY = ((coords[1]) + (coords[3]))/2
    texto = gf.Text(gf.Point(operX, operY), texto)
    return texto

def separa_texto(texto):
    # separa um texto operacional em uma lista contendo numeros e operador que separa os numeros. essa função é usada pela função "calcula()"
    oper = []
    temp = ''
    tem_operador = False
    for i in texto:
        if i not in '+-*x/÷':
            temp += i
        else:
            if not tem_operador:
                # Para não colocar mais de um operador na operação final, ele coloca apenas o primeiro
                oper.append(temp)
                temp = ''
                oper.append(i)
                tem_operador = True
    if len(temp) > 0:
        oper.append(temp)
    return oper

def calcula(texto):
    # executa o calculo a partir do texto separado (lista) pela func "separa_texto()"
    # primeiro a funcao tenta deixar em int(), se não é possível, ela coloca em float()
    oper = separa_texto(texto)
    operador = ''
    for n in oper:
        if n in '+-*x/÷':
            operador = n
            oper.pop(oper.index(n))
    
    calculo = 0
    if len(oper) == 2:
        try:
            if operador == '+':
                calculo = int(oper[0]) + int(oper[1])
            elif operador == '-':
                calculo = int(oper[0]) - int(oper[1])
            elif operador == '*' or operador == 'x':
                calculo = int(oper[0]) * int(oper[1])
            elif operador == '/' or operador == '÷':
                calculo = int(oper[0]) / int(oper[1])
            elif operador == '':
                return oper
            return calculo
        except:
            if operador == '+':
                calculo = float(oper[0]) + float(oper[1])
            elif operador == '-':
                calculo = float(oper[0]) - float(oper[1])
            elif operador == '*' or operador == 'x':
                calculo = float(oper[0]) * float(oper[1])
            elif operador == '/' or operador == '÷':
                calculo = float(oper[0]) / float(oper[1])
            elif operador == '':
                return oper
            return calculo
    else:
        return float(oper[0])

def teste_botoes(tecla, clique):
    # Teste do Clique:
    # Verifica o botão pressionado (mouse/tela ou tecla/teclado) e retorna um nome de botão que será usado posteriormente como número ou operador pela função "calcula()"
        if tecla != '':
            if tecla in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'colon', 'slash', 'plus', 'minus', 'colon', 'slash', 'asterisk', 'x', 'Return', 'equal', 'BackSpace', 'c']:
                if tecla in ['colon', 'slash']:
                    return '÷'
                elif tecla in ['asterisk', 'x']:
                    return 'x'
                elif tecla in ['equal', 'Return']:
                    return '='
                elif tecla == 'plus':
                    return '+'
                elif tecla == 'minus':
                    return '-'
                elif tecla == 'c':
                    return 'LIMPA'
                else:
                    return tecla
            else:
                return ''
        if clique != None:
            # Coluna 1
            if ((clique.getX() >= 10) and (clique.getX() <= 100)):
                if ((clique.getY() >= 100) and (clique.getY() <= 170)):
                    return '7'
                elif ((clique.getY() >= 180) and (clique.getY() <= 250)):
                    return '4'
                elif ((clique.getY() >= 260) and (clique.getY() <= 330)):
                    return '1'
                elif ((clique.getY() >= 340) and (clique.getY() <= 410)):
                    return 'LIMPA'
            # Coluna 2
            elif ((clique.getX() >= 110) and (clique.getX() <= 200)):
                if ((clique.getY() >= 100) and (clique.getY() <= 170)):
                    return '8'
                elif ((clique.getY() >= 180) and (clique.getY() <= 250)):
                    return '5'
                elif ((clique.getY() >= 260) and (clique.getY() <= 330)):
                    return '2'
                elif ((clique.getY() >= 340) and (clique.getY() <= 410)):
                    return '0'
                
            # Coluna 3
            elif ((clique.getX() >= 210) and (clique.getX() <= 300)):
                if ((clique.getY() >= 100) and (clique.getY() <= 170)):
                    return '9'
                elif ((clique.getY() >= 180) and (clique.getY() <= 250)):
                    return '6'
                elif ((clique.getY() >= 260) and (clique.getY() <= 330)):
                    return '3'
                elif ((clique.getY() >= 340) and (clique.getY() <= 410)):
                    return '='
            # Coluna 4
            elif ((clique.getX() >= 310) and (clique.getX() <= 390)):
                if ((clique.getY() >= 100) and (clique.getY() <= 170)):
                    return '+'
                elif ((clique.getY() >= 180) and (clique.getY() <= 250)):
                    return '-'
                elif ((clique.getY() >= 260) and (clique.getY() <= 330)):
                    return 'x'
                elif ((clique.getY() >= 340) and (clique.getY() <= 410)):
                    return '÷'
            else:
                return ''
        return None



def calculadora():
    win = gf.GraphWin('Calculadora', lim_larg, lim_alt)

    coords = {
        '7': [10, 100, 100, 170],
        '8': [110, 100, 200, 170],
        '9': [210, 100, 300, 170],
        '+': [310, 100, 390, 170],
        '4': [10, 180, 100, 250],
        '5': [110, 180, 200, 250],
        '6': [210, 180, 300, 250],
        '-': [310, 180, 390, 250],
        '1': [10, 260, 100, 330],
        '2': [110, 260, 200, 330],
        '3': [210, 260, 300, 330],
        '*': [310, 260, 390, 330],
        'limpa': [10, 340, 100, 410],
        '0': [110, 340, 200, 410],
        '=': [210, 340, 300, 410],
        '/': [310, 340, 390, 410],
        'visor': [10, 10, 390, 90]
    }


    ## Caixas de texto (BOTOES CLICÁVEIS DA CALCULADORA):
    # 7
    num7 = gf.Rectangle(gf.Point(coords['7'][0], coords['7'][1]), gf.Point(coords['7'][2], coords['7'][3]))
    num7.setFill('white')
    num7.draw(win)
    texto7 = gf.Text(gf.Point(((coords['7'][0]) + (coords['7'][2]))/2, ((coords['7'][1]) + (coords['7'][3]))/2), '7')
    texto7.draw(win)

    # 8
    num8 = gf.Rectangle(gf.Point(coords['8'][0], coords['8'][1]), gf.Point(coords['8'][2], coords['8'][3]))
    num8.setFill('white')
    num8.draw(win)
    texto8 = gf.Text(gf.Point(((coords['8'][0]) + (coords['8'][2]))/2, ((coords['8'][1]) + (coords['8'][3]))/2), '8')
    texto8.draw(win)
    
    # 9
    num9 = gf.Rectangle(gf.Point(coords['9'][0], coords['9'][1]), gf.Point(coords['9'][2], coords['9'][3]))
    num9.setFill('white')
    num9.draw(win)
    texto9 = gf.Text(gf.Point(((coords['9'][0]) + (coords['9'][2]))/2, ((coords['9'][1]) + (coords['9'][3]))/2), '9')
    texto9.draw(win)

    # +
    bot_mais = gf.Rectangle(gf.Point(coords['+'][0], coords['+'][1]), gf.Point(coords['+'][2], coords['+'][3]))
    bot_mais.setFill('white')
    bot_mais.draw(win)
    texto_mais = gf.Text(gf.Point(((coords['+'][0]) + (coords['+'][2]))/2, ((coords['+'][1]) + (coords['+'][3]))/2), '+')
    texto_mais.draw(win)


    # 4
    num4 = gf.Rectangle(gf.Point(coords['4'][0], coords['4'][1]), gf.Point(coords['4'][2], coords['4'][3]))
    num4.setFill('white')
    num4.draw(win)
    texto4 = gf.Text(gf.Point(((coords['4'][0]) + (coords['4'][2]))/2, ((coords['4'][1]) + (coords['4'][3]))/2), '4')
    texto4.draw(win)

    # 5
    num5 = gf.Rectangle(gf.Point(coords['5'][0], coords['5'][1]), gf.Point(coords['5'][2], coords['5'][3]))
    num5.setFill('white')
    num5.draw(win)
    texto5 = gf.Text(gf.Point(((coords['5'][0]) + (coords['5'][2]))/2, ((coords['5'][1]) + (coords['5'][3]))/2), '5')
    texto5.draw(win)

    # 6
    num6 = gf.Rectangle(gf.Point(coords['6'][0], coords['6'][1]), gf.Point(coords['6'][2], coords['6'][3]))
    num6.setFill('white')
    num6.draw(win)
    texto6 = gf.Text(gf.Point(((coords['6'][0]) + (coords['6'][2]))/2, ((coords['6'][1]) + (coords['6'][3]))/2), '6')
    texto6.draw(win)
    
    # -
    bot_menos = gf.Rectangle(gf.Point(coords['-'][0], coords['-'][1]), gf.Point(coords['-'][2], coords['-'][3]))
    bot_menos.setFill('white')
    bot_menos.draw(win)
    texto_menos = gf.Text(gf.Point(((coords['-'][0]) + (coords['-'][2]))/2, ((coords['-'][1]) + (coords['-'][3]))/2), '-')
    texto_menos.draw(win)

    # 1
    num1 = gf.Rectangle(gf.Point(coords['1'][0], coords['1'][1]), gf.Point(coords['1'][2], coords['1'][3]))
    num1.setFill('white')
    num1.draw(win)
    texto1 = gf.Text(gf.Point(((coords['1'][0]) + (coords['1'][2]))/2, ((coords['1'][1]) + (coords['1'][3]))/2), '1')
    texto1.draw(win)
    

    # 2
    num2 = gf.Rectangle(gf.Point(coords['2'][0], coords['2'][1]), gf.Point(coords['2'][2], coords['2'][3]))
    num2.setFill('white')
    num2.draw(win)
    texto2 = gf.Text(gf.Point(((coords['2'][0]) + (coords['2'][2]))/2, ((coords['2'][1]) + (coords['2'][3]))/2), '2')
    texto2.draw(win)
    

    # 3
    num3 = gf.Rectangle(gf.Point(coords['3'][0], coords['3'][1]), gf.Point(coords['3'][2], coords['3'][3]))
    num3.setFill('white')
    num3.draw(win)
    texto3 = gf.Text(gf.Point(((coords['3'][0]) + (coords['3'][2]))/2, ((coords['3'][1]) + (coords['3'][3]))/2), '3')
    texto3.draw(win)

    # *
    bot_multip = gf.Rectangle(gf.Point(coords['*'][0], coords['*'][1]), gf.Point(coords['*'][2], coords['*'][3]))
    bot_multip.setFill('white')
    bot_multip.draw(win)
    texto_multip = gf.Text(gf.Point(((coords['*'][0]) + (coords['*'][2]))/2, ((coords['*'][1]) + (coords['*'][3]))/2), 'x')
    texto_multip.draw(win)


    # LIMPA 
    bot_limpa = gf.Rectangle(gf.Point(coords['limpa'][0], coords['limpa'][1]), gf.Point(coords['limpa'][2], coords['limpa'][3]))
    bot_limpa.setFill('white')
    bot_limpa.draw(win)
    texto_limpa = gf.Text(gf.Point(((coords['limpa'][0]) + (coords['limpa'][2]))/2, ((coords['limpa'][1]) + (coords['limpa'][3]))/2), 'LIMPA')
    texto_limpa.draw(win)

    # 0
    num0 = gf.Rectangle(gf.Point(coords['0'][0], coords['0'][1]), gf.Point(coords['0'][2], coords['0'][3]))
    num0.setFill('white')
    num0.draw(win)
    texto0 = gf.Text(gf.Point(((coords['0'][0]) + (coords['0'][2]))/2, ((coords['0'][1]) + (coords['0'][3]))/2), '0')
    texto0.draw(win)

    # =
    bot_igual = gf.Rectangle(gf.Point(coords['='][0], coords['='][1]), gf.Point(coords['='][2], coords['='][3]))
    bot_igual.setFill('white')
    bot_igual.draw(win)
    texto_igual = gf.Text(gf.Point(((coords['='][0]) + (coords['='][2]))/2, ((coords['='][1]) + (coords['='][3]))/2), '=')
    texto_igual.draw(win)

    # /
    bot_div = gf.Rectangle(gf.Point(coords['/'][0], coords['/'][1]), gf.Point(coords['/'][2], coords['/'][3]))
    bot_div.setFill('white')
    bot_div.draw(win)
    texto_div = gf.Text(gf.Point(((coords['/'][0]) + (coords['/'][2]))/2, ((coords['/'][1]) + (coords['/'][3]))/2), '÷')
    texto_div.draw(win)
    ##

    lista_botoes = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9, bot_div, bot_igual, bot_mais, bot_menos, bot_multip, bot_limpa]

    # texto saída
    escapar = gf.Text(gf.Point(lim_larg/2, 490), 'Pressione "ESC" para sair.')
    escapar.draw(win)
    

    # Visor da calculadora:
    visor = gf.Rectangle(gf.Point(coords['visor'][0], coords['visor'][1]), gf.Point(coords['visor'][2], coords['visor'][3]))
    visor.setFill('beige')
    visor.draw(win)
    
    #
    tecla = ''
    texto = ''
    texto_visor = escreve_visor(win, coords['visor'], texto)
    texto_visor.draw(win)
    
    while tecla != 'Escape':
        # Se o usuário pressiona "Esc", o programa encerra.
        tecla = win.checkKey()
        clique = win.checkMouse()
        
        # Cria uma variável que representa o botão pressionado
        pressionado = teste_botoes(tecla, clique)
        if (pressionado != None) and (pressionado != ''):
            if pressionado in '1234567890+-*/÷x':
                
                if pressionado == '1':
                    num1.setFill('gray')
                    sleep(0.1)
                    num1.setFill('white')
                elif pressionado == '2':
                    num2.setFill('gray')
                    sleep(0.1)
                    num2.setFill('white')
                elif pressionado == '3':
                    num3.setFill('gray')
                    sleep(0.1)
                    num3.setFill('white')
                elif pressionado == '4':
                    num4.setFill('gray')
                    sleep(0.1)
                    num4.setFill('white')
                elif pressionado == '5':
                    num5.setFill('gray')
                    sleep(0.1)
                    num5.setFill('white')
                elif pressionado == '6':
                    num6.setFill('gray')
                    sleep(0.1)
                    num6.setFill('white')
                elif pressionado == '7':
                    num7.setFill('gray')
                    sleep(0.1)
                    num7.setFill('white')
                elif pressionado == '8':
                    num8.setFill('gray')
                    sleep(0.1)
                    num8.setFill('white')
                elif pressionado == '9':
                    num9.setFill('gray')
                    sleep(0.1)
                    num9.setFill('white')
                elif pressionado == '0':
                    num0.setFill('gray')
                    sleep(0.1)
                    num0.setFill('white')
                elif pressionado == '+':
                    bot_mais.setFill('gray')
                    sleep(0.1)
                    bot_mais.setFill('white')
                elif pressionado == '-':
                    bot_menos.setFill('gray')
                    sleep(0.1)
                    bot_menos.setFill('white')
                elif pressionado == 'x':
                    bot_multip.setFill('gray')
                    sleep(0.1)
                    bot_multip.setFill('white')
                elif pressionado == '÷':
                    bot_div.setFill('gray')
                    sleep(0.1)
                    bot_div.setFill('white')

                texto_visor.undraw()
                texto += pressionado

                texto_visor = escreve_visor(win, coords['visor'], texto)
                texto_visor.draw(win)
                # escreve números / operadores
            
            elif pressionado == 'LIMPA':
                bot_limpa.setFill('gray')
                sleep(0.1)
                bot_limpa.setFill('white')
                texto = ''
                texto_visor.undraw()
                # limpa a operação atual 
                ## só funciona pelo botão clicável

            elif pressionado == 'BackSpace':
                texto_visor.undraw()
                texto = texto[:-1]
                texto_visor = escreve_visor(win, coords['visor'], texto)
                texto_visor.draw(win)
                # apaga apenas 1 digito (o último) da operação atual
                ## só funciona pelo teclado

            elif pressionado == '=':
                bot_igual.setFill('gray')
                sleep(0.1)
                bot_igual.setFill('white')

                texto_visor.undraw()

                result = calcula(texto)
                if (result-int(result)) == 0:
                    result = int(result)
                
                texto_visor = escreve_visor(win, coords['visor'], result)
                texto_visor.draw(win)
                texto = str(result)
                # calcula a operação, apaga ela do visor e mostra o resultado
                ## ele testa se o número pode ser int(), se não, ele deixa em float() -- pra nao ficar feio (ex: "45.0" vira "45"), mas tenho quase certeza de que usa menos memória/bytes sei la algo assim
    win.close()

if __name__ == '__main__':
    calculadora()
