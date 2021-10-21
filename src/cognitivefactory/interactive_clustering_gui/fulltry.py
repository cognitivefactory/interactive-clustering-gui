from tkinter.constants import X


try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import filedialog
    import json
    import re
    from datetime import date
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

SAVEFOLDERPATH = "./"
INIFILEPATH = ""
SESSIONNAME = ""
MODE=0
X = {}

def browseFiles():
        return filedialog.askopenfilename(initialdir="/", title = "Select a File", filetypes=(("CSV files","*.csv"),))

def changeIni():
    global INIFILEPATH
    INIFILEPATH = browseFiles()

def changeSave():
    global SAVEFOLDERPATH 
    SAVEFOLDERPATH = browseFiles()

class App(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (accueil, accueil_import_nom, annotation, commencer, continuer_annot, continuer_cluster):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("accueil")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class accueil(tk.Frame):
    
    def import_nom(self,controller,l):
        changeIni()
        reg = re.compile(".*\\.csv")
        if(re.fullmatch(reg,INIFILEPATH)!=None):
            controller.show_frame("accueil_import_nom")
        else:
            tk.Label(l,text="/!\\ ERREUR D'IMPORTATION /!\\",fg="red").pack()

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        l = tk.LabelFrame(self, text="Bienvenue", padx=20, pady=20)
        l.pack(fill="both", expand="yes")
        tk.Label(l, text="A l'aide des boutons ci-dessous, vous pouvez choisir d'importer un document contenant les questions à traiter au format .csv en cliquant sur Importer.\nVous pouvez aussi choisir de continuer une sessions précédente en cliquant sur Charger.").pack()
        tk.Button(self, text ='Importer',command=lambda: [self.import_nom(controller,l)]).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text ='Charger').pack(side=tk.RIGHT, padx=5, pady=5)


class accueil_import_nom(tk.Frame):

    def get_name(self,string):
        global SESSIONNAME
        SESSIONNAME = string

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        l = tk.LabelFrame(self, text="Bienvenue", padx=20, pady=20)
        l.pack(fill="both", expand="yes")
        tk.Label(l, text="Veuillez nommer votre session").pack()
        entree = tk.Entry(self, width=30)
        tk.Button(self, text ='Valider', command=lambda: [self.get_name(entree.get()),print(SESSIONNAME),controller.show_frame("commencer")]).pack(side=tk.RIGHT, padx=5, pady=5)
        entree.pack()


class annotation(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        l = tk.LabelFrame(self, text="Annotation", padx=20, pady=20)
        l.pack(fill="both", expand="yes")
        tk.Label(l, text="Les deux entrées suivantes ont été trouvées comme similaires. Donneriez-vous la même réponse au deux ? \n Sélectionner :\n - le bouton gauche pour oui\n - le bouton du centre pour je ne sais pas\n - le bouton de droite pour non").pack()
        Zone_de_texte=tk.Text(self,width=50,height=3)
        Zone_de_texte.pack()
        Zone_de_texte2=tk.Text(self,width=50,height=3)
        Zone_de_texte2.pack()
        tk.Button(self, text ='OUI').pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text ='NON').pack(side=tk.RIGHT, padx=5, pady=5)
        tk.Button(self, text ='JE NE SAIS PAS').pack(side=tk.BOTTOM, padx=5, pady=5)

class commencer(tk.Frame):

    def ini_json(self):
        global X
        X = {
            "meta":{
                "session":SESSIONNAME,
                "inifilepath":INIFILEPATH,
                "savefolderpath":SAVEFOLDERPATH,
                "dateCreated":str(date.today()),
                "dateModified":str(date.today())
            },
            "constraints":[],
            "clusteringResults":[]
        }
        #Clustering Initial avec les paramètres
        jsonstring = json.dumps(X)
        with open(SAVEFOLDERPATH + SESSIONNAME + ".json","w") as savefile:
            savefile.write(jsonstring)



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text="Afin de lancer le clustering avec les paramètres par défaut (recommandé),\n appuyez sur COMMENCER.\n Vous pouvez aussi choisir de modifier les paramètres du clustering\n en cliquant sur PARAMETRES").pack()
        tk.Button(self, text ='COMMENCER', command= lambda: [self.ini_json(),controller.show_frame("annotation")]).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text ='PARAMETRES').pack(side=tk.RIGHT, padx=5, pady=5)

class continuer_annot(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text="L'annotation est terminée.\n Souhaitez-vous annoter d'autres couples,\n refaire un clustering ou terminer ?").pack()
        tk.Button(self, text ='ANNOTER').pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text ='TERMINER').pack(side=tk.RIGHT, padx=5, pady=5)
        tk.Button(self, text ='CLUSTERING').pack(side=tk.BOTTOM, padx=5, pady=5)

class continuer_cluster(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text="L'annotation est terminée.\n Souhaitez-vous refaire un clustering ou terminer ?").pack()
        tk.Button(self, text ='CLUSTERING').pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text ='TERMINER').pack(side=tk.RIGHT, padx=5, pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()