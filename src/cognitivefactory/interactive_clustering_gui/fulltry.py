from tkinter.constants import HORIZONTAL, X


try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import filedialog
    from tkinter.ttk import *
    import json
    import re
    from datetime import date
    import random
    import csv
    import time
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

SAVEFOLDERPATH = "./"
INIFILEPATH = ""
SESSIONNAME = ""
MODE=0
X = {}
SEED = random.seed()

def browseFiles():
        return filedialog.askopenfilename(initialdir="/", title = "Select a File", filetypes=(("CSV files","*.csv"),))

def browseFiles2():
        return filedialog.askopenfilename(initialdir="/", title = "Select a File", filetypes=(("JSON files","*.json"),))

def changeIni():
    global INIFILEPATH
    INIFILEPATH = browseFiles()

def changeSave():
    global SAVEFOLDERPATH 
    SAVEFOLDERPATH = browseFiles2()

def save():
    print(SAVEFOLDERPATH + SESSIONNAME + ".json")
    with open(SAVEFOLDERPATH + SESSIONNAME + ".json","w") as savefile:
            savefile.write(json.dumps(X))

class App(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (accueil, accueil_import_nom, annotation, commencer, clustering):
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

    def import_session(self,controller,l):
        changeSave()
        global SAVEFOLDERPATH
        reg = re.compile(".*\\.json")
        if(re.fullmatch(reg,SAVEFOLDERPATH)!=None):
            global MODE
            MODE = 1
            global X
            file = open(SAVEFOLDERPATH)
            editable = SAVEFOLDERPATH.split('/')[0:-1]
            SAVEFOLDERPATH = '/'.join(editable) + '/'
            print(SAVEFOLDERPATH)
            X = json.load(file)
            global SESSIONNAME
            global INIFILEPATH
            SESSIONNAME = X["meta"]["session"]
            INIFILEPATH = X["meta"]["inifilepath"]
            
            controller.show_frame("clustering")
        else:
            tk.Label(l,text="/!\\ ERREUR D'IMPORTATION /!\\",fg="red").pack()

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        l = tk.LabelFrame(self, text="Bienvenue", padx=20, pady=20)
        l.pack(fill="both", expand="yes")
        tk.Label(l, text="A l'aide des boutons ci-dessous, vous pouvez choisir d'importer un document contenant les questions à traiter au format .csv en cliquant sur Importer.\nVous pouvez aussi choisir de continuer une sessions précédente en cliquant sur Charger.").pack()
        tk.Button(self, text ='Importer',command=lambda: [self.import_nom(controller,l)]).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text ='Charger',command=lambda: self.import_session(controller,l)).pack(side=tk.RIGHT, padx=5, pady=5)


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
    ini = 0
    ID1=0
    ID2=0
    questions=[]

    def Get_questions(self):
        file = open(INIFILEPATH)
        reader=csv.reader(file)
        self.questions = list(reader)

    def Get_IDs(self):
        lines=len(self.questions)
        ID1=random.randint(0,lines-1)
        ID2=ID1
        while(ID2==ID1):
            ID2=random.randint(0,lines-1)
        return (ID1,ID2)
    
    def new_annotations(self,Zone1,Zone2):
        (ID1,ID2) = self.Get_IDs()
        Zone1.config(state="normal")
        Zone1.delete("1.0","end")
        Zone1.insert("end",self.questions[ID1][0])
        Zone1.config(state="disabled")
        Zone2.config(state="normal")
        Zone2.delete("1.0","end")
        Zone2.insert("end",self.questions[ID2][0])
        Zone2.config(state="disabled")
        self.ID1 = ID1
        self.ID2 = ID2

    def annoter(self,annotype):
        global X
        X["constraints"].append({
            "ID1":self.ID1,
            "ID2":self.ID2,
            "type":annotype
        })
        



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        l = tk.LabelFrame(self, text="Annotation", padx=20, pady=20)
        l.pack(fill="both", expand="yes")
        tk.Label(l, text="Les deux entrées suivantes ont été trouvées comme similaires. Donneriez-vous la même réponse au deux ? \n Sélectionner :\n - le bouton gauche pour oui\n - le bouton du centre pour je ne sais pas\n - le bouton de droite pour non").pack()
        Zone_de_texte=tk.Text(self,width=50,height=3,state="disabled")
        Zone_de_texte.pack()
        Zone_de_texte2=tk.Text(self,width=50,height=3,state="disabled")
        Zone_de_texte2.pack()
        a = tk.Button(self,text="Commencer",command=lambda:[self.Get_questions(),self.new_annotations(Zone_de_texte,Zone_de_texte2),a.pack_forget()])
        a.pack(side=tk.TOP,padx=5,pady=5)
        tk.Button(self, text ='OUI',command=lambda:[self.annoter("MUST_LINK"),self.new_annotations(Zone_de_texte,Zone_de_texte2)]).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text ='NON',command=lambda:[self.annoter("CANNOT_LINK"),self.new_annotations(Zone_de_texte,Zone_de_texte2)]).pack(side=tk.RIGHT, padx=5, pady=5)
        tk.Button(self, text ='JE NE SAIS PAS',command=lambda:[self.new_annotations(Zone_de_texte,Zone_de_texte2)]).pack(side=tk.BOTTOM, padx=5, pady=5)
        tk.Button(self, text ='Sauvegarder',command=lambda:save()).pack(side=tk.BOTTOM,padx=5,pady=5)
        tk.Button(self, text ='Clustering',command=lambda:[save(),Zone_de_texte.delete('1.0','end'),Zone_de_texte2.delete('1.0','end'),a.pack(side=tk.TOP,padx=5,pady=5),controller.show_frame("clustering")]).pack(side=tk.TOP,padx=5,pady=5)

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
        save()



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text="Afin de lancer le clustering avec les paramètres par défaut (recommandé),\n appuyez sur COMMENCER.\n Vous pouvez aussi choisir de modifier les paramètres du clustering\n en cliquant sur PARAMETRES").pack()
        tk.Button(self, text ='COMMENCER', command= lambda: [self.ini_json(),controller.show_frame("clustering")]).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text ='PARAMETRES').pack(side=tk.RIGHT, padx=5, pady=5)

