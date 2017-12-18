print("Textoor, a simple text reader")
read_permit = input("Read a text?(y?)")

if read_permit == "y": #This is the reading section
    try:
        file_name = str(input("Name and directory?"))
        print("-----------------------------------")
        print("Textoor Reader                    |")
        print("-----------------------------------")
        reading = open(file_name,"r")
        print(reading.read())
        print("Finished reading")
        reading.close()
    except NameError:
        print("ups!")
    except FileNotFoundError:
        print("File tidak ada")
    except PermissionError:
        print("Permission Denied")
    except UnicodeDecodeError:
        print("Cannot read the file")
    finally:
        print("Done")

else: 
    print("I don't understand")
    
#Textoor is just an experiment
#The initial feature is reading a file, i will add new feature to it later
