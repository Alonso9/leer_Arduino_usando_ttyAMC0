import mysql.connector #importamos el modulo para conectar con mysql 
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


def main():

    #Creamos una conexion con los datos del servidor y DDBB
    conn = mysql.connector.connect(host='localhost',user='root',passwd='',database='PI3')
    cursor = conn.cursor()

    cont = 0

    while cont < 10:

        ser1 = serial.Serial('/dev/ttyACM0',9600)
        #ser2 = serial.Serial('/dev/ttyACM1',9600)
        
        getval = ser1.readline()
        temp = datos(str(getval))
        print(f"Tu temperatura es: {temp} y tipo: {type(temp)}")
        cont+=1

        query = "INSERT INTO `tabla01`(`sensor_data`) VALUES (%s)"%(temp) #query para insertar datos en la tabla
        cursor.execute(query) #ejecutamos
        conn.commit()
        print(f"Se han insertado {cursor.rowcount} dato en la BD")
        
    conn.close() #Cerramos la conexion
    
main()

