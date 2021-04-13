
from tkinter import *

#Interfaz-------------------------------------------------------------------

fondoVivas=Tk()
fondoVivas.title("SUPER CALCULADORA saca cincos(5)")
fondoVivas.geometry("500x450")
fondoVivas.config(background="black")

bryanFrame=Frame(fondoVivas)
bryanFrame.pack()
bryanFrame.config(background="cyan")
bryanFrame.config(bd=18)
bryanFrame.config(relief="groove")


def fix_string(n):
       n = n.replace("(", "").replace(")", "").replace("'", "").replace(",", "")
       n = "".join(n.split(" "))
       return n


#Pantalla-------------------------------------------------------------------
valorScreen=StringVar()
valorScreen2=StringVar()
valorScreen3=StringVar()


screen=Entry(bryanFrame, textvariable=valorScreen, width=20, font=(5))
screen.grid(row=2, column=3) 
screen.config(background="white", fg="black", justify="right")

screen2=Entry(bryanFrame, textvariable=valorScreen2, width=20, font=(5))
screen2.grid(row=2, column=10) 
screen2.config(background="white", fg="black", justify="right")

screen3=Entry(bryanFrame, textvariable=valorScreen3, width=20, font=(5))
screen3.grid(row=9, column=10) 
screen3.config(background="white", fg="black", justify="right")

sistemas= Label(bryanFrame, text="ENTRADA 2")
sistemas.config(bd=5, bg="gray", fg="white", width=20, font=(5))
sistemas.config(relief="raised")
sistemas.grid(row=1, column=10)

sistemas= Label(bryanFrame, text="ENTRADA 1")
sistemas.config(bd=5, bg="gray", fg="white", width=20, font=(5))
sistemas.config(relief="raised")
sistemas.grid(row=1, column=3)

resp= Label(bryanFrame, text="RESPUESTA")
resp.config(bd=5, bg="gray", fg="white", width=20, font=(5))
resp.config(relief="raised")
resp.grid(row=8, column=10)
    
