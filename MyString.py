from codecs import Codec

mail = """
Hi Jhon,

This is Nikhil Thanks to taking Interest in 
Python Learning Program.
Hope you enjoy the Course

Thanks and Regards,
Nikhil
"""
Course = "Python for Beginner"
another = Course[:]

first = "Jhon"
last = "Smith"

message = first + ' [' + last + '] is a Python developer. '
msg = f'{first} [{last}] is a Python developer.'

print(Course[0])
print(Course[-1])
print(Course[1:-1])
print(Course[:])
print(Course[0:5])

print(another)

print(mail)

print(message)

print(msg)

print('Size of Course String ' + str(len(Course)))

print(Course.upper())

print(Course.replace("Beginner", "Fresher"))
print(Course.replace("beginner", " Absolute Beginner"))  # Python is case sensitive  that why it will have no effect

print('Python' in Course)  # Find Python in Course String return boolean value