class clustering(tk.Frame):

    def bar(self,progress,controller,l,p):
            progress['value'] = 20
            self.update_idletasks()
            time.sleep(1)
        
            progress['value'] = 40
            self.update_idletasks()
            time.sleep(1)
        
            progress['value'] = 50
            self.update_idletasks()
            time.sleep(1)
        
            progress['value'] = 60
            self.update_idletasks()
            time.sleep(1)
        
            progress['value'] = 80
            self.update_idletasks()
            time.sleep(1)
            progress['value'] = 100
            d = tk.Button(self,text="Passer à l'annotation",command=lambda:[progress.pack_forget(),d.pack_forget(),f.pack_forget(),p.pack(side=tk.RIGHT, padx=5, pady=5),l.pack(side=tk.BOTTOM, padx=5, pady=5),controller.show_frame("annotation")])
            d.pack(side=tk.BOTTOM)
            f = tk.Button(self,text="Sauvegarder",command=lambda:save())
            f.pack(side=tk.BOTTOM)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        progress = Progressbar(self,orient=HORIZONTAL,length=100,mode="determinate")
        tk.Label(self, text="L'annotation est terminée.\n Souhaitez-vous annoter d'autres couples,\n refaire un clustering ou terminer ?").pack()
        p = tk.Button(self, text ='Paramètres')
        p.pack(side=tk.RIGHT, padx=5, pady=5)
        l = tk.Button(self, text ='Lancer le Clustering',command=lambda:[progress.pack(pady=10),self.bar(progress,controller,l,p),l.pack_forget(),p.pack_forget()])
        l.pack(side=tk.BOTTOM, padx=5, pady=5)




if __name__ == "__main__":
    app = App()
    app.mainloop()