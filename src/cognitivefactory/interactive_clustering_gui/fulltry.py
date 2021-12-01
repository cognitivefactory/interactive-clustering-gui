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
    from constraints.factory import *
    from sampling.factory import *
    from clustering.factory import *
    from utils.vectorization import *
    from utils.preprocessing import preprocess
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

SAVEFOLDERPATH = "./"
INIFILEPATH = ""
SESSIONNAME = ""
MODE=0
X = {}
SEED = random.seed()
MANAGER = None
SAMPLER = sampling_factory("random")
NBANNOTATIONS = 3
REQRESULTS = 0
RESULTINGVECTORS = {}

def browseFiles():
        return filedialog.askopenfilename(initialdir="/", title = "Select a File", filetypes=(("CSV files","*.csv"),))

def browseFiles2():
        return filedialog.askopenfilename(initialdir="/", title = "Select a File", filetypes=(("JSON files","*.json"),))

def browseDirectories():
        return filedialog.askdirectory(initialdir="/",title="Select a directory")

def changeIni():
    global INIFILEPATH
    INIFILEPATH = browseFiles()

def changeSave():
    global SAVEFOLDERPATH 
    SAVEFOLDERPATH = browseFiles2()

def changeSave2():
    global SAVEFOLDERPATH
    SAVEFOLDERPATH = browseDirectories() + "/"

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
            global MANAGER
            with open(INIFILEPATH) as file:
                lines = file.readlines()
                n = len(lines)
                ids = [str(i) for i in range(0,n)]
                MANAGER = managing_factory(ids)
            for i in X["constraints"]:
                MANAGER.add_constraint(str(i["ID1"]),str(i["ID2"]),i["type"])
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
    samples = []
    number = 0
    questions=[]

    def Get_questions(self):
        file = open(INIFILEPATH)
        reader=csv.reader(file)
        self.questions = list(reader)
        print(self.questions)

    def Get_IDs(self):
        ID1 = int(self.samples[self.number][0])
        ID2 = int(self.samples[self.number][1])
        self.number = self.number+1
        print(ID1,ID2)
        return (ID1,ID2)
    
    def new_annotations(self,Zone1,Zone2,b,c,e):
        if (MANAGER.check_completude_of_constraints()):
            tk.Label(self,text="Toutes les contraintes possibles ont été annotées.").pack(side=tk.TOP,padx=5,pady=5)
        else:
            if(self.number < len(self.samples)):
                (ID1,ID2) = self.Get_IDs()
                Zone1.config(state="normal")
                Zone1.delete("1.0","end")
                print(self.questions[ID1][0])
                Zone1.insert("end",self.questions[ID1][0])
                Zone1.config(state="disabled")
                Zone2.config(state="normal")
                Zone2.delete("1.0","end")
                Zone2.insert("end",self.questions[ID2][0])
                Zone2.config(state="disabled")
                self.ID1 = ID1
                self.ID2 = ID2
            else:
                d = tk.Button(self,text="Continuer l'Annotation",command=lambda:[self.ini_sampling(MANAGER,NBANNOTATIONS),self.new_annotations(Zone1,Zone2,b,c,e),d.pack_forget(),b.pack(side=tk.LEFT, padx=5, pady=5),c.pack(side=tk.RIGHT, padx=5, pady=5),e.pack(side=tk.BOTTOM, padx=5, pady=5)])
                Zone1.delete('1.0','end')
                Zone2.delete('1.0','end')
                e.pack_forget()
                b.pack_forget()
                c.pack_forget()
                d.pack(side=tk.TOP,padx=5,pady=5)
                self.number=0

    def annoter(self,annotype,l):
        global X
        X["constraints"].append({
            "ID1":self.ID1,
            "ID2":self.ID2,
            "type":annotype
        })
        if(not MANAGER.add_constraint(str(self.ID1),str(self.ID2),annotype)):
            tk.Label(l,text="/!\\ ERREUR CONTRAINTE /!\\",fg="red").pack()
        
    def ini_sampling(self,manager,nb):
        if(REQRESULTS==0):
            self.samples=SAMPLER.sample(manager,nb)
        else:
            self.samples=SAMPLER.sample(manager,nb,X["clusteringResults"][-1],RESULTINGVECTORS)
        print("Sampler Created")
        print(self.samples)


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
        b = tk.Button(self, text ='OUI',command=lambda:[self.annoter("MUST_LINK",l),
        self.new_annotations(Zone_de_texte,Zone_de_texte2,b,c,e)])
        c = tk.Button(self, text ='NON',command=lambda:[self.annoter("CANNOT_LINK",l),
        self.new_annotations(Zone_de_texte,Zone_de_texte2,b,c,e)])
        e = tk.Button(self, text ='JE NE SAIS PAS',command=lambda:[self.new_annotations(Zone_de_texte,Zone_de_texte2,b,c,e)])
        a = tk.Button(self,text="Commencer",command=lambda:[self.ini_sampling(MANAGER,NBANNOTATIONS),
        self.Get_questions(),self.new_annotations(Zone_de_texte,Zone_de_texte2,b,c,e),
        a.pack_forget(),b.pack(side=tk.LEFT, padx=5, pady=5),
        c.pack(side=tk.RIGHT, padx=5, pady=5),
        e.pack(side=tk.BOTTOM, padx=5, pady=5)])
        a.pack(side=tk.TOP,padx=5,pady=5)
        tk.Button(self, text ='Sauvegarder',command=lambda:save()).pack(side=tk.BOTTOM,padx=5,pady=5)
        tk.Button(self, text ='Clustering',command=lambda:[save(),Zone_de_texte.delete('1.0','end'),
        Zone_de_texte2.delete('1.0','end'),
        a.pack(side=tk.TOP,padx=5,pady=5),
        controller.show_frame("clustering")]).pack(side=tk.TOP,padx=5,pady=5)

