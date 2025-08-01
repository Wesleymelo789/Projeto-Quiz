from Quiz_perguntas import perguntas_quiz
import Resultado_Quiz
def jogar_quiz():
    contador_perguntas = 0
    print ('Bem vindo ao Quiz - v2')
    print ('Responda as perguntas digitando o número da opção correta')
    perguntas = perguntas_quiz()
    contador = 0
    while contador < len(perguntas):
        pergunta_atual = perguntas[contador]

        print(pergunta_atual['pergunta'])

        for indice, i in enumerate (pergunta_atual.get('opcoes')):
            print(f'{indice+1}) {i}')

        resposta = int (input('digite sua resposta (1-4): '))


        if pergunta_atual.get('resposta') == pergunta_atual.get('opcoes')[resposta-1]:
            print ('você acertou!')
            contador_perguntas += 1
        else:
            print ('você não acertou a resposta!')
            print(f'A resposta correta era: {pergunta_atual.get("resposta")}')

        contador += 1

    Resultado_Quiz.Resultado_final(contador_perguntas, len(perguntas))

jogar_quiz()




