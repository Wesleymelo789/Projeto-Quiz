def Resultado_final(contador_perguntas, qtd_perguntas):

    print('RESULTADO FINAL!!!')
    print(f'Você acertou {contador_perguntas} de {qtd_perguntas} perguntas')
    aproveitamento = (contador_perguntas / qtd_perguntas) * 100
    print(f'{aproveitamento}%')

    if aproveitamento == 100:
        print('você acertou todas as questões')
    elif aproveitamento >= 70:
        print('muito bom, continue assim!')
    else:
        print('você pode melhorar, estude mais!')