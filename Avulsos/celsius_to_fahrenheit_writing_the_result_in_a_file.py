def celsius_to_fahrenheit(c):
  if(c<-273.15):
    return("It is impossible to have a temperature less than the absolute zero (0 F or -273.15 C)")
  f = c * 9/5 + 32
  return f
  
def enter_the_temperature():
  entrada = input("Enter the temperature in Celsius to show it in Fahrenheit")
  entrada_in_float = 0.0
  try:
    entrada_in_float = float(entrada)
    return entrada_in_float
  except ValueError:
  	return ("The temperature informed is invalid. Try again.")
    
    
#print(celsius_to_fahrenheit(enter_the_temperature()))


temperatures=[10,-20,-289,100]

def clean_the_file():
	with open("temperatures.txt","w") as file:
		file.write("")

clean_the_file()

def write_in_the_file(result):
	with open("temperatures.txt","a") as file:
		file.write(result+"\n")

for t in temperatures:
	f = celsius_to_fahrenheit(t)
	if(str(f)!="It is impossible to have a temperature less than the absolute zero (0 F or -273.15 C)"):
		write_in_the_file(str(f))
  #print(celsius_to_fahrenheit(t))





