# -*- coding: cp1252 -*-
#Universidad Tecnologica de Pereira
# Diego Alejandro Valencia - 1093225775
# Daniela Zuluaga Ocampo -  1112784440
#Inteligencia Artificial -Grupo 2

import nltk
import pygame

sintv=['tv','television']
sinluz=['luces','bombilla','bombillo']
sinpuerta=['porton','entrada']
sincortina=['persiana','cortinas']
sinarmario=['guardaropa','ropero','alacena','despensa','closet']
sinaroma=['perfumar']
sinducha=['chorro']
sinnevera=['frigorifico','refrigerador']
sinhorno=['micro-ondas']
sincomputador=['computadora','ordenador']

activado=(255,255,255)
desactivado=(118,213,254)

def Impresion(elemento,estado,accion,opcion):

	el=['televisor','armario','aromatizante','lavamanos','jabon','papel','horno','lavaplatos','computador','escritorio','sonido']
	la=['luz','chimenea','cortina','ventana','puerta','ducha','estufa','nevera','lavadora','secadora','cafetera']
	accione=['encender','enciende','encienda','prenda','prender','prende']
	accionap=['apagar','apaga','apague']
	accionab=['abre','abrir','abra']
	accionc=['cierra','cerrar','cierre']
	acciond=['desactive','desactiva','desactivar']
	accionac=['activar','active','activa']

	if accion in accione:
		accion='encendido'
	if accion in acciond:
		accion='desactivado'
	if accion in accionac:
		accion='activado'
	if accion in accionap:
		accion='apagado'
	if accion in accionab:
		accion='abierto'
	if accion in accionc:
		accion='cerrado'

	if opcion==1:
		if elemento in el:
			if estado==1:
				print "El",elemento,"se ha",accion
			else:
				print "El",elemento,"se ha",accion
		if elemento in la:
			if estado==1:
				print "La",elemento,"se ha",accion
			else:
				print "La",elemento,"se ha",accion
		if elemento =='aspersores':
			if estado==1:
				print "Los",elemento,"se han",accion
	if opcion==2:
		if elemento in el:
			if estado==1:
				print "El",elemento,"ya se ha",accion
			else:
				print "El",elemento,"ya se ha",accion
		if elemento in la:
			if estado==1:
				print "La",elemento,"ya se ha",accion
			else:
				print "La",elemento,"ya se ha",accion
		if elemento =='aspersores':
			if estado==1:
				print "Los",elemento,"ya se han",accion

