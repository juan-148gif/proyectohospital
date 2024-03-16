import service.adminService as adminService
import models.model as model

def createPatient(hospital,identification,name,birthdate,gender,street,telephone,mail):
    user=adminService.findUser(hospital,identification)
    if user:
        raise Exception("Ya existe el usuario con el documento ingresado")
    user = None
    if user:
        raise Exception("Ya existe el usuario con el nombre ingresado")
    person=model.Patient(identification,name,birthdate,gender,street,telephone,mail)
    hospital.patient.append(person)
    hospital.clinical_history[str(identification)]={}

def createMedicalConsultation(hospital, user, identification, motiveConsultation, symptomatology, diagnosis,
                                 procedure, procedureDetail, medicine, medicineDose, date):
    
    patient = findPatientbyId(hospital,identification)
    
    if patient is None:
        raise Exception("No existe un paciente con el ID proporcionado")

    new_clinical_history = {}
    new_clinical_history ["date"]=date
    new_clinical_history["doctor"] =user.identification
    new_clinical_history["motiveConsultation"]=motiveConsultation
    new_clinical_history["symtomatology"]=symptomatology
    new_clinical_history["diagnosis"]=diagnosis
    
    if procedure != "N/A":
        new_clinical_history["procedure"] = procedure
        new_clinical_history["procedureDetail"] = procedureDetail

    if medicine != "N/A":
        order = model.Order(len(hospital.orders), patient.identification, user.identification, medicine, date)
        hospital.orders.append(order)
        new_clinical_history["order"] = order.orderid
        new_clinical_history["medicine"] = medicine
        new_clinical_history["medicineDose"] = medicineDose

    print("Historia nueva:")
    print(new_clinical_history)

    
    if str(identification) not in hospital.clinical_history:
        hospital.clinical_history[str(identification)] = {}

    hospital.clinical_history[str(identification)][str(date)] = new_clinical_history

    print("Historia del paciente:")
    print(hospital.clinical_history[str(identification)])

    print("Historia del hospital:")
    print(hospital.clinical_history)


def findPatientbyId(hospital, identification):
    for patient in hospital.patient:
        if identification == patient.identification:
            return patient
    return None



   #de aca para abajo se modifico 

def createNurseVisit(hospital, user, identification, bloodPressure,temperature,pulse,oxygenLevel,medicine,procedure, procedureDetail, tests,
                     observation,date):
    
    patient = findPatientbyId(hospital,identification)
    
    if patient is None:
        raise Exception("No existe un paciente con el ID proporcionado")
    
    nurse_visit = {
        "date": date,
        "patient_id": patient.identification,
        "blood_pressure": bloodPressure,
        "temperature": temperature,
        "pulse": pulse,
        "oxygen_level": oxygenLevel,
        "medicine": medicine,
        "procedure": procedure,
        "procedure_detail": procedureDetail,
        "tests": tests,
        "observation": observation
    }

    # Agregar el registro al historial clínico del paciente
    if str(patient.identification) not in hospital.clinical_history:
        hospital.clinical_history[str(patient.identification)] = {}

    if str(date) not in hospital.clinical_history[str(patient.identification)]:
        hospital.clinical_history[str(patient.identification)][str(date)] = {}

    hospital.clinical_history[str(patient.identification)][str(date)]["nurse_visit"] = nurse_visit

    print("Registro de visita de enfermera creado exitosamente.")  

def findPatientbyId(hospital, identification):
    for patient in hospital.patient:
        if identification == patient.identification:
            return patient
    return None  
