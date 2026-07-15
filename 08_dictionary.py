student = {
    "key" : "value",
    "name" : "zahid",
    "course":"python",
    "is_active": True

}
student["course"] = "PYTHON"
student["subject"] = "SE"

print(student)
for key , value in student.items():
    print(key , value)
#print(student.keys())
#print(student.values())
print(student.items())

#student.update({"is_active" : False})
#print(student)

#print(student.get("key1"))  # return none
#print(student["key1"])     # return error