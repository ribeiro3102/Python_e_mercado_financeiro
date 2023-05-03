import statistics as st

def risco(a):
    if(a <= -0,5):
        return 'Risco alto'
    elif(a > -0.5)and(a <= 0.5):
        return 'Risco neutro'
    else:
        return 'Risco Baixo'

def media(lista):
        x = st.mean(lista)
        return x

def desvio(lista):
    y = st.pstdev(lista)
    return y