class Person():
    def __init__(self,name,identification,mail,telephone,role,userName,password,street,birthdate):
        self.name=name
        self.identification=identification
        self.mail=mail
        self.telephone=telephone
        self.role=role
        self.userName=userName
        self.password=password
        self.birthdate=birthdate
        self.street=street

class Patient():
    def __init__(self,identification,name,birthdate,gender,street,telephone,mail):
        self.identification=identification
        self.name=name
        self.birthdate=birthdate
        self.gender=gender
        self.street=street
        self.telephone=telephone
        self.mail=mail

class Hospital():
    def __init__(self):
        self.persons=[]
        self.patient=[]
        self.orders=[]
        self.clinical_history={}
        self.nurse_visits = {} #se agrego
        
class ClinicalHistory():
    def __init__(self, patient, date, motiveConsultation, symptomatology, diagnosis, procedure, procedureDetail, medicine, medicineDose):
        self.patient = patient
        self.date = date
        self.motiveConsultation = motiveConsultation
        self.symptomatology = symptomatology
        self.diagnosis = diagnosis
        self.procedure = procedure
        self.procedureDetail = procedureDetail
        self.medicine = medicine
        self.medicineDose = medicineDose
        

class Order():
    def __init__(self, orderid, patientIdentification, userIdentification, medicine, date):
        self.orderid = orderid
        self.patientIdentification = patientIdentification
        self.userIdentification = userIdentification
        self.medicine = medicine
        self.date = date





















