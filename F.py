import re
def EmailValidateFunction(Text) : 
    if re.match("^[_.0-9]+$",Text[0]) : 
        return False 
    elif re.match("^[A-z0-9_.]+@+[A-z]+[.]+[A-z]+$",Text) : 
        return True 
    else : 
        return False
def UserValidateFunction(Text) : 
    Text = Text.strip() 
    if re.match("^[_.]+$",Text[0]) : 
        return False 
    if re.match("^[A-z0-9_.]+$",Text) : 
        return True 
    else : 
        return False
def TextValidateFunction(Text) : 
    Text = Text.strip() 
    if re.match("^[A-z \s]+$",Text) : 
        return True 
    else : 
        return False
def PswValidateFunction(Text) : 
    Out = 0 
    if re.search("[a-z]",Text) : 
        Out += 1 
    if re.search("[A-Z]",Text) : 
        Out += 1 
    if re.search("[0-9]",Text) : 
        Out += 1 
    if Out > 2 : return True 
    else : return False
