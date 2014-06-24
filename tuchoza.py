#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Tarea Programada 4- Lenguajes de Programación - I Semestre 2014
## Estudiantes: - Edgar Solórzano
##              - Daniel Mora
##              - Gerardo Calderón

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# ---------> Archivo para el manejo de la aplicación Web <---------

## Se importan las librerías necesarias de Flask

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__) # Instancia de la aplicacion

#______________________________________________________________________________________#

#Funcion que crea el archivo donde se almacena la informacion de los apartamentos

class Crear():
    def __init__(self):
        self.datos = []

    def Apartas(self):
        archivo = open('Apartas.txt','w')
        archivo.close()

    def Favoritos(self):
        archivo = open('Favoritos.txt','w')
        archivo.close()

#______________________________________________________________________________________#
    
#Funcion que se encarga de escribir en un archivo los datos del apartamento que agrega el usuario

class Escribir():
    def __init__(self):
        self.datos = []
        
    def EscrituraApartas(self, titulo, descripcion, facilidades, caracteristicas, ubicacion, precio, contacto):
        
        self.Titulo = titulo
        self.Descripcion = descripcion
        self.Facilidades = facilidades
        self.Caracteristicas = caracteristicas
        self.Ubicacion = ubicacion
        self.Precio = precio
        self.Contacto = contacto

        Apartas = open('Apartas.txt','a')
        Apartas.write(titulo.lower() + "," + descripcion.lower() + "," + [facilidades.lower()] + ","+ [caracteristicas.lower()] + "," + ubicacion.lower() + "," + precio + "," + contacto.lower() )
        Apartas.write("\n")
        print("\n")
        Apartas.close()

    def EscrituraFavoritos(self, titulo, descripcion, ubicacion, precio, contacto):
     
        self.Titulo = titulo
        self.Descripcion = descripcion
        self.Ubicacion = ubicacion
        self.Precio = precio
        self.Contacto = contacto

        Favoritos = open('Favoritos.txt','a')
        Favoritos.write(titulo.lower() + "," + descripcion.lower() + "," + [facilidades.lower()] + ","+ [caracteristicas.lower()] + "," + ubicacion.lower() + "," + precio + "," + contacto.lower() )
        Favoritos.write("\n")
        Favoritos.close()
    
#____________________________________________________________________________________________________#
    
# Funcion que se encarga de leer el archivo donde estan los datos del apartamento ingresado


class Leer():
    def __init__(self):
        self.datos = []
        
    def LecturaApartas(self):
        archivo = open('Apartas.txt','r')
        lista = []
        consulta = archivo.readlines() # Lista que contiene las consultas del archivo.

        for elemento in consulta:
            fuerasalto = elemento.strip("\n") # Elimina el salto de linea
            enter = fuerasalto
            lista = lista + [lista.append([str(enter)])]             
        archivo.close()
        lista = filter(None,lista)
        return lista

    def LecturaFavoritos(self):
        archivo = open('Favoritos.txt','r')
        lista=[]
        consulta = archivo.readlines() # Lista que contiene todas las consultas del archivo.
        for elemento in consulta:
            fuera_salto = elemento.strip("\n") # Elimina el salto de consulta
            enter = fuera_salto
            lista= lista + [lista.append([str(enter)])]      
        archivo.close()
        lista= filter(None,lista)
        return lista
    
#______________________________________________________________________________________#

# *********************************
# ******** Mostrar Paginas ********
# *********************************

# - Funciones para mostrar las paginas desde el Menu

# - Funcion para mostrar la Pagina Principal

@app.route('/')
@app.route('/inicio')
def inicio():
    return render_template('ventana.inicio.htm')
    

# - Funcion para mostrar la pagina de Busqueda de apartamentos

@app.route('/busquedas/apartamentos')
def consulta_apartamentos():
    return render_template('consulta.apartamentos.htm')


# - Funcion para mostrar la pagina de publicacion de apartamentos 

@app.route('/publicacion/apartamentos')
def publicacion_restaurantes():
    crear_Archivo()
    return render_template('publicar.apartamentos.htm')
    

# - Funcion para mostrar la pagina de Información del proyecto
    
@app.route('/informacion')
def informacion():
    return render_template('rest.manager.informacion.htm')



