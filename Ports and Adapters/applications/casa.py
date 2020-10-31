# -*- coding: cp1252 -*-
#Universidad Tecnologica de Pereira
# Diego Alejandro Valencia - 1093225775
# Daniela Zuluaga Ocampo -  1112784440
#Inteligencia Artificial -Grupo 2

from cye import *
import nltk.tokenize
import pygame


habitaciones=['salon','sala','dormitorio','alcoba','cuarto','pieza','baño','lavavo','servicio',
'cocina','comedor','comedero','lavado','lavadero','estudio','oficina','garaje','cochera']

elementos=['televisor','tv','television','luces','luz','bombilla','bombillo','cortina','cortinas','ventana','puerta','porton','entrada','armario','aromatizante',
'lavamanos','dispensador de jabon','dispensador de papel','ducha','estufa','nevera','cafetera','lavaplatos','aspersores',
'alarma','lavadora','secadora','computadora','computador','escritorio','sonido','aire','closet']
acciones0=['apagar','apaga','apague','cierra','cerrar','cierre','desactive','desactiva','desactivar']
acciones1=['encender','enciende','encienda','encended','enciendas',
'prenda','prender','prende','abre','abrir','abra','activar','active','activa']

tamano = ancho,alto=797,446
pantalla = pygame.display.set_mode(tamano)

