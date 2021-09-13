
"""
Bienvenidos a mi código :D
Elaborado por: Alexa Mercado

"""
#Aquí se importan desde el archivo lifestore_file.py los 3 strings que usaremos
from lifestore_file import lifestore_products as LP
from lifestore_file import lifestore_sales as LSa
from lifestore_file import lifestore_searches as LSe

#Esta es una forma alterna de acomodar valores de una lista dependiendo si se quieren acomodados por máximos o mínimos. La forma en la que trabaja es la siguiente: 
#Por cada elemento de la lista, busca el máximo o mínimo, lo añade a otra lista (se llama sorteo) y la elimina de la lista inicial. Así siempre queda como resultado una lista inicial del máximo-1 o mínimo-1 y este proceso se repite b veces. En caso de que el índice de b sea mayor al de la lista de entrada, se hace append del string 'out of range'
""""
def sorteo(b,lista2,x):
  sorteo=[]
  for i in range (b):
    if len(lista2)!=0:
      if x=='high':
        A=max(lista2)
        lista2.remove(A)
        sorteo.append(A)
      elif x=='low':
        A=min(lista2)
        lista2.remove(A)
        sorteo.append(A)
      else: print("Error, elija high o low")
    else: 
      sorteo.append('out of range')
  return(sorteo)
"""

def counter(list1,x): #Función para contabilizar la recurrencia de un dato en una lista
  lista=[]
  lista2=[]
  if x==True: #Es true cuando se necesitan anidar dos parámetros por iteración a la lista, como el caso de la valoración que sería [id, calificación] o reembolso que sería [id, 1/0]
    valores=[[lista[0],lista[1]] for lista in list1] #le asigna los valores de los índices 0 y 1 de la lista de entrada a la variable valores
  else: #En caso de que sólo se necesite 1 valor, como el caso de búsquedas con el id del producto buscado
    valores=[lista for lista in list1] #le asigna los valores de la lista de entrada a valores
  for i in valores:
    if i not in lista:
     lista.append(i) #hace append de los valores nuevos que encuentre en lista
  for i in lista: #de todos los valores nuevos y únicos que encontró
    A=valores.count(i) #cuenta cuántas veces se encuentran en la lista de valores 
    lista2.append([A,i]) #genera una nueva lista que hace append de [veces que se encontró el valor, valor]
  return(lista2)

def sorteo(b,lista,x):
  sortedlist=[] #se genera lista vacía
  if x=='high': 
    lista.sort(reverse=True, key=lambda x: x[0]) #permite filtrar los datos de mayor a menor, tomando como dato crítico el que está en el índice 0
  elif x=='low':
    lista.sort(key=lambda x: x[0]) #permite filtrar los datos de menor a mayor, tomando como dato crítico el que está en el índice 0
  else: 
    print("Error, choose high o low")
    exit(1) #sale del programa en caso de que haya error
  
  for i in range (b): #Lo itera el número de veces que elija el usuario
    if i>=len(lista):
      sortedlist.append('Out of range') #en caso de que sea mayor al índice de la lista, hace append de 'out of range'
    else: 
      sortedlist.append(lista[i]) #en caso de que el índice esté dentro, hace append del valor en el índice i de nuestra lista de entrada 
  return(sortedlist) #regresa la lista sorteada

def ventastot(lista):#se introduce la lista de la que se desea encontrar su suma y promedio
  ventaZ=0
  count=0
  promedio=0
  #se generan 3 variables, ventaZ que guarda la suma de las ventas, count que permite contar cuántas veces se realiza el loop para despues poder sacar el promedio guardado en la variable promedio
  for i in lista: #itera en cada elemento de la lista introducida
    if i[4]==0: #sólo productos sin devolución a considerar
      for J in LP: #revisa cada elemento de la lista lifestore_products para revisar los precios
        if i[1]==J[0]: #revisa que los índices que contienen el id del producto sean iguales
          ventaZ+=float(J[2]) #suma el precio del producto encontrado a ventas
          count+=1 #cuenta las veces que se itera
      if count>0: #en caso de sí tener ventas
        promedio=ventaZ/count #saca el promedio
  return([ventaZ,promedio]) #regresa en forma de lista ventas y promedio

#Definición de variables 
ventas=[]
busca=[]
bajos=[]
altos=[]
ratingdual=[]
reembolso=[]
categoriaelegida=[]
resultadocat=[]

for venta in LSa: #itera en cada elemento de la lista lifestore_sales
  for J in LP: #revisa cada elemento de la lista lifestore_products para revisar la categoría
    if venta[1]==J[0]: #revisa que los índices que contienen el id del producto sean iguales
      ventas.append([venta[1],J[3]]) #hace append del id del producto y su categoría