# !!!!!!!!!!!!!!!!!!!
#!!! MANTENIMIENTO !!!
# !!!!!!!!!!!!!!!!!!!

# - Funciones para agregar los restaurantes y platillos a la Base de Conocimiento. Se utiliza el valor de un input invisible para determinar cual solicitud se 
#   debe realizar.   


##############################
######## Apartamentos ########
##############################

## Agregar un aparta nuevo ##

@app.route('/resultado_agregar_apartamento', methods=['POST'])
def agregar_aparta():
    titulo_local = 'Apartas'
    mensaje_insercion = ''
    
    # Valores que ingresa el usuario:
    titulo = request.form['inputTitulo']
    descripcion = request.form['inputDescripcion']
    facilidades = request.form['inputFacilidades']
    caracteristicas = request.form['inputCaracteristicas']
    ubicacion = request.form['inputUbicacion']
    precio = request.form['inputPrecio']
    contacto = request.form['inputContacto']
  
    # Darle a mensaje el valor de 'El aparta fue ingresado con éxito' o 'No se logró agregar el aparta'
    try:
        ## Llamar a la funcion que agrega el aparta en la Base de datos
        Escribir.EscrituraApartas(titulo, descripcion, facilidades, caracteristicas, ubicacion, precio, contacto)
        
    except:
        mensaje_insercion = 'No se logró agregar el apartamento'
        
    else:
        mensaje_insercion = 'El aparta fue ingresado con éxito'
        return render_template('resultado_insercion.html', titulo = titulo_local, mensaje = mensaje_insercion)


##############################
######### Favoritos ##########
##############################

## Agregar favorito ##

@app.route('/resultado_agregar_favorito', methods=['POST'])
def agregar_favorito():
    titulo_local = 'Favoritos'
    mensaje_insercion = ''
    
    # Valores que ingresa el usuario:
    titulo = request.form['inputTitulo']
    descripcion = request.form['inputDescripcion']
    facilidades = request.form['inputFacilidades']
    caracteristicas = request.form['inputCaracteristicas']
    ubicacion = request.form['inputUbicacion']
    precio = request.form['inputPrecio']
    contacto = request.form['inputContacto']
  
    # Darle a mensaje el valor de 'El aparta fue ingresado con éxito' o 'No se logró agregar el aparta'
    try:
        ## Llamar a la funcion que agrega el aparta en la Base de datos
        Escribir.EscrituraFavorito(titulo, descripcion, facilidades, caracteristicas, ubicacion, precio, contacto)
        
    except:
        mensaje_insercion = 'No se logró agregar el apartamento'
        
    else:
        mensaje_insercion = 'El aparta fue ingresado con éxito a favoritos'
        return render_template('resultado_insercion.html', titulo = titulo_local, mensaje = mensaje_insercion)
        

# !!!!!!!!!!!!!!!!!!!
#!!!!! CONSULTAS !!!!!!
# !!!!!!!!!!!!!!!!!!!

# - Funciones para devolver el resultado de las diferentes consultas. Se utiliza el valor de un input invisible para determinar cual consulta es la que se 
#   esta solicitando.

##############################
######## Apartamentos ########
##############################

## Mostrar todos los apartamentos ##

@app.route('/resultado_consulta_todos', methods=['POST'])
def consultar_apartas_todos():
    titulo_local = 'Todos los apartamentos'
    
    cont = 0
    lista = Leer.LecturaApartas()

    largo = len(lista)
    
    Resultado = []

    while (cont < largo): 

        ListaApartas = lista[cont]
        
        ListaApartasMuestra= ListaApartas[0].split(",")
        
        Resultado.append(ListaApartasMuestra[0])
           
        cont = cont + 1
    
    Resultado = list(set(Resultado))
    Resultado = filter(None,Resultado)
                
    return render_template('resultado_consulta_apartamentos.html', titulo = titulo_local, apartamentos = Resultado)

## Mostrar los apartas por ubicacion ##

