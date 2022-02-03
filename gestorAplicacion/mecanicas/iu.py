class Iu():
    escenaActual = 0
    allEscenas = []
    
    narrativa = None
    opcion_1 = None
    opcion_1_nar = None
    opcion_2_nar = None
    hayCombate = None

    class Escena:
        idEscena = int
        narracion = []
        narrativa = ""
        opciones = []
        hayCombate = False
        escenaFinal = False
        enemigo = ""	
    
    def __init__(self):
        self.allEscenas = []

    def escenario(self):
        
        escena0 = self.Escena()
        escena0.hayCombate = False
        escena0.idEscena = 0
		
        escena0.narrativa = """Capítulo 1 - Oculto tras las sombras"+"\n\nLa zozobra se había instalado en los habitantes del lejano poblado de Campoverde. Atrás habían quedado los días donde los párvulos retoños de Campoverde
jugaban a las escondidillas en los frondosos bosques limítrofes. Una invisible amenaza se arrastraba por la región, las desapariciones y asesinatos cada
vez eran más frecuentes y el alcalde Dientemayor había reunido cuadrillas de exploración para contrarrestar la amenaza oculta tras las sombras.\n
Has decidido no quedarte de brazos cruzados, pues al no haber cumplido aún la mayoría de edad, los adultos del lugar decidieron que no podrías ser parte
de la delegación. Has tomado prestada la espada corta y el pequeño escudo de tu abuelo Timun Haldegarth, el otrora gran guerrero del reino de Erzia.\n
Has esperado el anochecer para ir más allá de la amurallada aldea y ahora un cielo estrellado ilumina tenuemente tu trayecto hacia los bosques de Campoverde.
Conoces cada rincón del bosque, pues han sido incontables las idas y venidas a través de él, te es fácil reconocer un casi desapercibido camino que se proyecta
a un costado del camino principal, lo recorres hasta llegar al pie de una colina. Un montón de piedras se apilan en frente tuyo."""
        
        escena0.opciones = ["Echar un vistazo al cúmulo de piedras", 1, "Rodear la colina", 2]
        
        self.allEscenas.append(escena0)
	
        escena1 = self.Escena()
        escena1.hayCombate = False
        escena1.idEscena = 1
        escena1.narrativa = """El cúmulo de rocas no parece ser una formación natural. Un olor a sopa nauseabunda y leños quemándose parece proceder de alguna caverna oculta tras
las piedras."""
        escena1.opciones = ["Echar un vistazo a través de los agujeros entre las rocas", 3, "Tumbar las rocas haciendo uso de la fuerza bruta", 4]
        self.allEscenas.append(escena1)

		
        escena2 = self.Escena()
        escena2.hayCombate = True
        escena2.enemigo = "goblin"
        escena2.idEscena = 2
        escena2.narrativa = """Luego de luchar contra aquella alimaña, retornas al cúmulo de piedras y decides que es mejor echar un vistazo, seguramente ese goblin tiene relación
con aquella misteriosa pila.\nEl cúmulo de rocas no parece ser una formación natural. Un olor a sopa nauseabunda y leños quemándose parece proceder de alguna
caverna oculta tras las piedras."""
        escena2.opciones = ["Echar un vistazo a través de los agujeros entre las rocas", 3, "Tumbar las rocas haciendo uso de la fuerza bruta", 4]
        self.allEscenas.append(escena2)
		
        escena3 = self.Escena()
        escena3.hayCombate = False
        escena3.idEscena = 3
        escena3.narrativa = """Ves a un goblin haciendo guardia, aunque parece estar próximo a quedarse dormido el diligente esbirro. En ese preciso momento llega
un segundo guardia, mucho más fornido que el anterior y en aparente estado de embriaguez, tienta al atento guardia para abandonar su puesto de trabajo
para tomarse un par de hidromieles salvajes, pues al fin y al cabo: ¿quién podría descifrar el acertijo mágico que protege aquella entrada?
Ambas criaturas desaparecen -junto con su olor- quedando la entrada libre."""
        escena3.opciones = ["Buscar en las rocas algo relacionado con aquel acertijo", 5, "Tumbar las rocas haciendo uso de la fuerza bruta", 4]
        self.allEscenas.append(escena3)

        escena4 = self.Escena()
        escena4.hayCombate = True
        escena4.enemigo = "goblin"
        escena4.idEscena = 4
        escena4.narrativa = """Después de la ingeniosa decisión, la entrada a la caverna ha quedado despejada,
siendo esta iluminada solo por la pálida luna."""
        escena4.opciones = ["Adentrarse en la caverna", 6, "Es muy peligroso seguir adelante yo solo. Volveré al pueblo y le contaré a los adultos.", 6]
        self.allEscenas.append(escena4)

        escena5 = self.Escena()
        escena5.hayCombate = False
        escena5.idEscena = 5
        escena5.narrativa = """Lo que a primera vista pasa desapercibido, ante tu mirada atenta se deja ver una inscripción en el lenguaje de los elfos,
que reconoces fácilmente, pues Windalf, el viego mago, te instruyó en esta bella lengua años atrás."""
        escena5.opciones = ["Descifrar el acertijo", 7, "Tumbar las rocas haciendo uso de la fuerza bruta", 4]
        self.allEscenas.append(escena5)


        escena6 = self.Escena()
        escena6.escenaFinal = True
        escena6.hayCombate = False
        escena6.idEscena = 6
        escena6.narrativa = "Hasta acá la demo."
        self.allEscenas.append(escena6)
		
        escena7 = self.Escena()
        escena7.hayCombate = False
        escena7.idEscena = 7
        escena7.narrativa = """Con mucho orgullo pero poca sabiduría, malogras el hechizo y derribas las piedras que cubren la entrada a la caverna,
alertando así los guardas, iniciándose un combate feroz bajo la mortecina luz de la luna."""
        escena7.opciones = ["Adentrarse en la caverna", 6, "Es muy peligroso seguir adelante yo solo. Volveré al pueblo y le contaré a los adultos.", 6]
        self.allEscenas.append(escena7)

    def getEscena(self, seleccion):    
        self.narrativa = self.allEscenas[seleccion].narrativa
        self.opcion_1 = self.allEscenas[seleccion].opciones[1]
        self.opcion_2 = self.allEscenas[seleccion].opciones[3]
        self.opcion_1_nar = self.allEscenas[seleccion].opciones[0]
        self.opcion_2_nar = self.allEscenas[seleccion].opciones[2]
        self.hayCombate = self.allEscenas[seleccion].hayCombate
        #return escena(self.allEscenas[seleccion].narrativa, self.allEscenas[seleccion].opciones[1], )




#iu = Iu()
#escenario = iu.escenario()
#iu.getEscena(0)