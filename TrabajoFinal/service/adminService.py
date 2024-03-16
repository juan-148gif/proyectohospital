import models.model as model

def createUser(hospital,name,identification,mail,telephone,role,userName,password,street,birthdate):
    user=findUser(hospital,identification)
    if user:
        raise Exception("Ya existe el usuario con el documento ingresado")
    user = None
    if userName:
        user= findUserName(hospital,userName)
    if user:
        raise Exception("Ya existe el usuario con el nombre ingresado")
    person=model.Person(name,identification,mail,telephone,role,userName,password,street,birthdate)
    hospital.persons.append(person)


def findUserName(hospital,userName):
    print("buscando usuario por userName " + str(userName))
    for person in hospital.persons:
        if isinstance(person, model.Patient):
            print("aqui esta el problema")
            continue
        if userName == person.userName:
            return person
    return None


def findUser(hospital,identification):
    for person in hospital.persons:
        if identification == person.identification:
            return person
    return None