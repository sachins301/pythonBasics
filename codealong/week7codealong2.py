class SimpleClass:
    pass

class YesNoBooleanValueConverter:

    def convert(self, val):
        val = str(val).upper()
        if val == "Y" or val == "YES":
            return True
        else:
            return False

    def convert_back(self, val):
        val = str(val).upper()
        if val == "Y" or val == "YES":
            return True
        else:
            return False

class Student:

    first_name = ""
    last_name = ""
    is_graduated = False

student_a = Student()
student_a.first_name = "Sachin"
student_a.last_name = "Sudheer"
student_a.is_graduated = True

vc = YesNoBooleanValueConverter()
grad_status = vc.convert(student_a.is_graduated)
print(grad_status)

grad_status1 = vc.convert_back("N")
print(student_a.first_name, student_a.last_name, "Is graduated: ", vc.convert(grad_status1))