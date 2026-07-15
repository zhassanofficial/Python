#name = input("Enter your Good name :")
#print(f"Good Afternoon, My Good name is : {name} ")

letter = '''
        Dear <|Name|>
        You are selected!
        <|Date|>


        '''
print(letter.replace("<|Name|>", "Hassan").replace("<|Date|>" , "16 sep 2000"))

name = "This is zahid  Hassan"
print(name.find("  "))
print(name.replace("  " , " "))

print("\"Dear hassan, This python\' course is nice.Thanks!\"")