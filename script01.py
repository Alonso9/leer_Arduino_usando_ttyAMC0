from time import sleep
import serial

def datos(x):

    res = 0
    var = []
    temp = 0.0
    for i in x:
        if i.isdigit() == 1:
            var.append(i)
    text = ''
    for element in var:
        text += element

    temp += float(text)/100
    return temp #DRetornamos el valor de la temperatura


cont = 0

while cont < 10:

	ser1 = serial.Serial('/dev/ttyACM0',9600)
	#ser2 = serial.Serial('/dev/ttyACM1',9600)
	
	getval = ser1.readline()
	temp = datos(str(getval))
	print(f"Tu temperatura es: {temp} y tipo: {type(temp)}")
	cont+=1