while True:
  print ("-----------------------------------------")
  print ("Ohm's Calculator")
  print ("A next implementation of previous code")
  print ("Brought to you by Kurdgeon")
  print ("Usage:")
  print ("R => Ohm")
  print ("I => Ampere")
  print ("V => Volt")
  print ("Keluar? q")
  user_input = input("=>")
  
  if user_input == "q":
    break
  elif user_input == "r":
    num1 = float(input("Volt?"))
    num2 = float(input("Ampere?"))
    hasil = str(num1 / num2)
    print("Hasilnya = " + hasil)
  elif user_input == "i":
    num1 = float(input("Volt?"))
    num2 = float(input("Ohm?"))
    hasil = str(num1 / num2)
    print("Hasilnya = " + hasil)
  elif user_input == "v":
    num1 = float(input("Ampere?"))
    num2 = float(input("Ohm?"))
    hasil = str(num1 * num2)
    print("Hasilnya = " + hasil)
  else:
    print("Unknown command")
