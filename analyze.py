def boolPassFail(shouldCheck,checkBool):
    if shouldCheck and checkBool:
        return True
    elif shouldCheck == False and checkBool:
        return True
    elif shouldCheck == checkBool:
        return True
    else:
        return False