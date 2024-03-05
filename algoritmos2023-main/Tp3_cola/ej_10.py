from cola import Cola
'''Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
resolver las siguientes actividades:
a.escribir una función que elimine de la cola todas las notificaciones de Facebook;
b.escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
la palabra ‘Python’, si perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
11:43 y las 15:57, y determinar cuántas son.'''

mensajes = [
    {'hora' : '22:19', 'aplicacion' : 'Facebook', 'mensaje' : 'Osvaldo a cambiado su foto de perfil'},
    {'hora' : '05:45', 'aplicacion' : 'Twitter', 'mensaje' : 'Rojoyblanco24 te compartio un tweet'},
    {'hora' : '12:32', 'aplicacion' : 'Twitter', 'mensaje' : 'Ve la nueva publicacion de Python'},
    {'hora' : '15:06', 'aplicacion' : 'Spotify', 'mensaje' : 'Escucha el nuevo album de Feid'},
    {'hora' : '18:31', 'aplicacion' : 'Instagram', 'mensaje' : 'George Russel a comenzado a seguirte'},
    {'hora' : '23:20', 'aplicacion' : 'Facebook', 'mensaje' : 'A 235 personas le gusto tu publicacion'},
]

cola = Cola(mensajes)
cola.mostrar_mensajes_twitter()
cola.eliminar_mensajes_facebook()
horario = cola.almacenar_mensajes_pila()
print(f'{len(horario)} mensajes se produjeron entre las 11:43 y las 15:57')
print(cola)
print(cola.mensajes)