activado=(255,255,255)
desactivado=(118,213,254)
class Casa ():

	def __init__(self):

		self.salon=Salon()
		self.dormitorio=Dormitorio()
		self.bano=Bano()
		self.cocina=Cocina()
		self.comedor=Comedor()
		self.cuartoL=CuartoLavado()
		self.cuartoT=CuartoTrabajo()
		self.garaje=Garaje()

	def Pantalla(self,estado,elemento):
		imagen=pygame.image.load("fondo.jpg").convert()
		rectimagen=imagen.get_rect()
		pantalla.blit(imagen,rectimagen)

		#Carga cada uno de los elementos a modificar
		rectv=pygame.Rect(30,70,35,50)
		pygame.draw.rect(pantalla,desactivado,rectv)
		tv=pygame.image.load("televisor.png").convert_alpha()
		pantalla.blit(tv,rectv)

		recluzs=pygame.Rect(85,70,35,50)
		recluzd=pygame.Rect(235,70,35,50)
		recluzb=pygame.Rect(420,70,35,50)
		recluzcom=pygame.Rect(670,70,35,50)
		recluzco=pygame.Rect(30,290,35,50)
		recluzla=pygame.Rect(230,290,35,50)
		recluzof=pygame.Rect(385,290,35,50)
		recluzg=pygame.Rect(550,290,35,50)
		pygame.draw.rect(pantalla,desactivado,recluzs)
		pygame.draw.rect(pantalla,desactivado,recluzd)
		pygame.draw.rect(pantalla,desactivado,recluzb)
		pygame.draw.rect(pantalla,desactivado,recluzcom)
		pygame.draw.rect(pantalla,desactivado,recluzco)
		pygame.draw.rect(pantalla,desactivado,recluzla)
		pygame.draw.rect(pantalla,desactivado,recluzof)
		pygame.draw.rect(pantalla,desactivado,recluzg)
		luz=pygame.image.load("luz.png").convert_alpha()
		pantalla.blit(luz,recluzs)
		pantalla.blit(luz,recluzd)
		pantalla.blit(luz,recluzb)
		pantalla.blit(luz,recluzcom)
		pantalla.blit(luz,recluzco)
		pantalla.blit(luz,recluzla)
		pantalla.blit(luz,recluzof)
		pantalla.blit(luz,recluzg)
		
		recors=pygame.Rect(140,70,35,50)
		record=pygame.Rect(290,70,35,50)
		recorb=pygame.Rect(480,70,35,50)
		recorcom=pygame.Rect(720,70,35,50)
		recorof=pygame.Rect(440,355,35,50)
		pygame.draw.rect(pantalla,desactivado,recors)
		pygame.draw.rect(pantalla,desactivado,record)
		pygame.draw.rect(pantalla,desactivado,recorb)
		pygame.draw.rect(pantalla,desactivado,recorcom)
		pygame.draw.rect(pantalla,desactivado,recorof)
		cortina=pygame.image.load("cortina.png").convert_alpha()
		pantalla.blit(cortina,recors)
		pantalla.blit(cortina,record)
		pantalla.blit(cortina,recorb)
		pantalla.blit(cortina,recorcom)
		pantalla.blit(cortina,recorof)

		recvs=pygame.Rect(30,138,35,50)
		recvd=pygame.Rect(340,70,35,50)
		recvb=pygame.Rect(530,70,35,50)
		recvcom=pygame.Rect(670,138,35,50)
		pygame.draw.rect(pantalla,desactivado,recvs)
		pygame.draw.rect(pantalla,desactivado,recvd)
		pygame.draw.rect(pantalla,desactivado,recvb)
		pygame.draw.rect(pantalla,desactivado,recvcom)
		ventana=pygame.image.load("ventana.png").convert_alpha()
		pantalla.blit(ventana,recvs)
		pantalla.blit(ventana,recvd)
		pantalla.blit(ventana,recvb)
		pantalla.blit(ventana,recvcom)

		recps=pygame.Rect(85,138,35,50)
		recpd=pygame.Rect(235,138,35,50)
		recpb=pygame.Rect(585,70,35,50)
		recpcom=pygame.Rect(720,138,35,50)
		recpco=pygame.Rect(135,290,35,50)
		recplav=pygame.Rect(280,355,35,50)
		recpof=pygame.Rect(440,290,35,50)
		recpg=pygame.Rect(600,290,35,50)
		pygame.draw.rect(pantalla,desactivado,recps)
		pygame.draw.rect(pantalla,desactivado,recpd)
		pygame.draw.rect(pantalla,desactivado,recpb)
		pygame.draw.rect(pantalla,desactivado,recpcom)
		pygame.draw.rect(pantalla,desactivado,recpco)
		pygame.draw.rect(pantalla,desactivado,recplav)
		pygame.draw.rect(pantalla,desactivado,recpof)
		pygame.draw.rect(pantalla,desactivado,recpg)
		puerta=pygame.image.load("puerta.png").convert_alpha()
		pantalla.blit(puerta,recps)
		pantalla.blit(puerta,recpd)
		pantalla.blit(puerta,recpb)
		pantalla.blit(puerta,recpcom)
		pantalla.blit(puerta,recpco)
		pantalla.blit(puerta,recplav)
		pantalla.blit(puerta,recpof)
		pantalla.blit(puerta,recpg)

		recs=pygame.Rect(140,138,35,50)
		pygame.draw.rect(pantalla,desactivado,recs)
		sonido=pygame.image.load("sonido.png").convert_alpha()
		pantalla.blit(sonido,recs)

		recarm=pygame.Rect(290,138,35,50)
		pygame.draw.rect(pantalla,desactivado,recarm)
		armario=pygame.image.load("armario.png").convert_alpha()
		pantalla.blit(armario,recarm)

		recarom=pygame.Rect(420,138,35,50)
		pygame.draw.rect(pantalla,desactivado,recarom)
		aroma=pygame.image.load("aroma.png").convert_alpha()
		pantalla.blit(aroma,recarom)

		relav=pygame.Rect(480,138,35,50)
		relco=pygame.Rect(30,355,35,50)
		pygame.draw.rect(pantalla,desactivado,relav)
		pygame.draw.rect(pantalla,desactivado,relco)
		lavamanos=pygame.image.load("lavamos.png").convert_alpha()
		pantalla.blit(lavamanos,relav)
		pantalla.blit(lavamanos,relco)

		redu=pygame.Rect(530,138,35,50)
		pygame.draw.rect(pantalla,desactivado,redu)
		ducha=pygame.image.load("ducha.png").convert_alpha()
		pantalla.blit(ducha,redu)

		rene=pygame.Rect(85,290,35,50)
		pygame.draw.rect(pantalla,desactivado,rene)
		nevera=pygame.image.load("nevera.png").convert_alpha()
		pantalla.blit(nevera,rene)

		rearm=pygame.Rect(76,355,50,50)
		pygame.draw.rect(pantalla,desactivado,rearm)
		alacena=pygame.image.load("armarioc.png").convert_alpha()
		pantalla.blit(alacena,rearm)

		restuf=pygame.Rect(135,355,40,50)
		pygame.draw.rect(pantalla,desactivado,restuf)
		estufa=pygame.image.load("estufa.png").convert_alpha()
		pantalla.blit(estufa,restuf)

		relava=pygame.Rect(280,290,40,50)
		pygame.draw.rect(pantalla,desactivado,relava)
		lavadora=pygame.image.load("lavadora.png").convert_alpha()
		pantalla.blit(lavadora,relava)

		resec=pygame.Rect(225,355,40,50)
		pygame.draw.rect(pantalla,desactivado,resec)
		secadora=pygame.image.load("secadora.png").convert_alpha()
		pantalla.blit(secadora,resec)

		recomp=pygame.Rect(385,355,40,50)
		pygame.draw.rect(pantalla,desactivado,recomp)
		computador=pygame.image.load("computador.png").convert_alpha()
		pantalla.blit(computador,recomp)

	def Modificar(self,elementosmod,habitacionesmod):
		for i in habitacionesmod:
			if i=='salon'or i=='sala':
				estado,elemento=self.salon.ModificarSalon(elementosmod)
				self.salon.Cambio(pantalla,elemento,estado)
			if i=='dormitorio' or i=='alcoba' or i=='cuarto' or i=='pieza' :
				estado,elemento=self.dormitorio.ModificarDormitorio(elementosmod)
				self.dormitorio.Cambio(pantalla,elemento,estado)
			if i=='bano' or i=='lavavo' or i=='servicio':
				estado,elemento=self.bano.ModificarBano(elementosmod)
				self.bano.Cambio(pantalla,elemento,estado)
			if i=='cocina':
				estado,elemento=self.cocina.ModificarCocina(elementosmod)
				self.cocina.Cambio(pantalla,elemento,estado)
			if i=='comedor' or i=='comedero':
				estado,elemento=self.comedor.ModificarComedor(elementosmod)
				self.comedor.Cambio(pantalla,elemento,estado)
			if i=='lavado' or i=='lavadero':
				estado,elemento=self.cuartoL.ModificarCuartoL(elementosmod)
				self.cuartoL.Cambio(pantalla,elemento,estado)
			if i=='estudio' or i=='oficina':
				estado,elemento=self.cuartoT.ModificarCuartoT(elementosmod)
				self.cuartoT.Cambio(pantalla,elemento,estado)
			if i=='garaje' or i=='cochera':
				estado,elemento=self.garaje.ModificarGaraje(elementosmod)
				self.garaje.Cambio(pantalla,elemento,estado)