for search in LSe:
  busca.append(search[1]) #genera una lista con todos los IDs de búsquedas

for rating in LSa: 
  if rating[2]<=3: #en caso de que el rating encontrado en el elemento de lifestore_sales sea menor o igual a tres se considera mala review
    bajos.append([rating[1],rating[4]]) #en la lista bajos se añade el [id,reembolso (1/0)]
  else:  #en caso de que el rating sea mayor a 3 estrellas
    altos.append([rating[1],rating[4]]) #en la lista altos se añade el [id,reembolso (1/0)]
for i in bajos: 
  if i in altos: #en caso de que un elemento esté tanto en la lista de altos y bajos
    #print("ID: Rating alto y bajo:     ",i[0])
    ratingdual.append(i) #se añade a la lista de rating dual
  if i[1]==1: #en caso de que se haya reembolsado
    #print("ID: Producto con reembolso: ", i[0])
    reembolso.append(i) #se añade a la lista de los elementos con reembolso


#en esta sección se hace la cuenta de los items de las listas generadas de busquedas, ventas y ratings tanto altos como bajos
ventascontadas=counter(ventas,True) 
busquedascontadas=counter(busca,False)
ratingbajocontado=counter(bajos,True)
ratingaltocontado=counter(altos,True)

#Definición de variables de ventas por mes
ventas1=[]
ventas2=[]
ventas3=[]
ventas4=[]
ventas5=[]
ventas6=[]
ventas7=[]
ventas8=[]
ventas9=[]
ventas10=[]
ventas11=[]
ventas12=[]
#Variable que hace append de todos los meses
Ventapormeses=[]

#Filtra por mes los datos de ventas y los guarda en su lista respectiva
for i in LSa:
  if "/01/" in i[3]: 
    ventas1.append(i)
  elif "/02/" in i[3]: 
    ventas2.append(i)
  elif "/03/" in i[3]: 
    ventas3.append(i)
  elif "/04/" in i[3]: 
    ventas4.append(i)
  elif "/05/" in i[3]: 
    ventas5.append(i)
  elif "/06/" in i[3]: 
    ventas6.append(i)
  elif "/07/" in i[3]: 
    ventas7.append(i)
  elif "/08/" in i[3]: 
    ventas8.append(i)
  elif "/09/" in i[3]: 
    ventas9.append(i)
  elif "/10/" in i[3]: 
    ventas10.append(i)
  elif "/11/" in i[3]: 
    ventas11.append(i)
  elif "/12/" in i[3]: 
    ventas12.append(i)
  else: print("¡No hay más de 12 meses!") #En caso de que llegue un dato extranio

Ventatotal=ventastot(LSa) #Encuentra las ventas totales y promedio total de ventas

#Hace append de cada mes en Ventaspormeses[]
Ventapormeses.append([1,ventastot(ventas1)])
Ventapormeses.append([2,ventastot(ventas2)])
Ventapormeses.append([3,ventastot(ventas3)])
Ventapormeses.append([4,ventastot(ventas4)])
Ventapormeses.append([5,ventastot(ventas5)])
Ventapormeses.append([6,ventastot(ventas6)])
Ventapormeses.append([7,ventastot(ventas7)])
Ventapormeses.append([8,ventastot(ventas8)])
Ventapormeses.append([9,ventastot(ventas9)])
Ventapormeses.append([10,ventastot(ventas10)])
Ventapormeses.append([11,ventastot(ventas11)])
Ventapormeses.append([12,ventastot(ventas12)])


print("""
  ______        _______        _     
 |  ____|      |__   __|      | |    
 | |__   _ __ ___ | | ___  ___| |__  
 |  __| | '_ ` _ \| |/ _ \/ __| '_ \ 
 | |____| | | | | | |  __/ (__| | | |
 |______|_| |_| |_|_|\___|\___|_| |_|

                 and

      ╦  ┬┌─┐┌─┐╔═╗┌┬┐┌─┐┬─┐┌─┐
      ║  │├┤ ├┤ ╚═╗ │ │ │├┬┘├┤ 
      ╩═╝┴└  └─┘╚═╝ ┴ └─┘┴└─└─┘

""") #Para que se vea pro

print("Bienvenido a este software para consultar datos de tu tienda\n\n")
hola=input("Usuario: ")
cont=input("Contraseña: ")
intento=1

#Esta sección espera que el usuario digite correctamente la contraseña en al menos 3 intentos, si no, finaliza el programa
while(cont!='Pass123'):
  if intento<=2:
    print("Contraseña incorrecta, intenta de nuevo")
    cont=input("Contraseña: ")
    intento+=1
  else: 
    print("Contacte a su administrador")
    exit(1)

