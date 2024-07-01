import functions as func

value = "y"
print(func.yesNoBooleanConverster(value))

value = "yes"
print(func.yesNoBooleanConverster(value))

value = "no"
print(func.yesNoBooleanConverster(value))

val1 = False
val = func.booleanYesNoConverter(val1)
print(val)

val2 = "D"
print("Move state:", func.moveQueueValueConverter(val2))

val2 = "C"
print("Move state:", func.moveQueueValueConverter(val2))

val2 = "P"
print("Move state:", func.moveQueueValueConverter(val2))
