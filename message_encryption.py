#al014
#78093 Goncalo Santos
#78854 Andre Aguas
#79112 Goncalo Fialho


def encripta (N,i,j):
    """
    encripta: int x int x int-->int
    encripta(N,i,j) recebe a mensagem original e dois numeros inteiros, e 
    devolve a mensagem encriptada
    """
    m=calcula_m(i,j)
    n=calcula_n(i,j)
    e=calcula_e(n)
    if N >= m:
        raise ValueError('encripta: a mensagem tem de ser inferior a '+str(m))  
    C = N ** e % m
    return C      

    
def decifra (C,i,j):
    """
    encripta: int x int x int-->int
    encripta(N,i,j) recebe a mensagem encriptada e dois numeros inteiros, e 
    devolve a mensagem encriptada
    """    
    m=calcula_m(i,j)
    n=calcula_n(i,j)    
    e=calcula_e(n)
    d=calcula_d(e,n)
    if C >= m:
        raise ValueError('decifra: a mensagem tem de ser inferior a ' +str(m))    
    N = C ** d % m
    return N


def n_esimo_primo(n):
    """
    n_esimo_primo: int--> int
    n_esimo_primo(n) recebe um inteiro positivo e devolve o primo
    correspondente a esse inteiro
    """
    divisor = 2
    conta = 0
    while conta < n:
        if e_primo(divisor):
            conta = conta + 1
        divisor = divisor + 1
    return (divisor-1)


def calcula_m(i,j):
    """
    calcula_m: int x int--> int
    calcula_m(i,j): recebe dois numeros primos e devolve a variavel 'm'
    """    
    p = n_esimo_primo(i)
    q = n_esimo_primo(j)
    m = p * q  
    return m

def calcula_n(i,j):
    """
    calcula_n: int x int--> int
    calcula_m(i,j): recebe dois numeros primos e devolve a variavel 'n'
    """
    p = n_esimo_primo(i)
    q = n_esimo_primo(j)    
    n = (p - 1) * (q - 1)
    return n


def calcula_e(n):
    """
    calcula_e: int--> int
    calcula_e(n) recebe 'n' e devolve o valor da variavel 'e'
    """
    e=2
    while mdc(n,e) != 1:
        e = e + 1
    return e

         
def calcula_d(e,n):
    """
    calcula_d: int x int--> int
    calcula_d(e,n) recebe 'e' e 'n', e devolve o valor da variavel 'd'
    """
    k = 1
    d = (1 + k * n)/(e)
    while int(d) != d:
        k = k + 1
        d = (1 + k * n)/(e)
    return int(d)
#neste caso retornamos int(d) pois d e um float, desta forma transformamo-lo
#em int


def e_primo(n):
    """
    e_primo: int--> bool
    e_primo(n) recebe um inteiro positivo e verifica se e primo
    """
    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            return False
        divisor = divisor + 1
    return True


def mdc(n,e):
    """
    mdc: int x int--> int
    mdc(n,e) recebe 'n' e 'e' e devolve o seu maximo divisor comum
    """
    while e != 0:
        n, e = e, n % e
    return n