class Salon():

	def __init__(self):
		self.elemsalon=['televisor','luz','cortina','ventana','puerta','sonido']
		self.esalon=[]
		for i in range(len(self.elemsalon)):
			self.esalon.append(0)
			
	def Cambio(self,pantalla,elemento,estado):
		if elemento=='televisor':
			rec=pygame.Rect(30,70,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("televisor.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='luz':
			rec=pygame.Rect(85,70,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("luz.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='cortina':
			rec=pygame.Rect(140,70,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("cortina.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='ventana':
			rec=pygame.Rect(30,138,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("ventana.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='puerta':
			rec=pygame.Rect(85,138,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("puerta.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='sonido':
			rec=pygame.Rect(140,138,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("sonido.png").convert_alpha()
			pantalla.blit(ob,rec)

	def ModificarSalon(self,elementosmod):
		for j in range (len(elementosmod)):
			if elementosmod[j][0] in sintv:
				elementosmod[j][0] = 'televisor'
			if elementosmod[j][0] in sinluz:
				elementosmod[j][0]='luz'
			if elementosmod[j][0] in sinpuerta:
				elementosmod[j][0]= 'puerta'
			if elementosmod[j][0] in sincortina:
				elementosmod[j][0]= 'cortina'
			pos=None
			try:
				pos=self.elemsalon.index(elementosmod[j][0])
			except ValueError:
				print "El elemento no se encuentra en la habitacion"
			if pos!=None:
				if elementosmod[j][1]==1:
					if self.esalon[pos]==1:
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
					else:
						self.esalon[pos]=elementosmod[j][1]
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
				else:
					if self.esalon[pos]==0:
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
					else:
						self.esalon[pos]=elementosmod[j][1]
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
		return elementosmod[j][1],elementosmod[j][0]

class Dormitorio():

	def __init__(self):
		self.elemdormitorio=['luz','cortina','ventana','puerta','armario']
		self.edormitorio=[]
		for i in range(len(self.elemdormitorio)):
			self.edormitorio.append(0)

	def Cambio(self,pantalla,elemento,estado):

		if elemento=='luz':
			rec=pygame.Rect(235,70,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("luz.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='cortina':
			rec=pygame.Rect(290,70,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("cortina.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='ventana':
			rec=pygame.Rect(340,70,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("ventana.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='puerta':
			rec=pygame.Rect(235,138,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("puerta.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='armario':
			rec=pygame.Rect(290,138,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("armario.png").convert_alpha()
			pantalla.blit(ob,rec)

	def ModificarDormitorio(self,elementosmod):
		for j in range (len(elementosmod)):
			if elementosmod[j][0] in sinluz:
				elementosmod[j][0]='luz'
			if elementosmod[j][0] in sinpuerta:
				elementosmod[j][0]= 'puerta'
			if elementosmod[j][0] in sincortina:
				elementosmod[j][0]= 'cortina'
			if elementosmod[j][0] in sinarmario:
				elementosmod[j][0]= 'armario'
			pos=None
			try:
				pos=self.elemdormitorio.index(elementosmod[j][0])
			except ValueError:
				print "El elemento no se encuentra en la habitacion"
			if pos!=None:
				if elementosmod[j][1]==1:
					if self.edormitorio[pos]==1:
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
					else:
						self.edormitorio[pos]=elementosmod[j][1]
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
				else:
					if self.edormitorio[pos]==0:
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
					else:
						self.edormitorio[pos]=elementosmod[j][1]
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
		return elementosmod[j][1],elementosmod[j][0]
 
class Bano():
	
	def __init__(self):
		self.elembano=['luz','cortina','ventana','puerta','aroma','lavamanos','ducha','calentador']
		self.ebano=[]
		for i in range(len(self.elembano)):
			self.ebano.append(0)

	def Cambio(self,pantalla,elemento,estado):

		if elemento=='luz':
			rec=pygame.Rect(420,70,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("luz.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='cortina':
			rec=pygame.Rect(480,70,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("cortina.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='ventana':
			rec=pygame.Rect(530,70,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("ventana.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='puerta':
			rec=pygame.Rect(585,70,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("puerta.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='aroma':
			rec=pygame.Rect(420,138,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("aroma.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='lavamanos':
			rec=pygame.Rect(480,138,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("lavamos.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='ducha':
			rec=pygame.Rect(530,138,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("ducha.png").convert_alpha()
			pantalla.blit(ob,rec)

	def ModificarBano(self,elementosmod):
		for j in range (len(elementosmod)):
			if elementosmod[j][0] in sinluz:
				elementosmod[j][0]='luz'
			if elementosmod[j][0] in sinpuerta:
				elementosmod[j][0]= 'puerta'
			if elementosmod[j][0] in sincortina:
				elementosmod[j][0]= 'cortina'
			if elementosmod[j][0] in sinaroma:
				elementosmod[j][0]= 'aroma'
			if elementosmod[j][0] in sinducha:
				elementosmod[j][0]= 'ducha'
			pos=None
			try:
				pos=self.elembano.index(elementosmod[j][0])
			except ValueError:
				print "El elemento no se encuentra en la habitacion"
			if pos!=None:
				if elementosmod[j][0]=='ducha':
					if elementosmod[j][1]==1:
						if self.ebano[pos]==1:
							Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
						else:
							self.ebano[pos]=elementosmod[j][1]
							Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
							print "¿Desea encender el calentador de agua?"
							instruccion=str(raw_input(">>"))
							tokens=nltk.word_tokenize(instruccion)
							if 'si' in tokens:
								posd=self.elembano.index('calentador')
								self.ebano[posd]=1
								Impresion('calentador',1,'encender',1)
								print "El calentador de agua se ha encendido"
					else:
						if self.ebano[pos]==0:
							Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
						else:
							posd=self.elembano.index('calentador')
							self.ebano[posd]=elementosmod[j][1]
							Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
							self.ebano[posd]=0
							Impresion('calentador',0,'apagar',1)
				else:
					if elementosmod[j][1]==1:
						if self.ebano[pos]==1:
							Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
						else:
							self.ebano[pos]=elementosmod[j][1]
							Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
					else:
						if self.ebano[pos]==0:
							Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
						else:
							self.ebano[pos]=elementosmod[j][1]
							Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
		return elementosmod[j][1],elementosmod[j][0]

class Cocina():

	def __init__(self):

		self.elemcocina=['luz','nevera','puerta','lavaplatos','armario','estufa']
		self.ecocina=[]
		for i in range(len(self.elemcocina)):
			self.ecocina.append(0)

		self.estufa=[0,0,0,0] #Cantidad de fogones

	def Cambio(self,pantalla,elemento,estado):

		if elemento=='luz':
			rec=pygame.Rect(30,290,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("luz.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='nevera':
			rec=pygame.Rect(85,290,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("nevera.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='puerta':
			rec=pygame.Rect(135,290,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("puerta.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='lavaplatos':
			rec=pygame.Rect(30,355,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("lavamos.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='armario':
			rec=pygame.Rect(76,355,50,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("armarioc.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='estufa':
			rec=pygame.Rect(135,355,40,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("estufa.png").convert_alpha()
			pantalla.blit(ob,rec)

	def ModificarCocina(self,elementosmod):
		for j in range (len(elementosmod)):
			if elementosmod[j][0] in sinluz:
				elementosmod[j][0]='luz'
			if elementosmod[j][0] in sinpuerta:
				elementosmod[j][0]= 'puerta'
			if elementosmod[j][0] in sinnevera:
				elementosmod[j][0]= 'nevera'
			if elementosmod[j][0] in sinhorno:
				elementosmod[j][0]= 'horno'
			if elementosmod[j][0] in sinarmario:
				elementosmod[j][0]= 'armario'
			pos=None
			try:
				pos=self.elemcocina.index(elementosmod[j][0])
			except ValueError:
				print "El elemento no se encuentra en la habitacion"
			if pos!=None:
				if elementosmod[j][0]=='estufa':
					fogoencendidos=0
					fogoapagados=0
					if elementosmod[j][1]==1:
						for i in range(len(self.estufa)):
							if self.estufa[i]==1:
								print "El fogon",i+1,"ya se encuentra encendido"
								fogoencendidos=fogoencendidos+1
						if fogoencendidos==4:
							print "Todos los fogones de la estufa ya se encuentran encendidos"
						else:
							print "¿Que fogon desea encender?, Por favor escribir el numero del fogon"
							instruccion=str(raw_input(">>"))
							tokens=nltk.word_tokenize(instruccion)
							if ('1' in tokens) or ('uno' in tokens):
								if self.estufa[0]==0:
									self.estufa[0]=elementosmod[j][1]
									print "El fogon 1 se ha encendido"
								else:
									print "El fogon 1 ya se encuentra encendido"
							if '2' in tokens or 'dos' in tokens:
								if self.estufa[1]==0:
									self.estufa[1]=elementosmod[j][1]
									print "El fogon 2 se ha encendido"
								else:
									print "El fogon 2 ya se encuentra encendido"
							if '3' in tokens or 'tres' in tokens:
								if self.estufa[2]==0:
									self.estufa[2]=elementosmod[j][1]
									print "El fogon 3 se ha encendido"
								else :
									print "El fogon 3 ya se encuentra encendido"
							if '4' in tokens or 'cuatro' in tokens:
								if self.estufa[3]==0:
									self.estufa[3]=elementosmod[j][1]
									print "El fogon 4 se ha encendido"
								else:
									print "El fogon 4 ya se encuentra encendido"
					else:
						for i in self.estufa:
							if i==0:
								fogoapagados=fogoapagados+1
						if fogoapagados==4:
							print "Todos los fogones de la estufa ya se encuentran apagados"
						else:
							print "¿Que fogon desea apagar?, Por favor escribir el numero del fogon"
							instruccion=str(raw_input(">>"))
							tokens=nltk.word_tokenize(instruccion)
							if ('1' in tokens) or ('uno' in tokens):
								if self.estufa[0]==0:
									self.estufa[0]=elementosmod[j][1]
									print "El fogon 1 se ha apagado"
								else:
									print "El fogon 1 ya se encuentra apagado"
							if '2' in tokens or 'dos' in tokens:
								if self.estufa[1]==0:
									self.estufa[1]=elementosmod[j][1]
									print "El fogon 2 se ha apagado"
								else:
									print "El fogon 2 ya se encuentra apagado"
							if '3' in tokens or 'tres' in tokens:
								if self.estufa[2]==0:
									self.estufa[2]=elementosmod[j][1]
									print "El fogon 3 se ha apagado"
								else :
									print "El fogon 3 ya se encuentra apagado"
							if '4' in tokens or 'cuatro' in tokens:
								if self.estufa[3]==0:
									self.estufa[3]=elementosmod[j][1]
									print "El fogon 4 se ha apagado"
								else:
									print "El fogon 4 ya se encuentra apagado"
				else:
					if elementosmod[j][1]==1:
						if self.ecocina[pos]==1:
							Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
						else:
							self.ecocina[pos]=elementosmod[j][1]
							Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
					else:
						if self.ecocina[pos]==0:
							Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
						else:
							self.ecocina[pos]=elementosmod[j][1]
							Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
		return elementosmod[j][1],elementosmod[j][0]
			
class Comedor():

	def __init__(self):

		self.elemcomedor=['luz','cortina','ventana','puerta']
		self.ecomedor=[]
		for i in range(len(self.elemcomedor)):
			self.ecomedor.append(0)

	def Cambio(self,pantalla,elemento,estado):
		if elemento=='luz':
			rec=pygame.Rect(670,70,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("luz.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='cortina':
			rec=pygame.Rect(720,70,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("cortina.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='ventana':
			rec=pygame.Rect(670,138,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("ventana.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='puerta':
			rec=pygame.Rect(720,138,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("puerta.png").convert_alpha()
			pantalla.blit(ob,rec)


	def ModificarComedor(self,elementosmod):
		for j in range (len(elementosmod)):
			if elementosmod[j][0] in sinluz:
				elementosmod[j][0]='luz'
			if elementosmod[j][0] in sinpuerta:
				elementosmod[j][0]= 'puerta'
			if elementosmod[j][0] in sincortina:
				elementosmod[j][0]= 'cortina'
			pos=None
			try:
				pos=self.elemcomedor.index(elementosmod[j][0])
			except ValueError:
				print "El elemento no se encuentra en la habitacion"
			if pos!=None:
				if elementosmod[j][1]==1:
					if self.ecomedor[pos]==1:
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
					else:
						self.ecomedor[pos]=elementosmod[j][1]
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
				else:
					if self.ecomedor[pos]==0:
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
					else:
						self.ecomedor[pos]=elementosmod[j][1]
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
		return elementosmod[j][1],elementosmod[j][0]

class CuartoLavado():

	def __init__(self):

	 	self.elemlavado=['luz','lavadora','secadora','puerta']
		self.elavado=[]
		for i in range(len(self.elemlavado)):
			self.elavado.append(0)

	def Cambio(self,pantalla,elemento,estado):

		if elemento=='luz':
			rec=pygame.Rect(230,290,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("luz.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='puerta':
			rec=pygame.Rect(280,355,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("puerta.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='lavadora':
			rec=pygame.Rect(280,290,40,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("lavadora.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='secadora':
			rec=pygame.Rect(225,355,40,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("secadora.png").convert_alpha()
			pantalla.blit(ob,rec)

	def ModificarCuartoL(self,elementosmod):
		for j in range (len(elementosmod)):
			if elementosmod[j][0] in sinluz:
				elementosmod[j][0]='luz'
			if elementosmod[j][0] in sinpuerta:
				elementosmod[j][0]= 'puerta'
			pos=None
			try:
				pos=self.elemlavado.index(elementosmod[j][0])
			except ValueError:
				print "El elemento no se encuentra en la habitacion"
			if pos!=None:
				if elementosmod[j][1]==1:
					if self.elavado[pos]==1:
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
					else:
						self.elavado[pos]=elementosmod[j][1]
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
				else:
					if self.elavado[pos]==0:
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
					else:
						self.elavado[pos]=elementosmod[j][1]
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
		return elementosmod[j][1],elementosmod[j][0]

class CuartoTrabajo():

	def __init__(self):

		self.elemtrabajo=['luz','puerta','cortina','computador']
		self.etrabajo=[]
		for i in range(len(self.elemtrabajo)):
			self.etrabajo.append(0)

	def Cambio(self,pantalla,elemento,estado):

		if elemento=='luz':
			rec=pygame.Rect(385,290,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("luz.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='puerta':
			rec=pygame.Rect(440,290,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("puerta.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='cortina':
			rec=pygame.Rect(440,355,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("puerta.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='computador':
			rec=pygame.Rect(385,355,40,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("puerta.png").convert_alpha()
			pantalla.blit(ob,rec)

	def ModificarCuartoT(self,elementosmod):
		for j in range (len(elementosmod)):
			if elementosmod[j][0] in sincomputador:
				elementosmod[j][0] = 'computador'
			if elementosmod[j][0] in sinluz:
				elementosmod[j][0]='luz'
			if elementosmod[j][0] in sinpuerta:
				elementosmod[j][0]= 'puerta'
			if elementosmod[j][0] in sincortina:
				elementosmod[j][0]= 'cortina'
			pos=None
			try:
				pos=self.elemtrabajo.index(elementosmod[j][0])
			except ValueError:
				print "El elemento no se encuentra en la habitacion"
			if pos!=None:
				if elementosmod[j][1]==1:
					if self.etrabajo[pos]==1:
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
					else:
						self.etrabajo[pos]=elementosmod[j][1]
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
				else:
					if self.etrabajo[pos]==0:
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
					else:
						self.etrabajo[pos]=elementosmod[j][1]
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
		return elementosmod[j][1],elementosmod[j][0]

class Garaje():

	def __init__(self):

		self.elemgaraje=['luz','puerta']
		self.egaraje=[]
		for i in range(len(self.elemgaraje)):
			self.egaraje.append(0)

	def Cambio(self,pantalla,elemento,estado):
		if elemento=='luz':
			rec=pygame.Rect(550,290,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("luz.png").convert_alpha()
			pantalla.blit(ob,rec)

		if elemento=='puerta':
			rec=pygame.Rect(600,290,35,50)
			if estado==1:
				pygame.draw.rect(pantalla,activado,rec)
			else:
				pygame.draw.rect(pantalla,desactivado,rec)
			ob=pygame.image.load("puerta.png").convert_alpha()
			pantalla.blit(ob,rec)

	def ModificarGaraje(self,elementosmod):
		for j in range (len(elementosmod)):
			if elementosmod[j][0] in sinluz:
				elementosmod[j][0]='luz'
			if elementosmod[j][0] in sinpuerta:
				elementosmod[j][0]= 'puerta'

			pos=None
			try:
				pos=self.elemgaraje.index(elementosmod[j][0])
			except ValueError:
				print "El elemento no se encuentra en la habitacion"
			if pos!=None:
				if elementosmod[j][1]==1:
					if self.egaraje[pos]==1:
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
					else:
						self.egaraje[pos]=elementosmod[j][1]
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
				else:
					if self.egaraje[pos]==0:
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],2)
					else:
						self.egaraje[pos]=elementosmod[j][1]
						Impresion(elementosmod[j][0],elementosmod[j][1],elementosmod[j][2],1)
		return elementosmod[j][1],elementosmod[j][0]