class commencer(tk.Frame):

    def sauvcommand(self,label):
        changeSave2()
        label["text"]=SAVEFOLDERPATH

    def appliquercommand(self,scale,menu):
        global NBANNOTATIONS
        NBANNOTATIONS = scale.get()
        a = menu.get()
        global SAMPLER
        global REQRESULTS
        if(a=="Random in same cluster"):
            SAMPLER = sampling_factory("random_in_same_cluster")
            REQRESULTS = 1
        elif(a=="Farthest in same cluster"):
            SAMPLER = sampling_factory("farthest_in_same_cluster")
            REQRESULTS = 1
        elif(a=="closest in different clusters"):
            SAMPLER = sampling_factory("closest_in_different_clusters")
            REQRESULTS = 1
        print(a)




    def settings(self):
        window = tk.Tk()
        window.title('Session Settings')
        window.geometry('200x400')
        appliquer = tk.Button(window,text="Appliquer",command=lambda:[self.appliquercommand(annot,select),window.destroy()])
        label1 = tk.Label(window,text=SAVEFOLDERPATH)
        sauv = tk.Button(window,text="Modifier Emplacement de Sauvegarde",command=lambda:[self.sauvcommand(label1)])
        label2 = tk.Label(window,text="Annotations par itération:")
        annot = tk.Scale(window,from_=1,to=30,orient=HORIZONTAL)
        label3 = tk.Label(window,text="Méthode d'échantillonage:")
        select = tk.StringVar(window)
        select.set("Random")
        options = ["Random","Random in same cluster", "Farthest in same cluster", "closest in different clusters"]
        echan = tk.OptionMenu(window,select,*options)
        annot.set(5)
        label1.pack(side=tk.TOP)
        sauv.pack(side=tk.TOP)
        label2.pack(side=tk.TOP)
        annot.pack(side=tk.TOP)
        label3.pack(side=tk.TOP)
        echan.pack(side=tk.TOP)
        appliquer.pack(side=tk.BOTTOM)
        window.mainloop()

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

    def ini_manager(self):
        global MANAGER
        with open(INIFILEPATH) as file:
            lines = file.readlines()
            n = len(lines)
        ids = [str(i) for i in range(0,n)]
        MANAGER = managing_factory(ids)
        print(MANAGER.get_list_of_managed_data_IDs())


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text="Afin de lancer le clustering avec les paramètres par défaut (recommandé),\n appuyez sur COMMENCER.\n Vous pouvez aussi choisir de modifier les paramètres du clustering\n en cliquant sur PARAMETRES").pack()
        tk.Button(self, text ='COMMENCER', command= lambda: [self.ini_manager(),
        self.ini_json(),
        controller.show_frame("clustering")]).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text ='PARAMETRES',command=lambda:[
            self.settings()
        ]).pack(side=tk.RIGHT, padx=5, pady=5)