pygame.init()
rectv=pygame.Rect(30,70,35,50)
m=Casa()
m.Pantalla(10,None)
pygame.display.flip()

stop=True
elementosmod=[]
habitacionesmod=[]
print "¿En que puedo ayudar?"



while stop:
	instruccion=str(raw_input(">>"))
	if 'y' in instruccion:
		print "Por favor dame una orden simple, un ejemplo puede ser:"
		print "Enciende la luz del comedor" 
	else:
		if instruccion.lower()!='apagar':
			tokens=nltk.word_tokenize(instruccion)
			for i in tokens:
				if i.lower() in habitaciones:
					habitacionesmod.append(i.lower())
				if i.lower() in elementos:
					for j in tokens:
						if j.lower() in acciones0: 
							elementosmod.append([i.lower(),0,j.lower()])
						if j.lower() in acciones1:
							elementosmod.append([i.lower(),1,j.lower()])

			if len(elementosmod)==0 and len(habitacionesmod)==0:
				print "Esta no es una instruccion valida, por favor especifique el objeto"
				print "en el cual quiere que se realice la accion, la accion a realizar y su ubicacion"

			if len(elementosmod)>1 or len(habitacionesmod)>1:
				print "Por favor dame una orden simple, un ejemplo puede ser:"
				print "Enciende la luz del comedor" 
				elementosmod=[]
				habitacionesmod=[]

			if len(habitacionesmod)==0 and len(elementosmod)!=0:
				print "¿En que habitacion quiere realizar la accion?"
				instruccion=str(raw_input(">>"))
				tokens=nltk.word_tokenize(instruccion)
				for i in tokens:
					if i.lower() in habitaciones:
						habitacionesmod.append(i.lower())
					if i.lower() == 'apagar':
						stop=False

			if len(elementosmod)!=0 and len(habitacionesmod)!=0:
				m.Modificar(elementosmod,habitacionesmod)
				elementosmod=[]
				habitacionesmod=[]

			if len(acciones0)==0 and len(acciones1)==0:
				if i.lower()=='apagar':
					stop=False
				else:
					print "No me es posible realizar esta accion"
					elementosmod=[]
					habitacionesmod=[]

			if len(elementosmod)==0 and len(habitacionesmod)!=0:
				if i.lower()=='apagar':
					stop=False
				else:
					print "No logro encontrar el elemento que menciona"
					elementosmod=[]
					habitacionesmod=[]
		else:
			stop=False

	for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=False
	pygame.display.flip()
print "Me apagare, Hasta Luego !!"
