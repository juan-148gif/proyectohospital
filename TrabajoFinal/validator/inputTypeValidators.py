def strinValidator(string,element):
    if string=="" or string==None:
        raise Exception(element + " no tiene un valor valido")
    

def integerValidator(string,element):
    strinValidator(string,element)
    try:
        return int(string)
    except:
        raise Exception(element + " no es un numero valido")