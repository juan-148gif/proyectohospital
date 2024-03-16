from models import model
from service import login 
from validator import personInputValidator

hospital=model.Hospital()
person=model.Person("admin",1234,"qwert@tdea.edu",3021243212,"admin","admin","admin","2344",1324)
hospital.persons.append(person)


def createDoctor():
    personInputValidator.createUser(hospital,"Doctor")

def createNurses():
    personInputValidator.createUser(hospital,"Nurse")

def createPatient():
    personInputValidator.createPatient(hospital)

def createMedicalConsultation(user):
    personInputValidator.createMedicalConsultation(hospital,user)

def createNurseVisit(user):
    personInputValidator.createNurseVisit(hospital,user)  #se modifico  

def createadminPersonal():
    personInputValidator.createUser(hospital,"Personal administrativo")


def adminMenu(user):
    option = input(" 1. Crear Doctor \n 2. Crear enfermero/a \n 3. Crear Personal administrativo \n 4. Cerrar sesion \n")
    if option=="1":
        createDoctor()
    if option=="2":
        createNurses()
    if option=="3":
        createadminPersonal()
    if option=="4":
        print("Cerrando sesion \n")
        return
    
def personalMenu(user):
    option = input(" 1. Crear Paciente \n 2. Cerrar sesion \n")
    if option=="1":
        createPatient()
    if option=="2":
        print("Cerrando sesion \n")
        return


def hospitalMenu(user):
    while(True):
        option = input("1. Crear Historia clinica \n 2. Cerrar sesion \n")
        if option=="1":
            createMedicalConsultation(user)
        if option=="2":
            print("Cerrando sesion \n")
            return

def nurseMenu(user):
    print("Ha hecho login como Enfermero/a \n")

    while True:
        option = input("1. Registrar visita de paciente \n2. Cerrar sesión \n")

        if option == "1":
            createNurseVisit(user) #se modifico
        elif option == "2":
            print("Cerrando sesión \n")
            return


def loginRouter(user):
    if user.role=="admin":
        return adminMenu(user)
    if user.role=="Doctor":
        print("Ha iniciado sesion Doctor \n")
        return hospitalMenu(user)
    if user.role=="Nurse":
        print("Ha iniciado sesion Enfermera \n")
        return nurseMenu(user)
    if user.role=="Personal administrativo":
        print("Ha iniciado sesion Personal administrativo \n")
        return personalMenu(user)
    raise Exception("Rol invalido")

def loginFun():
    userName = input("Ingrese su usuario \n")
    password = input("Ingrese su contraseña \n")   
    user = login.login(hospital,userName,password)
    if user==None:
       raise Exception(" el usuario no existe")
    return loginRouter(user)


while True:
    option=input("1. iniciar sesion \n0. para finalizar la ejecucion \n ")
    if option =="1":
        try:
            loginFun()
        except Exception as error:
            print(str(error))
    if option =="0":
        print(" Se cierra el programa ")
        break