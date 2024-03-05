class Cola:
    def __init__(self, mensajes):
        self.mensajes = mensajes

    def eliminar_mensajes_facebook(self):
        mensajes_copia = self.mensajes.copy()
        for mensaje in mensajes_copia:
            if mensaje['aplicacion'] == 'Facebook':
                self.mensajes.remove(mensaje)

    def mostrar_mensajes_twitter(self):
        for i in range(len(self.mensajes)):
            if self.mensajes[i]['aplicacion'] == 'Twitter' and 'Python' in self.mensajes[i]['mensaje']:
                print(self.mensajes[i])

    def almacenar_mensajes_pila(self):
        pila = []
        for i in range(len(self.mensajes)):
            if '11:43' <= self.mensajes[i]['hora'] <= '15:57':
                pila.append(self.mensajes[i])
        return pila