@app.route('/resultado_consulta_ubicacion', methods=['POST'])
def consultar_apartas_ubicacion():

    Tipo = 'ubicacion'
    consulta = request.form['inputTipo']
    titulo_local = 'Apartas por ubicacion: '+consulta

    cont=0
    lista = Leer.LecturaApartas()
    largo= len(lista)
    
    Resultado = []
    
    while (cont < largo):

        ListaApartas = lista[cont]
        ListaApartasMuestra = ListaAparats[0].split(",")

        Ubicacion = ListaApartasMuestra[4]
        
        if(consulta == Ubicacion):

            Nombre = ListaApartasMuestra[0]
            Resultado.append(Nombre)

        cont = cont + 1

    Resultado = list(set(Resultado))
                
    if Resultado == []:
        return render_template('resultado_consulta_apartamentos.html', titulo=titulo_local, nombre='', tipo=Tipo)
    else:
        return render_template('resultado_consulta_apartamentos.html', titulo=titulo_local, nombre='Si hay resultados', apartamentos=Resultado)
		
## Mostrar los apartas con un determinado precio ##

@app.route('/resultado_consulta_precio', methods=['POST'])
def consultar_restaurantes_nombre():
    consulta = request.form['inputPrecio']
    tipo = 'precio'
       
    titulo_local = 'Apartamentos por precio: '+consulta
    
    cont=0
    lista = Leer.LecturaApartas() 
    largo= len(lista) 
    
    Resultado = []   

    while (cont < largo): 

        ListaApartas = lista[cont]
        ListaApartasMuestra = ListaApartas[0].split(",") 
        
        Precio = ListaApartasMuestra[5]
        
        if(consulta == Precio):

            Titulo = ListaApartasMuestra[0]
            Descripcion = ListaApartasMuestra[1]
            Caracteristicas = ListaApartasMuestra[3]
            Ubicacion = ListaApartasMuestra[4]
            Contacto = ListaApartasMuestra[5]

	    Resultado.append(Titulo)
	    Resultado.append(Descripcion)
	    Resultado.append(Caracteristicas)
	    Resultado.append(Ubicacion)
	    Resultado.append(Contacto)
		
        cont = cont + 1  
        
    Resultado = list(set(Resultado))
    
    if Resultado == []:
		return render_template('resultado_consulta_precio.html', titulo=titulo_local, nombre='No existen apartamentos con ese precio')
    else:
		return render_template('resultado_consulta_precio.html', titulo=titulo_local, nombre=consulta, tipo_comida=Tipo_Comida, ubicacion=Ubicacion, telefono=Telefono, horario=Horario)


##############################
######### Facilidades y caracteristicas##########
##############################

## Mostrar los apartamentos que tengan cierta facilidad ##

@app.route('/resultado_consulta_apartas', methods=['POST'])
def consultar_apartas_facilidad():
    consulta = request.form['inputFacilidad']
    titulo_local = 'Apartamentos por facilidad: '+consulta
    
    Tipo = 'facilidad'
    cont=0
    lista = Leer.LecturaApartas()
    largo= len(lista[2])
    
    Resultado = []
    
    while (cont < largo):

        for i in lista[2]:
        
            if(consulta == i):

                Titulo = lista[0]
                Resultado.append(Titulo)

            cont = cont + 1

    Resultado = list(set(Resultado))
                
    if Resultado == []:
        return render_template('resultado_consulta_apartamentos.html', titulo=titulo_local, nombre='', tipo=Tipo)
    else:
        return render_template('resultado_consulta_apartamentos.html', titulo=titulo_local, nombre='Si hay resultados', apartamentos=Resultado)


## Mostrar los apartamentos que tengan cierta caracteristica ##

@app.route('/resultado_consulta_apartas', methods=['POST'])
def consultar_apartas_facilidad():
    consulta = request.form['inputCaracteristica']
    titulo_local = 'Apartamentos por caracteristica: '+consulta
    
    Tipo = 'caracteristicas'
    cont=0
    lista = Leer.LecturaApartas()
    largo= len(lista[3])
    
    Resultado = []
    
    while (cont < largo):

        for i in lista[3]:
        
            if(consulta == i):

                Titulo = lista[0]
                Resultado.append(Titulo)

            cont = cont + 1

    Resultado = list(set(Resultado))
                
    if Resultado == []:
        return render_template('resultado_consulta_apartamentos.html', titulo=titulo_local, nombre='', tipo=Tipo)
    else:
        return render_template('resultado_consulta_apartamentos.html', titulo=titulo_local, nombre='Si hay resultados', apartamentos=Resultado)
    
    
###############################################
# - Se corre el servidor web para la aplicación
###############################################
if __name__ == '__main__':
	app.run(debug=True)
    
