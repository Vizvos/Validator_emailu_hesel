import re

def validuj_email(email):
    """ Ověří, zda je email v platném formátu """
    vzor = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(vzor, email) is not None

def validuj_heslo(heslo):
    """ Ověří, zda heslo splňuje pravidla:
        - Min. 8 znaků
        - Alespoň 1 velké písmeno
        - Alespoň 1 číslo
    """
    vzor = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.match(vzor, heslo) is not None

def validuj_delku(heslo):
    vzor = r'^.{8,}$'
    return re.match(vzor, heslo) is not None

def validuj_velke_pismeno(heslo):
    vzor = r'^(?=.*[A-Z])'
    return re.match(vzor, heslo) is not None