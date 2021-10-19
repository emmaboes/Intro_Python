import openpyxl
print("Abriendo libro...")

#Carga archivo 
wb=openpyxl.load_workbook("censuspopdata.xlsx")

sheet = wb["Population by Census Tract"]
print("Leyendo filas...")

datos_censo ={} #Iniciamos un diccionario vacio FUERA DEL FOR

# Se hace contador
for fila in range(2, sheet.max_row + 1) 
    fila_str = str(fila) 
    estado = sheet["B"+ fila_str].value
    condado = sheet["C" + fila_str].value
    poblacion = sheet["D" + fila_str].value

    datos_censo.setdefault(estado,{}) #Si no existe el estado, crea un diccionario vacio
    datos_censo[estado].setdefault(condado,{"tramos":0, "poblacion":0}) 
    datos_censo[estado][condado]["tramos"]+=1 #por cada ciclo for se suma un num.
    datos_censo[estado][condado]["poblacion"]+= int(poblacion)

  
california=datos_censo["CA"]

# Se cuantifica la población  del condado
for condado in california:
    poblacion_california += california[condado]["poblacion"] 
    print("La población de", condado, "es de", california[condado]["poblacion"], "personas")

print("La población total de california es de", poblacion_california , "personas")