while(True): #Bucle infinito
  print(100*"\n") #Para limpiar pantalla
  print("¿Qué deseas hacer?")
  decision=input("""
   _______________________________
  |1.- Mayores ventas             |
  |2.- Mayores búsquedas          |
  |3.- Menores ventas             |
  |4.- Menores búsquedas          |
  |_______________________________|
  |5.- Mejores reseñas            |
  |6.- Peores reseñas             |
  |_______________________________|
  |7.- Total de ingresos          |
  |8.- Ventas promedio mensuales  |
  |9.- Meses con más ventas       |
  |_______________________________|
  """)
  decision=int(decision) #Haciendo cast de la variable a int
  print(100*"\n") # Para limpiar pantalla
  
  index=0 #Nos permitirá enumerar las listas de salida como counter

  tablav="|  Lugar  |  ID  |  Ventas   |"
  tablab="|  Lugar  |  ID  | Búsquedas |"
  tablar="|  Lugar  |  ID  |  #Ratings |"
  tablabr="|  Lugar  |  ID  |  #Ratings |  Reembolso  |"
  tablam="|  Mes  |  Ventas  |  Promedio |"

  if decision==1: #Mayores ventas
    dec=input("¿De cuántos items deseas mayores ventas? \n")
    highventas=sorteo(int(dec),ventascontadas,'high') #Sort descendente de "dec" ventas cuantificadas 
    print(tablav) #Imprimiendo los títulos de la tabla

    for i in highventas: #Imprime elemento por elemento: index, ID y número de ventas
      index+=1
      print( "| ",index, "      ", i[1][0],"       ",i[0])

    #La siguiente parte del código es igual para todas las opciones, intenté hacer una función pero no me fue posible posicionar en la función un continue, por lo que es repetitivo a través del código
    inout=input("¿Deseas hacer otra consulta? (y/n) \n")
    if inout=='y':
      continue
    else: 
      print("Hasta la vista, viejo")
      exit(1)
  
  elif decision==2: #Búsquedas máximas
    dec=input("¿De cuántos items deseas mayores búsquedas? \n")
    highbusq=sorteo(int(dec),busquedascontadas,'high') #Sort descendente de "dec" búsquedas cuantificadas 
    
    print(tablab)
    for i in highbusq:
      index+=1
      print( "| ",index, "      ", i[1],"       ",i[0])
    
    inout=input("¿Deseas hacer otra consulta? (y/n) \n") #Espera que el usuario le diga si quiere hacer otra cosa
    if inout=='y':
      continue
    else: 
      print("Hasta la vista, baby")
      exit(1)
  
  elif decision==3: #Búsquedas menores
    dcateg=[] #Se genera una variable que almacenará las categorías
    dec=input("¿De cuántos items deseas menores búsquedas? \n")
    lowventas=sorteo(int(dec),ventascontadas,'low') #Sort ascendente de "dec" búsquedas cuantificadas 
    bajventas=sorteo(len(LSa),ventascontadas,'low') #La peor situación es que tuviéramos una categoría por venta, por lo que se genera esta lista que considera esa opción

    print(tablab)
    for i in lowventas:
      index+=1
      print( "| ",index, "      ", i[1][0],"       ",i[0])
    
    index=0
    inout=input("¿Deseas consultar por categoría? (y/n) \n")
    if inout=='y':
      print("\nCategorías disponibles:")

      #El loop siguiente itera por todos los índices de lifestore_Products y numera las diferentes categorías encontradas
      for i in LP:
        if i[3] not in dcateg:
          index+=1
          print(index,".- ",i[3])
          dcateg.append(i[3])
       
      ca=input("Elige tu categoría: \n")
      ca=int(ca)
      cat=dcateg[ca-1] #La categoría elegida sería de n-1 ya que nuestras listas empiezan con índice 0
      num=input("Elige cuántos items quieres de esa categoría: \n")
      num=int(num)

      print("Categoría elegida: ",cat)
      print(tablav)
    
      for i in bajventas:
        if i != 'Out of range':
          if i[1][1]==cat:
            categoriaelegida.append(i) #Va introduciendo dependiendo la categoría que eligió el usuario los elementos correspondientes a la misma
   
      for i in range(num): #Itera el número de veces que el usuario haya elegido
        if i<len(categoriaelegida):
          resultadocat.append(categoriaelegida[i])
        else: resultadocat.append('Out of range') #Siempre teniendo en cuenta si excede los datos existentes en la lista
        
      index=0
      for i in resultadocat:
        index+=1
        print( "| ",index, "      ", i[1][0],"       ",i[0])
      
      inout=input("¿Deseas hacer otra consulta? (y/n) \n")
      if inout=='y':
       continue
      else: 
        print("Hasta la vista, ser etéreo")
        exit(1)
    else:
      inout=input("¿Deseas hacer otra consulta? (y/n) \n")
      if inout=='y':
        continue
      else: 
        print("Hasta la vista, ser de luz")
        exit(1)       
  
  elif decision==4: #Búsquedas menores
    dec=input("¿De cuántos items deseas menores búsquedas? \n")
    lowbusq=sorteo(int(dec),busquedascontadas,'low')  #Sort ascendente de "dec" búsquedas cuantificadas 
    
    print(tablab)
    
    for i in lowbusq:
      index+=1
      print( "| ",index, "      ", i[1],"       ",i[0])
    
    inout=input("¿Deseas hacer otra consulta? (y/n) \n")
    if inout=='y':
      continue
    else: 
      print("Hasta la vista, corazón")
      exit(1)   

  elif decision==5: #Mejores reseñas
    print("Se considera que los artículos con buenas reseñas son los que tienen de 4 a 5 estrellas\n")
    dec=input("¿De cuántos items deseas mejores reseñas? \n")
    bestrev=sorteo(int(dec),ratingaltocontado,'high')  #Sort descendente de "dec" ratings buenos cuantificados 
    
    print(tablar)
    for i in bestrev:
      index+=1
      print( "| ",index, "      ", i[1][0],"       ",i[0])
    
    print("\n Los IDs de productos que recibieron reviews tanto buenas como malas son: ")
    for i in ratingdual:
      print(i[0])

    inout=input("¿Deseas hacer otra consulta? (y/n) \n")
    if inout=='y':
      continue
    else: 
      print("Hasta la vista, chulísimo")
      exit(1)   
  
  elif decision==6: #Peores reseñas
    print("Se considera que los artículos con malas reseñas son los que tienen de 1 a 3 estrellas y se documenta si hubo reembolso\n")
    dec=input("¿De cuántos items deseas peores reseñas? \n")
    worstrev=sorteo(int(dec),ratingbajocontado,'high')  #Sort descendente de "dec" ratings malos cuantificados
    
    print(tablabr)
    for i in worstrev:
      index+=1
      if i!='Out of range':
        if i[1][1]==1: #En esta sección se revisa si tuvieron devolución y se cambia el 1/0 por Sí/No
          i[1][1]='Sí'
        else:
          i[1][1]='No'
        print( "| ",index, "      ", i[1][0],"       ",i[0], "          ",i[1][1])
      else: print( "| ",index, "      ", "---","     ","---", "        ","---") #En caso de que la petición esté fuera del rango, imprime esto

    print("\n Los IDs de productos que recibieron reviews tanto buenas como malas son: ")
    for i in ratingdual:
      print(i[0])

    inout=input("¿Deseas hacer otra consulta? (y/n) \n")
    if inout=='y':
      continue
    else: 
      print("Hasta la vista, pythonista")
      exit(1) 
  
  elif decision==7: #Total de ingresos
    print("Tu venta total es de: ",Ventatotal[0], "\n")
    print("Siendo el promedio de: ",Ventatotal[1], "\n")
    
    inout=input("¿Deseas hacer otra consulta? (y/n) \n")
    if inout=='y':
      continue
    else: 
      print("Hasta la vista, mi estimado")
      exit(1) 

  elif decision==8: #Consulta de venta por mes
    mes=input("Elige el mes a consultar: (1-12) \n")
    mes=int(mes)
    print(tablam)
    print( "| ",Ventapormeses[mes-1][0], "     ", Ventapormeses[mes-1][1][0],"    ",Ventapormeses[mes-1][1][1])
    inout=input("¿Deseas hacer otra consulta? (y/n) \n")
    
    if inout=='y':
      continue
    else: 
      print("Hasta la vista, bonito")
      exit(1) 

  elif decision==9: #Meses con más ventas
    mesalto=[] #Variable que guarda los valores de n meses más altos
    mesnum=input("Elige de cuántos meses quieres las mayores ventas: \n")
    mesnum=int(mesnum)

    ventasmayores=Ventapormeses
    ventasmayores.sort(reverse=True, key=lambda x: x[1][0]) #Sorteo descendente tomando como referencia el valor que está en n[1][0]
    
    for i in range(mesnum): #Añade los valores de los n meses que el usuario elija
      mesalto.append(ventasmayores[i])
    
    print(tablam)  

    for i in mesalto:
      print( "| ",i[0], "    ", i[1][0],"   ",i[1][1])
    
    inout=input("¿Deseas hacer otra consulta? (y/n) \n")
    if inout=='y':
      continue
    else: 
      print("Hasta la vista, EmTecher")
      exit(1) 