filename = input("The Filename:")
parts = filename.split(".")
if len(parts)>1:
    extension = parts[-1]
    print("The Extension of the file is :",extension)
else:
    print("There is no Extension")    
    
    