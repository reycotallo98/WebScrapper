import tkinter
import requests, bs4
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import platform


def scrap(URL, a):
    htm = []
    print('hola')
    if a != 0 or type(URL) == list:

        for cambio in range(0, a + 1):
            url = requests.get(URL.format(cambiante=cambio))
            htm.append(bs4.BeautifulSoup(url.text, 'lxml'))
        print(htm[0].text)
        return htm


    else:
        url = requests.get(URL)
        htm.append(bs4.BeautifulSoup(url.text, 'html.parser'))
        print(htm[0])
        return htm


class ventana:
    if format(platform.system()) == 'Windows':
        def __init__(self):

            # generamos la app para Windows, con responsibidad
            self.ruta = ''
            self.window = Tk()
            self.fullScreenState = False
            self.window.attributes("-fullscreen", self.fullScreenState)

            self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
            self.window.geometry("%dx%d" % (self.w, self.h))

            self.window.bind("<F11>", self.toggleFullScreen)
            self.window.bind("<Escape>", self.quitFullScreen)
            self.window.title('WebScrapper by reycotallo98')
            self.window.config(bg='black')

            # Creamos el grid principal
            Panel_Sup = Frame(self.window, bd=2, relief=FLAT)
            Panel_Sup.pack(side=TOP)
            Panel_Sup.config(bg='black')

            Panel_izquierdo = Frame(self.window, bd=2, relief=FLAT, bg='azure4')
            Panel_izquierdo.pack(side=LEFT)

            Panel_derecho = Frame(self.window, bd=2, relief=FLAT)
            Panel_derecho.pack(side=RIGHT)

            etiqueta_titulo = Label(Panel_Sup,
                                    text='WebScraper by reycotallo98',
                                    fg='gold',
                                    font=('Dosis', 30),
                                    bg='black',
                                    justify=LEFT)
            etiqueta_titulo.grid(row=0, column=0)

            text_URL = Label(Panel_Sup,
                             text='Introduce aqui tu URL',
                             fg='white',
                             font=('Dosis', 15),
                             bg='black',
                             justify=tkinter.LEFT,

                             )
            text_URL.grid(row=1, column=0)

            etiqueta_Scrapper = Label(Panel_izquierdo,
                                      text='Scrapping Config',
                                      fg='gold',
                                      font=('Dosis', 20),
                                      bg='black',
                                      anchor=tkinter.CENTER)
            etiqueta_Scrapper.grid(row=0, column=0)
            """VARIABLES
                        URL"""
            self.URL_toScrap = StringVar()

            # CUADRO DE URL
            self.URLtoScrap = Entry(Panel_Sup,
                                    font=('Dosis', 18),
                                    fg=self._from_rgb((116, 225, 0)),
                                    bd=1,
                                    width=int(self.w / 40),
                                    bg='black',
                                    state=NORMAL,
                                    textvariable=self.URL_toScrap)
            self.URLtoScrap.grid(row=3, column=0)
            # CUADRO VISUALIZADOR DE HTML

            self.htmlViewer = Text(Panel_derecho,
                                   font=('Dosis', 12),
                                   bd=1,
                                   width=int(self.w / 13),
                                   height=int(self.h / 23),
                                   bg='black',
                                   fg='white')
            self.htmlViewer.grid(row=0, column=0)
            '''
                        checkbutton multipagina
                        '''

            '''
            urlmultipagina

            '''
            # multipagina?
            self.URL2 = StringVar()
            self.url2 = Entry(Panel_izquierdo,
                              font=('Dosis', 18),
                              fg=self._from_rgb((116, 225, 0)),
                              bd=1,
                              width=45,
                              bg='black',
                              state=DISABLED,
                              textvariable=self.URL2)
            self.url2.grid(row=2, column=0)
            self.N_pag = IntVar()
            self.numero_pag = Entry(Panel_izquierdo,
                                    font=('Dosis', 18),
                                    fg=self._from_rgb((116, 225, 0)),
                                    bd=1,
                                    width=2,
                                    bg='black',
                                    state=DISABLED,
                                    textvariable=self.N_pag)
            self.N_pag.set(0)
            self.numero_pag.grid(row=2, column=1)
            self.var_multipagina = IntVar()

            self.multipagina = Checkbutton(Panel_izquierdo,
                                           text='Si quieres que tu Scrapping se realice en modo multipagina\nSustituye la parte que cambie en al url por "{cambiante}" en la url\n y su numero de paginas',
                                           font=('Dosis', 16),
                                           onvalue=1, offvalue=0,
                                           bg='azure4',
                                           variable=self.var_multipagina,
                                           command=self.activar_url2)
            self.multipagina.grid(row=1, column=0)
            self.busqueda = StringVar()
            self.lista = ttk.Combobox(Panel_izquierdo,
                                      state=DISABLED,
                                      textvariable=self.busqueda
                                      )
            self.lista.grid(row=4, column=0)

            self.but = Button(Panel_izquierdo, text='A Scrapear',
                              font=('Dosis', 14),
                              fg='white',
                              bg='black',
                              width=9,
                              justify=RIGHT)
            self.but.grid(row=3, column=0)
            self.but.config(command=lambda: self.mostrar(scrap(self.URL_toScrap.get(), 0)) if (
                    self.var_multipagina.get() == 0) else self.mostrar(scrap(self.url2.get(), self.N_pag.get())))
            # Cuadro de Scrapping config
            self.atributos = []
            self.botones = []
            self.VariablesCheckbox = []
            self.panelcheck = Frame(Panel_izquierdo,
                                    height=50,
                                    bg='azure4')
            self.panelcheck.grid(row=4, column=0)

            self.excavar = Button(Panel_izquierdo,
                                  text='excavar',
                                  fg='black',
                                  bg='azure2',
                                  width=6,
                                  font=('Dosis', 14),
                                  state=DISABLED)
            self.excavar.grid(row=5, column=0)
            self.botonScrap = Button(Panel_izquierdo,
                                     text='Scrapear',
                                     fg='black',
                                     bg='azure2',
                                     width=6,
                                     font=('Dosis', 14),
                                     state=DISABLED)
            self.botonScrap.grid(row=5, column=1)
            self.botonScrap.config(command=lambda: self.escarvar())
            self.window.mainloop()

        def _from_rgb(self, rgb):
            """translates an rgb tuple of int to a tkinter friendly color code
            """
            return "#%02x%02x%02x" % rgb

        def toggleFullScreen(self, event):
            self.fullScreenState = not self.fullScreenState
            self.window.attributes("-fullscreen", self.fullScreenState)

        def quitFullScreen(self, event):
            self.fullScreenState = False
            self.window.attributes("-fullscreen", self.fullScreenState)
    else:
        # generamos la app para linux o mac con responsividad
        def __init__(self):
            self.window = Tk()
            self.window.attributes('-zoomed', True)
            self.fullScreenState = False
            self.window.bind("<F11>", self.toggleFullScreen)
            self.window.bind("<Escape>", self.quitFullScreen)

            self.window.mainloop()

        def toggleFullScreen(self, event):
            self.fullScreenState = not self.fullScreenState
            self.window.attributes("-zoomed", self.fullScreenState)

        def quitFullScreen(self, event):
            self.fullScreenState = False
            self.window.attributes("-zoomed", self.fullScreenState)

        def _from_rgb(rgb):
            """translates an rgb tuple of int to a tkinter friendly color code
            """
            return "#%02x%02x%02x" % rgb

    def escarvar(self):
        l = []
        self.ruta = self.ruta + self.busqueda.get()
        for a in self.scraper:
            l.append(a.select(self.ruta))
        self.htmlViewer.delete(1.0, END)
        print(l)
        for a in l[0]:
            self.htmlViewer.insert(END, a)
        return ''

    def mostrar(self, a):
        self.htmlViewer.delete(1.0, END)
        self.scraper = a
        self.lista.config(state=NORMAL)
        self.htmlViewer.insert(END, a[0])
        messagebox.showinfo('Importante',
                            'Para scrapear la pagina:\n-Uso de los desplegables: \nEstos mostraran los hijos del elemento seleccionado, al seleccionar alguno \neste se actualizara mostrando los siguientes hijos\nUso del cuadro de texto:\n Este se usa para buscar por clases o ids , deberás usarlo cuando hayas encontrado lo que buscas\n se rellena poniendo ".nombredeclase" o "#nombreid", se pueden concatenar varios nombres\nLos checkbuttons son para seleccionar los datos que te interesan')
        self.but.config(state=DISABLED)
        self.lista.config(state=NORMAL)
        m = []
        for l in self.scraper[0].findAll():
            print(l)
            m.append(l.__str__()[1:l.__str__().find(' ')][0:4])
        m = list(set(m))
        self.lista['values'] = m
        self.botonScrap.config(state=NORMAL)
        self.excavar.config(state=NORMAL)
        return ''

    def actualizar(self):
        a = []
        for a in self.scraper:
            a.select(self.ListValue)

    def activar_url2(self):

        if self.var_multipagina.get() == 1:
            self.url2.config(state=NORMAL)
            self.numero_pag.config(state=NORMAL)
            self.URL2.set(self.textoURL())
            return ''
        else:
            self.url2.config(state=DISABLED)
            self.URL2.set('')
            self.numero_pag.config(state=DISABLED)
            self.N_pag.set('0')
            return ''

    def textoURL(self):
        return self.URL_toScrap.get()


if __name__ == '__main__':
    app = ventana()
