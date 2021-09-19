from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesUnemi import *
from datetime import date
import time

# Procesos de las Opciones del Menu Mantenimiento
def carreras():
   borrarPantalla()
   validar = Valida()     
   gotoxy(29,2);print("MANTENIMIENTO DE CARRERAS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(13,5);print("Descripcion Carrera: ")
   des=validar.solo_letras("Ingrese la Carrera:","Error: Solo Letra",25,5)
   archiCarrera = Archivo("carrera.txt",";")
   carreras = archiCarrera.leer()
   if carreras : idSig = int(carreras[-1][0])+1
   else: idSig=1
   carrera = Carrera(idSig,des)
   datos = carrera.getCarrera()
   datos = ';'.join(datos)
   archiCarrera.escribir([datos],"a")

def materias():
    borrarPantalla()
    validar = Valida()
    gotoxy(28,2);print("MANTENIMIENTO DE MATERIAS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(12,5);print("Descripcion MATERIAS: ")
    des=validar.solo_letras("Ingrese la materia:","Error: Solo Letra",25,5)
    archiMateria = Archivo("Materia.txt",";")
    materias = archiMateria.leer()
    if materias : idSig = int(materias[-1][0])+1
    else: idSig=1
    materia = Materia(idSig,des)
    datos = materia.getMateria()
    datos = ';'.join(datos)
    archiMateria.escribir([datos],"a")

def periodos():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE PERIODO")
   gotoxy(15,4);print("Periodo: ")
   gotoxy(15,5);print("Descripcion : ")
   per=validar.solo_numeros("Error: Solo numeros",25,4)
   gotoxy(28,5);des = input()
   archiPeriodo = Archivo("periodo.txt",";")
   periodo = archiPeriodo.leer()
   periodo = Periodo(per,des)
   datos = periodo.getPeriodo()
   datos = ';'.join(datos)
   archiPeriodo.escribir([datos],"a")                 
   gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
      

def profesores():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula: : ")
   gotoxy(15,6);print("Titulo: : ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   nom=validar.solo_letras("Ingrese el Nombre:","Error: Solo Letra",25,4)
   ced=validar.cedula("Error: Solo numeros de Cedula",25,5)
   gotoxy(25,6);tit = input()
   tel=validar.solo_numeros("Error: Solo numeros",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(33,8);print(entCarrera.descripcion)
          archiProfesor = Archivo("./profesor.txt",";")
          lisProfesores = archiProfesor.leer()
          if lisProfesores : idSig = int(lisProfesores[-1][0])+1
          else: idSig=1
          entProfesor = Profesor(idSig,nom,ced,tit,tel)
          datos = entProfesor.getProfesor()
          datos = ';'.join(datos)
          archiProfesor.escribir([datos],"a")                 
          gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
      else:
          gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")
       
def estudiantes():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE Estudiante")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula: : ")
   gotoxy(15,6);print("Dirección: :")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   nom=validar.solo_letras("Ingrese el Nombre:","Error: Solo Letra",25,4)
   ced=validar.cedula("Error: Solo numeros de Cedula",25,5)
   dir=validar.solo_letras("Su Dirección:","Error: Solo Letra",25,6)
   tel=validar.solo_numeros("Error: Solo numeros",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(33,8);print(entCarrera.descripcion)
          archiEstudiante = Archivo("./estudiante.txt",";")
          lisEstudiante = archiEstudiante.leer()
          if lisEstudiante : idSig = int(lisEstudiante[-1][0])+1
          else: idSig=1
          entEstudiante = Estudiante(idSig,nom,ced,dir,tel)
          datos = entEstudiante.getEstudiante()
          datos = ';'.join(datos)
          archiEstudiante.escribir([datos],"a")                 
          gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
      else:
          gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")

def matriculas():
    borrarPantalla()
    validar = Valida()
    gotoxy(20,2);print("INGRESO DE MATRICULA")
    gotoxy(15,4);print("Valor: ")
    gotoxy(15,5);print("Estudiante ID[    ]: ")
    gotoxy(15,6);print("Carrera ID   [    ]: ")
    gotoxy(15,7);print("Periodo ID   [    ]: ")
    valor = validar.solo_numeros("Error: Solo numeros",23,4)
    lisEstudiante, entEstudiante = [], None
    while not lisEstudiante:
        gotoxy(31,5);id = input().upper()
        archiEstudiante = Archivo("estudiante.txt")
        lisEstudiante = archiEstudiante.buscar(id)
        if lisEstudiante:
            entEstudiante = Estudiante(lisEstudiante[0], lisEstudiante[1], lisEstudiante[2], lisEstudiante[3], lisEstudiante[4])
            gotoxy(35,5);print(entEstudiante.nombre)
        else:
            gotoxy(35,5);print("No existe Estudiante con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(39,5);print(" "*55) 
    lisCarrera, entCarrera = [], None
    while not lisCarrera:
        gotoxy(31,6);id = input().upper()
        archiCarrera = Archivo("carrera.txt")
        lisCarrera = archiCarrera.buscar(id)
        if lisCarrera:
            entCarrera = Carrera(lisCarrera[0], lisCarrera[1])
            gotoxy(35,6);print(entCarrera.descripcion)
        else:
            gotoxy(35,6);print("No existe Carrera con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(39,6);print(" "*55) 
    lisPeriodo, entPeriodo = [], None
    while not lisPeriodo:
        gotoxy(31,7);id = input().upper()
        archiPeriodo = Archivo("periodo.txt")
        lisPeriodo = archiPeriodo.buscar(id)
        if lisPeriodo:
            entPeriodo = Periodo(lisPeriodo[0], lisPeriodo[1])
            gotoxy(35,7);print(entPeriodo.periodo)
        else:
            gotoxy(35,7);
            print("No existe Periodo con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(39,7);print(" "*55) 
    gotoxy(23,10);grabar = input().lower()
    if grabar == "s":
        archiMatricula = Archivo("matricula.txt")
        lisMatricula = archiMatricula.leer()
        if lisMatricula:
            idSig = int(lisMatricula[-1][0]) + 1
        else:
            idSig = 1
        entMatricula = Matricula(idSig,entEstudiante,entCarrera,entPeriodo,valor)
        datos = entMatricula.getMatricula()
        datos = ';'.join(datos)
        archiMatricula.escribir([datos], "a")
        gotoxy(15,9);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(15,9);input("Registro No fue Grabado\n presione una tecla para continuar...")

def notas():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE MATRICULA")
   gotoxy(15,4);print("Periodo    ID: [  ] ")
   gotoxy(15,5);print("Estudiante ID: [  ]")
   gotoxy(15,6);print("Materia    ID: [  ]")
   gotoxy(15,7);print("Profesor   ID: [  ]")
   gotoxy(15,8);print("Primer Nota:")
   gotoxy(15,9);print("Primer Segunda:")
   gotoxy(15,10);print("     ID[    ]: ")
   n1=validar.solo_numeros("Error: Solo numeros",32,8)
   n2=validar.solo_numeros("Error: Solo numeros",32,9)
   lisPeriodo,entPeriodo = [],None
   while not lisPeriodo:
      gotoxy(32,4);id = input().upper()
      archiPeriodo = Archivo("periodo.txt")
      lisPeriodo = archiPeriodo.buscar(id)
      if lisPeriodo:
          entPeriodo = Periodo(lisPeriodo[0],lisPeriodo[1]) 
          gotoxy(35,4);print(entPeriodo.descripcion)
      else: 
         gotoxy(33,4);print("No existe Periodo con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(39,4);print(" "*55)          
   lisEstudiante,entEstudiante = [],None
   while not lisEstudiante:
      gotoxy(32,5);id = input().upper()
      archiEstudiante = Archivo("./estudiante.txt")
      lisEstudiante = archiEstudiante.buscar(id)
      if lisEstudiante:
          entEstudiante = Estudiante(lisEstudiante[0],lisEstudiante[1],lisEstudiante[2],lisEstudiante[3],lisEstudiante[4]) 
          gotoxy(35,5);print(entEstudiante.nombre)
      else: 
         gotoxy(39,5);print("No existe Estudiante con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(39,5);print(" "*55)
   lisMateria,entMateria = [],None
   while not lisMateria:
      gotoxy(32,6);id = input().upper()
      archiMateria = Archivo("Materia.txt")
      lisMateria = archiMateria.buscar(id)
      if lisMateria:
          entMateria = Materia(lisMateria[0],lisMateria[1]) 
          gotoxy(35,6);print(entMateria.descripcion)
      else: 
         gotoxy(33,6);print("No existe Materia con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(39,6);print(" "*55)
   lisProfesores,entProfesores = [],None
   while not lisProfesores:
      gotoxy(32,7);id = input().upper()
      archiProfesores = Archivo("profesor.txt")
      lisProfesores = archiProfesores.buscar(id)
      if lisProfesores:
          entProfesores = Profesor(lisProfesores[0],lisProfesores[1],lisProfesores[2],lisProfesores[3],lisProfesores[4]) 
          gotoxy(35,7);print(entProfesores.nombre)
      else: 
         gotoxy(33,7);print("No existe Profesor con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(39,7);print(" "*55)
   gotoxy(24,10);grabar = input().lower()
   if grabar == "s":
        archiNotas = Archivo("notas.txt")
        lisNotas = archiNotas.leer()
        if lisNotas:
            idSig = int(lisNotas[-1][0]) + 1
        else:
            idSig = 1
        entNotas = Notas(idSig,entPeriodo,entEstudiante,entMateria,entProfesores,n1,n1)
        datos = entNotas.getNotas()
        datos = ';'.join(datos)
        archiNotas.escribir([datos], "a")
        gotoxy(15, 11);
        input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
        gotoxy(15, 11);
        input("Registro No fue Grabado\n presione una tecla para continuar...")
                
# Menu Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Matriculacion","3) Notas","4) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='6':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Carrera","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                carreras()
            elif opc1 == "2":
                materias()
            elif opc1 == "3":
                periodos()        
            elif opc1 == "4":
                profesores()
            elif opc1 == "5":
                estudiantes()
                                 
    elif opc == "2":
        opc2 = ' '
        while opc2 !=2:
            borrarPantalla()
            menu2 = Menu("Menu Matriculacion",["1) Matricula","2) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                matriculas()
            else: opc2 != "2"
                
    elif opc == "3":
        opc3 = ' '
        while opc3 !=2:
            borrarPantalla()
            menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                notas()
            else: opc3 != "2"
            input("Presione una tecla para salir")
    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