class clustering(tk.Frame):
    
    CLUSTERINGTYPE="kmeans"
    nb_clusters = 3
    d={"ini":"ini"}
    
    def appliqcommand(self,text,nb):
        self.CLUSTERINGTYPE = text
        self.nb_clusters=nb

    def settings(self):
        window = tk.Tk()
        window.title('Session Settings')
        window.geometry('200x400')
        appliq = tk.Button(window,text="Appliquer",command=lambda:[self.appliqcommand(select.get(),clust.get()),window.destroy()])
        label1 = tk.Label(window,text="Méthode de Classification:")
        select = tk.StringVar(window)
        select.set("kmeans")
        options = ["kmeans","hierarchical","spectral"]
        classi = tk.OptionMenu(window,select,*options)
        label2 = tk.Label(window,text="Nombre de clusters:")
        clust = tk.Scale(window,from_=2,to=20,orient=HORIZONTAL)
        clust.set(3)
        label1.pack(side=tk.TOP)
        classi.pack(side=tk.TOP)
        label2.pack(side=tk.TOP)
        clust.pack(side=tk.TOP)
        appliq.pack(side=tk.BOTTOM)
        window.mainloop()

    def clusterize(self,clusteringtype,controller,p,l,progress):
        model = clustering_factory(clusteringtype)
        file = open(INIFILEPATH)
        reader=csv.reader(file)
        questions = list(reader)
        ini = []
        for i in questions:
            ini.append(i[0])
        print(ini)
        keys = [str(i) for i in range(0,len(ini))]
        if(self.d=={"ini":"ini"}):
            a = dict(zip(keys,ini))
            print(a)
            self.d=vectorize(preprocess(a))
            global RESULTINGVECORS
            RESULTINGVECTORS = self.d
        results = model.cluster(MANAGER,self.d,self.nb_clusters)
        global X
        X["clusteringResults"].append(results)
        d = tk.Button(self,text="Passer à l'annotation",command=lambda:[progress.pack_forget(),
        d.pack_forget(),
        f.pack_forget(),
        p.pack(side=tk.RIGHT, padx=5, pady=5),
        l.pack(side=tk.BOTTOM, padx=5, pady=5),
        controller.show_frame("annotation")])
        d.pack(side=tk.BOTTOM)
        f = tk.Button(self,text="Sauvegarder",command=lambda:save())
        f.pack(side=tk.BOTTOM)




    def bar(self,progress):
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
            

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        progress = Progressbar(self,orient=HORIZONTAL,length=100,mode="determinate")
        tk.Label(self, text="L'annotation est terminée.\n Souhaitez-vous annoter d'autres couples,\n refaire un clustering ou terminer ?").pack()
        p = tk.Button(self, text ='Paramètres',command=lambda:[self.settings()])
        p.pack(side=tk.RIGHT, padx=5, pady=5)
        l = tk.Button(self, text ='Lancer le Clustering',command=lambda:[progress.pack(pady=10),
        self.clusterize(self.CLUSTERINGTYPE,controller,l,p,progress),
        self.bar(progress),
        l.pack_forget(),
        p.pack_forget()])
        l.pack(side=tk.BOTTOM, padx=5, pady=5)




if __name__ == "__main__":
    app = App()
    app.mainloop()