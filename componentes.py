from helpers import borrarPantalla, gotoxy
import time
class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones))) 
        return opc   

class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*20)
        return valor

    def solo_letras(self,mensaje,mensajeError,col,fil): 
        while True:
            gotoxy(col,fil) 
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
                time.sleep(1)
                gotoxy(col,fil);print(" "*20)
        return valor

    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor
    
    def cedula(self,mensajeError,col,fil):
        
        while True:
            gotoxy(col,fil) 
            ced = input()
            suma = 0
            for i in range(len(ced)-1):
                x = int(ced[i])
                if i%2 == 0:
                    x = x*2
                    if x > 9:
                        x = x - 9
                suma = suma + x
            if suma%10 != 0:
                result = 10 -(suma%10)
            try:
                if int(ced[-1]) == result:
                    break 
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*29)
        return ced                   
    
class otra:
    pass    

