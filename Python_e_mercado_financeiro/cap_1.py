# 1.2 OPERAÇÕES SIMPLES NO CONSOLE
1+1
3/2
4-10
2**3
10 % 3

x=5
print(x)
y=10
print(y)
print(x,y)
print("x= ",x, "  y = ",y)
print(x+y)
print(x-y)
print(x/y)
print(x**y)

import math

math.exp(2)
math.log(10)
math.log2(3)
math.pow(2,3)
math.sqrt(16)
math.sin(3)
math.cos(3)
math.degrees(3.14)

import math as mt
mt.cos(3)
mt.log(2)

# 1.3 LISTAS NO CONSOLE
dados = [10,5,1,1,2,2,3,5,10,2,2,1,3,4,4]
print(dados[0])
print(dados[-1])
print(len(dados))

mercado = ['ações', 'opções','futuro','dolar','ouro','criptomoedas']
print(mercado)
print(mercado[0:3])
print(mercado[2:5])

'futuro' in mercado
'ouro'in mercado
'indice' in mercado

fut = 'futuro' in mercado
print(" 'futuro' está na lista? ", fut)

mercado[2] = 'commodity'
print(mercado)

#para alterar mais de uma palavra, usa-se a noção de fatiamento
mercado[0:2] = ['tesouro','títulos']
print(mercado)

#adicionando elementos a uma lista (append)
mercado.append('comprar')
mercado.append('dolar')
print(mercado)

# contando repetições (count)
mercado.count('dolar')

# adicionando lista em lista (extend)
mercado.extend(['Petrobras','BB','Vale'])
print(mercado)

# ordenação de uma lista em ordem crescente (se temos nomes com letras maiúsculas, o Python leva em 
# conta na separação entre letras o tamanho das letras e ordena separadamente)
mercado.sort()
print(mercado)

# se desejamos colocar em ordem independente do tamanho da fonte ou palavra inicial, devemos usar uma 
# chave (key) que deve igualar ao comando de string válido para todos os casos de letras: str.casefold
mercado.sort(key=str.casefold)
print(mercado)

# ordenando em ordem inversa (reverse)
mercado.reverse()
print(mercado)

# removendo elementos da lista (remove)
mercado.remove('ouro')
print(mercado)

# descobrindo o índice dos elementos (index)
mercado.index('Petrobras')
mercado.index('criptomoedas')

# inserindo elementos em uma posição desejada (insert)
mercado.insert(2, 'Fundo de Investimento')
print(mercado)

# limpando a lista toda (clear)
mercado.clear()
print(mercado)

# 1.4 OPERAÇÕES COM ELEMENTOS DAS LISTAS NO CONSOLE
ibov = ['PETR4', 'BBAS3','USIM5','GGBR4','VALE3']
# do elemento de índice 2 ao índice 3
ibov[2:4]
# do elemento de índice 1 até o último
ibov[1:]
# do elemento de inicial (índice 0) ao elemento de índice 2
ibov[:3]
# do elemento inicial ao último, saltando de 2 em 2
ibov[0:5:2]
# seleciona os 3 últimos da lista
ibov[-3:]
# seleciona os dois primeiros elementos da lista (pois é -(3 -1))
ibov[:-3]

# 1.5 ESTATÍSTICA BÁSICA DE CONSOLE
import statistics as st
prec = [10,11,11,10,10,10,8,8,9,7,11,12,13,8,9]
print(prec)

# Média (mean)
st.mean(prec)
# Mediana (median)
st.median(prec)
# Moda (mode)
st.mode(prec)
# Desvio padrão (stdev)
st.stdev(prec)
# desvio padrão populacional (pstdev)
st.pstdev(prec)

# 1.6 BIBLIOTECAS CIENTÍFICAS NO CONSOLE
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,20)
y=3*x-3
plt.plot(x,y)
plt.show()

# 1.7 ARQUIVOS DE TIPO TEXTO NO CONSOLE
x = [3,2,1]
f = open('dad.txt','w')
f.write('%d %d %d\n' % (x[0], x[1],x[2]))
f.close()

f = open("dad.txt",'r')
y=f.read()
print(y)
f.close()

# 1.8 ARQUIVOS EXCEL NO CONSOLE
import xlrd as excel
caminho = "dados/dados_1.xlsx"
arq=excel.load_workbook(caminho)
plan = arq['Planilha1']
x=plan['A1'].value
print(x)
