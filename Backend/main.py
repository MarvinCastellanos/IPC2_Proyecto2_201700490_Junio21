from flask import Flask
from flask.globals import request
from xml.etree import ElementTree as ET
from xml.dom import minidom

app=Flask(__name__)
#LISTA CONTENEDORA DE DATOS
class lista:
    def __init__(self):
        self.lista_datos=[]
    
    def agrega(self,dato):
        self.lista_datos.append(dato)

#OBJETOS DE DATOS
class cliente:
    def __init__(self, nombre, apellido, edad, cumpleanos, fechaPrimeraCompra):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.cumpleanos=cumpleanos
        self.fechaPrimeraCompra=fechaPrimeraCompra

class mejorCliente:
    def __init__(self,nombre,fechaUltimaCompra,CantidadComprada,cantidadGastada):
        self.nombre=nombre
        self.fechaUltimaCompra=fechaUltimaCompra
        self.cantidadComprada=CantidadComprada
        self.cantidadGastada=cantidadGastada

class juego:
    def __init__(self,nombre,plataforma,anoLanzamiento,clasificacion,stock):
        self.nombre=nombre
        self.plataforma=plataforma
        self.anoLanzamiento=anoLanzamiento
        self.clasificacion=clasificacion
        self.stock=stock

class juegoMasVendido:
    def __init__(self,nombre,fechaUltimaCompra,copiasVendidas,stock):
        self.nombre=nombre
        self.fechaUltimaCompra=fechaUltimaCompra
        self.copiasVendidas=copiasVendidas
        self.stock=stock
#DECLARACION DE LISTAS CONTENEDORAS DE DATOS
listaCliente=lista()
listaMejorCliente=lista()
listaJuego=lista()
listaJuegoMasVendido=lista()

aux=cliente('marvin','castellanos','38','0110','0202')
#FUNSION QUE OBTIENE XML Y LEE LOS DATOS
@app.route('/procesa',methods=['POST'])
def leeXML():
    xml=request.data.decode('utf-8')
    root = ET.fromstring(xml)
#RECORRIDO DE XML
    for child in root:
        #ASIGNACION DE DATOS A LISTA CLIENTES
        if child.tag=='clientes':
            for cliente in child:
                #print(len(child))
                nombre=cliente.find('nombre').text
                apellido=cliente.find('apellido').text
                edad=cliente.find('edad').text
                cumpleanos=cliente.find('fechaCumpleanos').text
                fechaPrimerCompra=cliente.find('fechaPrimeraCompra').text
                print(nombre)
                listaCliente.agrega(cliente(nombre,apellido,edad,cumpleanos,fechaPrimerCompra))
                continue
        #ASIGNACION DE DATOS A LISTA MEJORES CLIENTES
        elif child.tag=='mejoresClientes':
            for mejorCliente in child:
                name=mejorCliente.find('nombre').text
                fechaUltimaCompra=mejorCliente.find('fechaUltimaCompra').text
                cantidadComprada=mejorCliente.find('cantidadComprada').text
                cantidadGastada=mejorCliente.find('cantidadGastada').text
                
                listaMejorCliente.agrega(mejorCliente('name','fechaUltimaCompra','cantidadComprada','cantidadGastada'))
                continue
        #ASIGNACION DE DATOS A LISTA JUEGOS
        elif child.tag=='juegos':
            for juego in child:
                nombre=juego.find('nombre').text
                plataforma=juego.find('plataforma').text
                anoLanzamiento=juego.find('anoLanzamiento').text
                clasificacion=juego.find('clasificacion').text
                stock=juego.find('stock').text
                print(nombre)
                listaCliente.agrega(juego(nombre,plataforma,anoLanzamiento,clasificacion,stock))
                continue
        #ASIGNACION DE DATOS A LISTA JUEGOS MAS VENDIDOS
        elif child.tag=='juegosMasVendidos':
            for juegoMasVendido in child:
                nombre=juegoMasVendido.find('nombre').text
                fechaUltimaCompra=juegoMasVendido.find('fechaUltimaCompra').text
                copiasVendidas=juegoMasVendido.find('copiasVendidas').text
                stock=juegoMasVendido.find('stock').text
                print(nombre)
                listaCliente.agrega(juegoMasVendido(nombre,fechaUltimaCompra,copiasVendidas,clasificacion,stock))
                continue
    #print('lista cliente: '+str(len(listaCliente)))
    return ''

if __name__=='__main__':
    app.run(debug=True)
    