#Función general para conversión hexadecimal------------------------------------------------------------
def ConversorHex(caracter_hexad):
    equivalencias={
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    if caracter_hexad in equivalencias:
        return equivalencias[caracter_hexad]
    else:
        return int(caracter_hexad)


#Funciones de conversión para entrada 1--------------------------------------------------------

def DecBin(n):
    n =list(bin(int(n))[2:])
    valorScreen.set(n)
    
def HexBin(n):
    n = n.upper()
    n=n[::-1]
    decimal=0
    posicion=0
    for digito in n:
        valor=ConversorHex(digito);
        exp=16**posicion;
        igual=exp*valor;
        decimal += igual
        posicion += 1
    
    ress=[]
    while(decimal>=1):
        ress.append(decimal%2);
        decimal=int(decimal/2);
    sol=ress[::-1]
    valorScreen.set(sol)
    
def OctBin(n):
    decimal=0
    posicion=0
    n=n[::-1]
    for digito in n:
        entero=int(digito);
        exp=int(8**posicion);
        equivalencia=int(exp*entero)
        decimal+=equivalencia
        posicion+=1
    
    ress=[]
    while(decimal>=1):
        ress.append(decimal%2);
        decimal=int(decimal/2);
    sol=ress[::-1]
    valorScreen.set(sol)
    

#Funciones de conversión para entrada 2--------------------------------------------------------

def DecBin2(n):
    n =list(bin(int(n))[2:])
    valorScreen2.set(n)
    
def HexBin2(n):
    n = n.upper()
    n=n[::-1]
    decimal=0
    posicion=0
    for digito in n:
        valor=ConversorHex(digito);
        exp=16**posicion;
        igual=exp*valor;
        decimal += igual
        posicion += 1
    
    ress=[]
    while(decimal>=1):
        ress.append(decimal%2);
        decimal=int(decimal/2);
    sol=ress[::-1]
    valorScreen2.set(sol)
    
def OctBin2(n):
    decimal=0
    posicion=0
    n=n[::-1]
    for digito in n:
        entero=int(digito);
        exp=int(8**posicion);
        equivalencia=int(exp*entero)
        decimal+=equivalencia
        posicion+=1
    
    ress=[]
    while(decimal>=1):
        ress.append(decimal%2);
        decimal=int(decimal/2);
    sol=ress[::-1]
    valorScreen2.set(sol)


#Funciones para conversión de salida-----------------------------------------------------------
def BinDec(n):
    n = fix_string(n)
    n = int(n, base =2)
    valorScreen3.set(n)

def BinHex(n):
    n = fix_string(n)
    n = hex(int(n, base=2))[2:].upper()
    valorScreen3.set(n)
    
def BinOct(n):
    n = fix_string(n)
    n = oct(int(n, base=2))[2:]
    valorScreen3.set(n)  


#Complementos a 1 y a 2
def complementoa1(x):
    ca1 = ''
    for i in range (len(x)):
        if x[i] == '0':
            x[i] == '1'
            ca1 = ca1 + '1'
            
        else:
            x[i] == '1'
            x == x + '0'
            ca1 = ca1 + '0'
    return(ca1)

def complementoa2(x):
    y = '1'
    y = y.zfill(len(x))
    ca2 = suma_binaria(x,y)
    
    return(ca2)


#Funciones para las operaciones internas entre binarios------------------------------------------------
def suma_binaria(num_a, num_b):
    ''' zfill completa con ceros el número de menor tamaño '''
    if len(num_a) > len(num_b):
        num_b = num_b.zfill(len(num_a))
    else :
        num_a = num_a.zfill(len(num_b))        
    
    resultado = ""
    acarreo = "0"
    for i in range (len(num_a)-1, -1, -1):
        
        if num_a[i] == "0" and num_b[i] == "0" and acarreo == "0":
            resultado = "0" + resultado
            
        elif num_a[i] == "0" and num_b[i] == "0" and acarreo == "1":
            resultado = "1" + resultado
            acarreo = "0"
            
        elif num_a[i] == "0" and num_b[i] == "1" and acarreo == "0":
            resultado = "1" + resultado
            
        elif num_a[i] == "0" and num_b[i] == "1" and acarreo == "1":
            resultado = "0" + resultado
            acarreo = "1"
            
        elif num_a[i] == "1" and num_b[i] == "0" and acarreo == "0":
            resultado = "1" + resultado
            
        elif num_a[i] == "1" and num_b[i] == "0" and acarreo == "1":
            resultado = "0" + resultado
            acarreo = "1"
            
        elif num_a[i] == "1" and num_b[i] == "1" and acarreo == "0":
            resultado = "0" + resultado
            acarreo = "1"
            
        elif num_a[i] == "1" and num_b[i] == "1" and acarreo == "1":
            resultado = "1" + resultado
            acarreo = "1"
            
    if acarreo == "1":
        resultado = "1" + resultado       
    
    valorScreen3.set(resultado)
    return (resultado, acarreo)
    
def resta_binaria(num_a,num_b):
    
    if len(num_a) > len(num_b):
        num_b = num_b.zfill(len(num_a))
    else: 
        num_a = num_a.zfill(len(num_b))
        
    ca1 = complementoa1(num_b)
    
    resultado_temp, acarreo = suma_binaria(num_a, ca1)

    if acarreo == '1':
        resultado, acarreo_resta = complementoa2(resultado_temp[1:])
        
    
    if acarreo == '0':
        resultado = '-' + complementoa1(resultado_temp)
         
    valorScreen3.set(resultado)
    return (resultado)

def multipli_binaria(num_a,num_b):
    '''***
    -Funcion que determina el producto de dos numeros binarios(num_a X num_b).
    -Esta funcion necesita la funcion suma_binario para hacer las respectivas multiplicaciones. 
    
    Entradas:
    num_a: string
    num_b: string
    
    Esta funcion retorna el ultimo valor de la lista 'resultado'.
    :)
    ***'''
    vacio = ''   
    resultado = []
    for i in range (len(num_b)-1, -1, -1):     # Multiplicacion basica de ceros y unos 
        if num_b[i] == '0':                    # Condicon si multiplica por 0 
            multipli = vacio.zfill(len(num_a)) # Agregar ceros segun el tamaño de num_a
            resultado.append(multipli)         # El resultado se guarda en la lista 'resultado'
        if num_b[i] == '1':                    # Condicion si multiplica por 1
            multipli = num_a                   # Multiplicacion por uno devulve el mismo numero 
            resultado.append(multipli)         # El resultado se guarda en la lista 'resultado'

    for i in range (0,len(resultado),1):      # Completar ceros en cada parametro de la lista para sumarlos
        resultado[i] = resultado[i]+vacio.zfill(i)
        
    for i in range (0, len(resultado)-1,1):   # Se hacen las sumas del contenido de la lista'resultado'
        res_suma, acarreo = suma_binaria(resultado[i+1],resultado[i])
        resultado[i+1]=res_suma       
                       
    valorScreen3.set(resultado[-1])
    return (resultado[-1])  #retorna el ultimo valor de la lista

def division_binaria(num_a, num_b):
    resultado = ''
    residuo = ''
    
    if int(num_a) < int(num_b):
        resultado = '0'
        residuo = num_a
        
    if int(num_a) > int(num_b):
        num_a_temp = num_a[0:len(num_b)]
        
        for i in range (len(num_a) - len(num_b) + 1):
            if int(num_a_temp) >= int(num_b):
                resultado = resultado + '1'
                num_a_temp = resta_binaria(num_a_temp, num_b)
        
            else:
                resultado = resultado + '0' 
                residuo = num_a_temp
            if i + len(num_b) < len(num_a):
                num_a_temp = num_a_temp + num_a[i + len(num_b)]
            
    if num_a == num_b:
        resultado = '1'
    valorScreen3.set(resultado)
    return(resultado)

def pot_binaria(num_a, potencia):
    '''***
    -Funcion que multiplica el "num_a" segun la catidad de veces que le determinemos en "potencia".
    -Esta funcion necesita la funcion multipli_binario para hacer las respectivas potenciaciones.
    
    Entradas:
    num_a: string
    potencia: entero
    
    Esta funcion retorna:
    resultado: string
    ó
    num_a
    
    Salu2
    ***'''
    potencia=int(potencia)
    inicial = num_a                             #Inicalizar variable que me guarda cada operacion
    if potencia > 1:
        for i in range(1,potencia,1):               #Se define cuantas veces se va a multiplicar 
            resultado = multipli_binaria(inicial,num_a) # Multiplicacion
            inicial = resultado                      # Guardar la multiplicacion en la varible
    
    elif potencia == 0:
         resultado = '1'
    elif potencia == 1:
        resultado = num_a
     
    valorScreen3.set(resultado)
    return resultado                         #Para potencias mayores a 1 retorna resultado
    

#Bloque 3 de calculadora con signos-------------------------------------------
teclaSum=Button(bryanFrame, text="+",bg="black",fg="white", width=5, font=(10), command=lambda:suma_binaria(valorScreen.get(),valorScreen2.get()))
teclaSum.config(bd=5)
teclaSum.config(relief="raised")
teclaSum.grid(row=9, column=3)
teclaRes=Button(bryanFrame, text="-",bg="black",fg="white", width=5, font=(10), command=lambda:resta_binaria(valorScreen.get(),valorScreen2.get()))
teclaRes.config(bd=5)
teclaRes.config(relief="raised")
teclaRes.grid(row=10, column=3)
teclaMul=Button(bryanFrame, text="*",bg="black",fg="white", width=5, font=(10), command=lambda:multipli_binaria(valorScreen.get(),valorScreen2.get()))
teclaMul.config(bd=5)
teclaMul.config(relief="raised")
teclaMul.grid(row=11, column=3) 
teclaDiv=Button(bryanFrame, text="/",bg="black",fg="white", width=5, font=(10), command=lambda:division_binaria(valorScreen.get(),valorScreen2.get()))
teclaDiv.config(bd=5)
teclaDiv.config(relief="raised")
teclaDiv.grid(row=12, column=3) 
teclaPot=Button(bryanFrame, text="^",bg="black",fg="white", width=5, font=(10), command=lambda:pot_binaria(valorScreen.get(),valorScreen2.get()))
teclaPot.config(bd=5)
teclaPot.config(relief="raised")
teclaPot.grid(row=13, column=3) 

#Bloque 4 de calculadora con sistemas numéricos para entrada-------------------------------------------
teclaDec=Button(bryanFrame, text="DEC to BIN",bg="black",fg="white", width=10, font=(5), command=lambda:DecBin(valorScreen.get()))
teclaDec.config(bd=5)
teclaDec.config(relief="raised")
teclaDec.grid(row=4, column=3)
teclaHex=Button(bryanFrame, text="HEX to BIN",bg="black",fg="white", width=10, font=(5), command=lambda:HexBin(valorScreen.get()))
teclaHex.config(bd=5)
teclaHex.config(relief="raised")
teclaHex.grid(row=5, column=3) 
teclaOct=Button(bryanFrame, text="OCT to BIN",bg="black",fg="white", width=10, font=(5), command=lambda:OctBin(valorScreen.get()))
teclaOct.config(bd=5)
teclaOct.config(relief="raised")
teclaOct.grid(row=6, column=3)

#Bloque 4.2 de calculadora con sistemas numéricos para entrada-------------------------------------------
teclaDec2=Button(bryanFrame, text="DEC to BIN",bg="black",fg="white", width=13, font=(5), command=lambda:DecBin2(valorScreen2.get()))
teclaDec2.config(bd=5)
teclaDec2.config(relief="raised")
teclaDec2.grid(row=4, column=10)
teclaHex2=Button(bryanFrame, text="HEX to BIN",bg="black",fg="white", width=13, font=(5), command=lambda:HexBin2(valorScreen2.get()))
teclaHex2.config(bd=5)
teclaHex2.config(relief="raised")
teclaHex2.grid(row=5, column=10) 
teclaOct2=Button(bryanFrame, text="OCT to BIN",bg="black",fg="white", width=13, font=(5), command=lambda:OctBin2(valorScreen2.get()))
teclaOct2.config(bd=5)
teclaOct2.config(relief="raised")
teclaOct2.grid(row=6, column=10)

#Bloque 5 de calculadora con sistemas numéricos para salida-------------------------------------------
respDec=Button(bryanFrame, text="DECIMAL",bg="black",fg="white", width=13, font=(5), command=lambda:BinDec(valorScreen3.get()))
respDec.config(bd=5)
respDec.config(relief="raised")
respDec.grid(row=10, column=10)
respHex=Button(bryanFrame, text="HEXADECIMAL",bg="black",fg="white", width=13, font=(5),command = lambda: BinHex(valorScreen3.get()))
respHex.config(bd=5)
respHex.config(relief="raised")
respHex.grid(row=11, column=10)
respOct=Button(bryanFrame, text="OCTAL",bg="black",fg="white", width=13, font=(5), command = lambda: BinOct(valorScreen3.get()))
respOct.config(bd=5)
respOct.config(relief="raised")
respOct.grid(row=12, column=10)

fondoVivas.mainloop()

