import tkinter as tk

window = tk.Tk()
window.title("Ejercicio 10 - Scrollbar")
window.geometry("400x300")

frame = tk.Frame(window)
frame.pack(fill="both", expand=True, padx=10, pady=10)

scroll = tk.Scrollbar(frame)
scroll.pack(side="right", fill="y")

text = tk.Text(frame, wrap="word", yscrollcommand=scroll.set)
text.pack(side="left", fill="both", expand=True)

scroll.config(command=text.yview)

long_text = """Taylor Alison Swift (West Reading, Pensilvania; 13 de diciembre de 1989) es una cantautora estadounidense. 
Sus composiciones autobiográficas y sus reinvenciones artísticas la han convertido en un icono cultural del siglo XXI. 
Es la artista musical con mayores ingresos por conciertos en directo, 
la mujer más rica del mundo de la música y una de las artistas musicales con más ventas de todos los tiempos.

Swift firmó con Big Machine Records en 2005 y debutó como cantante de country con los álbumes Taylor Swift (2006) y Fearless (2008). 
Los sencillos «Teardrops on My Guitar», 
«Love Story» y «You Belong with Me» cosecharon un gran éxito tanto en las emisoras de radio country como en las de pop. 
Speak Now (2010) amplió su sonido country pop con influencias rock y Red (2012) presentó una producción más pop. 
Su identidad artística del country basculó hacia el pop con el álbum de synth pop 1989 (2014) y el de hip hop Reputation (2017). 
A lo largo de la década de 2010 acumuló los números uno del Billboard Hot 100 «We Are Never Ever Getting Back Together», 
«Shake It Off», «Blank Space», «Bad Blood» y «Look What You Made Me Do», y lanzó el ecléctico álbum pop Lover (2019). 
En la siguiente aparecerían los álbumes indie folk Folklore y Evermore (ambos en 2020), 
y los álbumes pop minimalistas Midnights (2022) y The Tortured Poets Department (2024). 
Entre sus sencillos número uno en la lista Billboard Hot 100 del periodo se encuentran «Cardigan», 
«Willow» o «All Too Well». Su gira The Eras Tour (2023-2024) es la gira de conciertos más taquillera de todos los tiempos. 
La película que la acompaña, The Eras Tour (2023), se convirtió en la película de concierto más taquillera de la historia.

Swift es la primera artista en vender más de un millón de copias de cada uno de sus siete álbumes durante la primera semana 
en Estados Unidos y ha sido nombrada artista discográfica global del año por la IFPI en cinco ocasiones. 
Publicaciones como Rolling Stone y Billboard la han incluido entre los mejores artistas de todos los tiempos. 
Es la primera persona del mundo artístico en ser nombrada persona del año por la revista Time (2023). 
Entre sus galardones se incluyen 14 premios Grammy, entre ellos un récord de cuatro premios al álbum del año, y un premio Primetime Emmy. 
Es la artista más premiada de los premios American Music, los Billboard Music Awards y los MTV Video Music Awards. 
Swift, que es objeto de una amplia cobertura mediática, cuenta con una base global de fanes, conocidos como swifties."""

text.insert("1.0", long_text)

window.mainloop()
