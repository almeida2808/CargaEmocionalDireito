import re

import pandas as pd

def valencia(lexico, texto, flip=True, output="completo"):
    """
    Calcula uma métrica da valência de um texto.
    
    Parâmetros:
    
    lexico - Aponta para um arquivo contendo o OpLexicon ou a versão não-flexionada do SentiLex.
    
    texto - String contendo o texto que terá sua valência calculada.
    
    flip - Booleano indicando se devemos aplicar o método para lidar com intensificadores e negadores.
    (Adaptado de Avanço e Nunes, 2014)
    
    output - Um de "completo", "indice", "percentual". Quando completo, retorna uma tupla com o valor do índice
    e o percentual de palavras com carga emocional diferente de 0.
    """
        
    #listas de negadores (flip), amplificadores e redutores
    lex_flip = ['jamais','nada','nem', 'nenhum', 'ninguém','nunca','não','tampouco']
    lex_amplificador  =['mais', 'muito', 'demais', 'completamente', 'absolutamente', 'totalmente', 'definitivamente', 'extremamente', 'frequentemente', 'bastante']
    lex_redutor = ['pouco', 'quase','menos','apenas']
    
    if "lexico_v3.0" in lexico:
        lex = pd.read_csv(lexico)
        lex.columns = ["palavra", "classe", "valor", "método"]

    elif 'SentiLex' in lexico:
        lex = pd.read_csv(lexico, sep = 'N0=')
        lex.columns = ['palavrabruto','valorbruto']
        lex['palavra']= lex.apply(lambda row: str(row.palavrabruto).split('.')[0], axis=1)
        lex['valor'] = lex.apply(lambda row: str(row.valorbruto).split(';')[0], axis=1)
        
    lex_dict = {k:v for k, v in zip(lex.palavra, lex.valor)}

    palavras_texto = re.findall(r'\w+',texto)

    contador_relativo = 0
    contador_absoluto = 0
    contador_total = len(palavras_texto)

        
    for i in range(len(palavras_texto)):
        
        #cálculo levando em conta negativas e intensificadores
        if flip == True:
            if palavras_texto[i-1 or i-2 or i-3 or i-4] in lex_amplificador: 
                #o método .get() aceita um default para caso a chave não seja encontrada. Isso economiza o if.

                if palavras_texto[i-1 or i-2 or i-3 or i-4] in lex_flip: 
                    contador_relativo += int(lex_dict.get(palavras_texto[i], 0)) / 3
                    contador_absoluto += abs(int(lex_dict.get(palavras_texto[i], 0))) / 3

                else:
                    contador_relativo += int(lex_dict.get(palavras_texto[i], 0)) * 3
                    contador_absoluto += abs(int(lex_dict.get(palavras_texto[i], 0))) * 3

            elif palavras_texto[i-1 or i-2 or i-3 or i-4] in lex_redutor: 

                if palavras_texto[i-1 or i-2 or i-3 or i-4] in lex_flip: 
                    contador_relativo += int(lex_dict.get(palavras_texto[i], 0)) * 3
                    contador_absoluto += abs(int(lex_dict.get(palavras_texto[i], 0))) * 3

                else:
                    contador_relativo += int(lex_dict.get(palavras_texto[i], 0)) / 3
                    contador_absoluto += abs(int(lex_dict.get(palavras_texto[i], 0))) / 3

            elif palavras_texto[i-1 or i-2 or i-3 or i-4] in lex_flip: 
                contador_relativo += int(lex_dict.get(palavras_texto[i], 0)) * -1
                contador_absoluto += abs(int(lex_dict.get(palavras_texto[i], 0)))

            else:
                contador_relativo += int(lex_dict.get(palavras_texto[i], 0))
                contador_absoluto += abs(int(lex_dict.get(palavras_texto[i], 0)))
        
        #cálculo simples
        elif flip == False:
            contador_relativo += int(lex_dict.get(palavras_texto[i], 0))
            contador_absoluto += abs(int(lex_dict.get(palavras_texto[i], 0)))

        else:            
            print("ERRO! flip deve ser um booleano")
    
    indice = contador_relativo/len(palavras_texto) * 1000
    porcentagem_emocao = contador_absoluto / contador_total

    if output == "completo":
        return (indice, porcentagem_emocao)
    elif output == "indice":
        return indice
    elif output == "percentual":
        return porcentagem_emocao