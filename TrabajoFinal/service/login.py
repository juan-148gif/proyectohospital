def passwordValidate(person,password):
    if person.password==password:
        return person
    raise Exception("La contraseña es incorrecta")

def login(hospital,userName,password):
    for person in hospital.persons:
        if person.userName==userName:
            return passwordValidate(person,password)
    return None