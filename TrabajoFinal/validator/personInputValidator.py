import validator.inputTypeValidators as inputTypeValidators
import service.adminService as adminService
import service.administrationService as administrationService
import datetime

def createUser(hospital,role):
    name=input("Ingrese el nombre del usuario \n")
    inputTypeValidators.strinValidator(name,"nombre del usuario \n")
    identification=inputTypeValidators.integerValidator(input("Ingrese el documento del usuario \n"),"cedula del usuario \n")
    mail=input("Ingrese el correo del usuario \n")
    inputTypeValidators.strinValidator(mail,"correo del usuario \n")
    telephone=inputTypeValidators.integerValidator(input("Ingrese el numero de contacto del usuario \n"),"movil del usuario \n")
    userName=input("Ingrese el usuario \n")
    inputTypeValidators.strinValidator(userName, "Nombre del usuario \n")
    password=input("Ingrese la contraseña del usuario \n")
    inputTypeValidators.strinValidator(password, "contraseña \n")
    birthdate=input("Ingrese la fecha de nacimiento del usuario \n")
    inputTypeValidators.strinValidator(birthdate,"fecha de nacimiento \n")
    street=input("Ingrese la direccion del usuario \n")
    inputTypeValidators.strinValidator(street,"direccion del usuario \n")
    print("Se pasaron las validaciones")
    adminService.createUser(hospital,name,identification,mail,telephone,role,userName,password,street,birthdate)

def createPatient(hospital):
    identification=inputTypeValidators.integerValidator(input("Ingrese el documento del Paciente \n"),"cedula del Paciente \n")
    name=input("Ingrese el nombre del Paciente \n")
    inputTypeValidators.strinValidator(name,"nombre del Paciente \n")
    birthdate=input("Ingrese la fecha de nacimiento del Paciente \n")
    inputTypeValidators.strinValidator(birthdate,"fecha de nacimiento del Paciente \n")
    gender=input("Ingrese el genero del Paciente \n")
    inputTypeValidators.strinValidator(gender,"genero del Paciente \n")
    street=input("Ingrese la direccion del Paciente \n")
    inputTypeValidators.strinValidator(street,"direccion del Paciente \n")
    telephone=inputTypeValidators.integerValidator(input("Ingrese el numero de contacto del Paciente \n"),"movil del Paciente \n")
    mail=input("Ingrese el correo del Paciente \n")
    inputTypeValidators.strinValidator(mail,"correo del Paciente \n")
    print("Se pasaron las validaciones")
    administrationService.createPatient(hospital,identification,name,birthdate,gender,street,telephone,mail)

def createMedicalConsultation(hospital,user):
    date= datetime.datetime.today()
    print(date)
    identification=inputTypeValidators.integerValidator(input("Ingrese el documento del usuario \n"),"cedula del usuario \n")
    motiveConsultation=input("Ingrese el motivo de la consulta \n")
    inputTypeValidators.strinValidator(motiveConsultation,"Consulta realizada \n")
    symptomatoly=input("Ingrese el diagnostico registrado \n")
    inputTypeValidators.strinValidator(symptomatoly,"sinmatologia \n")
    diagnosis=input("Ingrese el dianostico del usuario \n")
    inputTypeValidators.strinValidator(diagnosis,"Diagnostico realizado \n")
    symptomatology=input("Ingrese los sintomas del usuario \n")
    inputTypeValidators.strinValidator(symptomatology,"Sintomas agregados \n")
    procedure=input("Ingrese el procedimiento del usuario \n")
    inputTypeValidators.strinValidator(procedure,"Procedimiento agregado \n")
    procedureDetail=input("Ingrese el detalle del procedimiento del usuario \n")
    inputTypeValidators.strinValidator(procedureDetail,"Detalle guardado \n")
    medicine=input("Ingrese la medicina para el usuario \n")
    inputTypeValidators.strinValidator(medicine,"Medicina registrada \n")
    medicineDose=input("Ingrese el detalle de la dosis de la medicina del usuario \n")
    inputTypeValidators.strinValidator(medicineDose,"Diagnostico de medicina realizado \n")

    
    administrationService.createMedicalConsultation(hospital,user,identification,date, motiveConsultation, symptomatology, diagnosis, procedure, procedureDetail, medicine, medicineDose)

#se creo createNurseVisi abajo

def createNurseVisit(hospital, user):
    identification=inputTypeValidators.integerValidator(input("Ingrese el documento del usuario \n"),"cedula del usuario \n")
    bloodPressure=input("Ingrese la apresion \n")
    inputTypeValidators.strinValidator(bloodPressure,"presion realizada \n")
    temperature=input("Ingrese temperatura \n")
    inputTypeValidators.strinValidator(temperature,"temperatura registrada \n")
    pulse=input("Ingrese el pulso del usuario \n")
    inputTypeValidators.strinValidator(pulse,"Pulso realizado \n")
    oxygenLevel=input("Ingrese oxigeno del usuario \n")
    inputTypeValidators.strinValidator(oxygenLevel,"Oxigeno agregados \n")
    procedure=input("Ingrese el procedimiento realizado \n")
    inputTypeValidators.strinValidator(procedure,"Procedimiento agregado \n")
    procedureDetail=input("Ingrese el detalle del procedimiento al  usuario \n")
    inputTypeValidators.strinValidator(procedureDetail,"Detalle guardado \n")
    medicine=input("Ingrese la medicina suministrada al usuario \n")
    inputTypeValidators.strinValidator(medicine,"Medicina registrada \n")
    medicineDose=input("Ingrese el detalle de la dosis de la medicina del usuario \n")
    inputTypeValidators.strinValidator(medicineDose,"Diagnostico de medicina realizado \n")
    tests=input("Ingrese las pruebas realizadas \n")
    inputTypeValidators.strinValidator(tests,"prueba registrada\n")
    observation=input("Observacion del usuario \n")
    inputTypeValidators.strinValidator(observation,"observacion realizado \n")
    date=input("dato del usuario \n")
    inputTypeValidators.strinValidator(date,"dato realizado \n")


    administrationService.createNurseVisit(hospital, user, identification, bloodPressure,temperature,pulse,oxygenLevel,medicine,procedure, procedureDetail, tests,
                     observation,date)