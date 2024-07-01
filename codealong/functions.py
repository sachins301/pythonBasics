def yesNoBooleanConverster(val):
    val = str(val).upper()
    if val == "Y" or val == "YES":
        return True
    else:
        return False


def booleanYesNoConverter(val):
    if val:
        return "Yes"
    return "No"


# null
def nullToBooleanConverter(value):
    return value != None


def moveQueueValueConverter(val):
    val = str(val).upper()
    if val == "R":
        return "Released"
    elif val == "H":
        return "Hold"
    elif val == "D":
        return "Deleted"
    elif val == "P":
        return "Pending"
    else:
        return None
