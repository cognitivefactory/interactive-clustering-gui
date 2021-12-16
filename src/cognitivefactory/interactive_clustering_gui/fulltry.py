# -*- coding: utf-8 -*-

"""
* Name:         cognitivefactory.interactive_clustering_gui.fulltry
* Description:  The full code for the interface.
* Author:       Thomas Tremble and Clementine Misiak
* Created:      15/12/2021
* Licence:      CeCILL-C License v1.0 (https://cecill.info/licences.fr.html)
"""

# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import csv
import json
import re
import time
import tkinter as tk  # python 3
from datetime import date
from tkinter import filedialog
from tkinter import font as tkfont  # python 3
from tkinter.constants import HORIZONTAL
from tkinter.ttk import Progressbar
from typing import Any, Dict, List

from cognitivefactory.interactive_clustering.clustering.factory import clustering_factory
from cognitivefactory.interactive_clustering.constraints.factory import managing_factory
from cognitivefactory.interactive_clustering.sampling.factory import sampling_factory
from cognitivefactory.interactive_clustering.utils.preprocessing import preprocess
from cognitivefactory.interactive_clustering.utils.vectorization import vectorize

# ==============================================================================
# GLOBAL VARIABLES
# ==============================================================================

SAVEFOLDERPATH = "./"
INIFILEPATH = ""
SESSIONNAME = ""
MODE = 0
DICTSAVE: Dict[Any, Any] = {}
MANAGER = None
SAMPLER = sampling_factory("random")
NBANNOTATIONS = 3
REQRESULTS = 0
RESULTINGVECTORS: Dict[Any, Any] = {}

# ==============================================================================
# GLOBAL FUNCTIONS
# ==============================================================================


def browseFiles():
    """
    Opens a file browser that asks for a CSV

    Returns:
        Path to the file
    """
    return filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("CSV files", "*.csv"),))


def browseFiles2():
    """
    Opens a file browser that asks for a json

    Returns:
        Path to the file
    """
    return filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("JSON files", "*.json"),))


def browseDirectories():
    """
    Opens a file browser that asks for a directory

    Returns:
        Path to the directory
    """
    return filedialog.askdirectory(initialdir="/", title="Select a directory")


def changeIni():
    """
    Sets the path to the initial dataset to the one selected in the browser.
    """
    global INIFILEPATH
    INIFILEPATH = browseFiles()


def changeSave():
    """
    Sets the path to the saving file to the one selected in the browser.
    This one is used in the case where we haven't imported from a previous session, the "/" is already included.
    """
    global SAVEFOLDERPATH
    SAVEFOLDERPATH = browseFiles2()


def changeSave2():
    """
    Sets the path to the saving file to the one selected in the browser.
    This one is used in the case where we have imported from a previous session, in which case it's missing a "/".
    """
    global SAVEFOLDERPATH
    SAVEFOLDERPATH = browseDirectories() + "/"


def save():
    """
    Saves the content of DICTSAVE (ie all the session's current data) to the save file.
    """
    print(SAVEFOLDERPATH + SESSIONNAME + ".json")
    with open(SAVEFOLDERPATH + SESSIONNAME + ".json", "w") as savefile:
        savefile.write(json.dumps(DICTSAVE))


# ==============================================================================
# MAIN APPLICATION
# ==============================================================================


class App(tk.Tk):
    """
    Class used to initialize the application.
    Frames each have their own classes, this one calls for them when needed.

    Reference:
        https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of the app.

        Args:
            **kwargs: Unused
            *args: Unused
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Accueil, AccueilImportNom, Annotation, Commencer, Clustering):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Accueil")

    def show_frame(self, page_name):
        """
        Method called to show a specific frame, it does NOT open or close anything, just shows it.

        Args:
            page_name: Name of the class to which the frame belongs.
        """
        frame = self.frames[page_name]
        frame.tkraise()


# ==============================================================================
# WELCOME FRAME
# ==============================================================================


class Accueil(tk.Frame):
    """
    Class for the welcoming frame, where the user can import a dataset for a new session or load a former one.
    """

    def import_nom(self, controller, label):
        """
        Called on "Importer" press, asks for the csv file of the dataset.

        Args:
            controller: Controller of the App
            label: Label entity where the name is stored
        """
        changeIni()
        reg = re.compile(r".*\.csv")
        if re.fullmatch(reg, INIFILEPATH) is None:
            tk.Label(label, text="/!\\ ERREUR D'IMPORTATION /!\\", fg="red").pack()
        else:
            controller.show_frame("AccueilImportNom")

    def import_session(self, controller, label):
        """
        Called on "Charger" press, asks for the json save file then loads all the necessary systems.

        Args:
            controller: Controller of the app
            label: Label object where the error message will popup
        """
        changeSave()
        global SAVEFOLDERPATH
        reg = re.compile(r".*\.json")
        if re.fullmatch(reg, SAVEFOLDERPATH) is None:
            tk.Label(label, text="/!\\ ERREUR D'IMPORTATION /!\\", fg="red").pack()
        else:
            global MODE
            MODE = 1
            global DICTSAVE
            with open(SAVEFOLDERPATH) as savefile:
                editable = SAVEFOLDERPATH.split("/")[:-1]
                SAVEFOLDERPATH = "/".join(editable) + "/"
                print(SAVEFOLDERPATH)
                DICTSAVE = json.load(savefile)
                global SESSIONNAME
                global INIFILEPATH
                SESSIONNAME = DICTSAVE["meta"]["session"]
                INIFILEPATH = DICTSAVE["meta"]["inifilepath"]
            global MANAGER
            with open(INIFILEPATH) as inifile:
                lines = inifile.readlines()
                n = len(lines)
                ids = [str(i) for i in range(0, n)]
                MANAGER = managing_factory(ids)
            for i in DICTSAVE["constraints"]:
                MANAGER.add_constraint(str(i["ID1"]), str(i["ID2"]), i["type"])
            controller.show_frame("Clustering")

    def __init__(self, parent, controller):
        """
        Initializes the frame.

        Args:
            parent: parent App
            controller: Controller of the application
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.LabelFrame(self, text="Bienvenue", padx=20, pady=20)
        label1.pack(fill="both", expand="yes")
        tk.Label(
            label1,
            text="A l'aide des boutons ci-dessous, vous pouvez choisir d'importer un document contenant les questions à traiter au format .csv en cliquant sur Importer.\nVous pouvez aussi choisir de continuer une sessions précédente en cliquant sur Charger.",
        ).pack()
        tk.Button(self, text="Importer", command=lambda: [self.import_nom(controller, label1)]).pack(
            side=tk.LEFT, padx=5, pady=5
        )
        tk.Button(self, text="Charger", command=lambda: self.import_session(controller, label1)).pack(
            side=tk.RIGHT, padx=5, pady=5
        )


# ==============================================================================
# SESSION NAMING FRAME
# ==============================================================================


class AccueilImportNom(tk.Frame):
    """
    Class for the name entering frame, allows the user to name their session.
    """

    def change_name(self, string):
        """
        Changes the session's name on a global scale.

        Args:
            string: new name for the session
        """
        global SESSIONNAME
        SESSIONNAME = string

    def __init__(self, parent, controller):
        """
        Initializes the frame.

        Args:
            parent: parent App
            controller: Controller of the application
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.LabelFrame(self, text="Bienvenue", padx=20, pady=20)
        label1.pack(fill="both", expand="yes")
        tk.Label(label1, text="Veuillez nommer votre session").pack()
        entree = tk.Entry(self, width=30)
        tk.Button(
            self,
            text="Valider",
            command=lambda: [self.change_name(entree.get()), print(SESSIONNAME), controller.show_frame("Commencer")],
        ).pack(side=tk.RIGHT, padx=5, pady=5)
        entree.pack()


# ==============================================================================
# ANNOTATION FRAME
# ==============================================================================


class Annotation(tk.Frame):
    """
    Class for the annotation frame. Where the user will create annotation to generate constraints.
    """

    ini = 0
    ID1 = 0
    ID2 = 0
    samples: List[Any] = []
    number = 0
    questions: List[str] = []
    isup = 0
    lfr = tk.LabelFrame
    Zone1 = tk.Text
    Zone2 = tk.Text
    b1 = tk.Button
    b2 = tk.Button
    b3 = tk.Button

    def onKeyPress(self, event):
        """
        Annotates depending on the user's key presses, as if they had clicked on the buttons.

        Args:
            event: tkinter event that contains the info of the key press
        """
        if self.isup == 1:
            print(event.keysym)
            if event.keysym == "Right":
                self.annoter("CANNOT_LINK", self.lfr)
                self.new_annotations(self.Zone1, self.Zone2, self.b1, self.b2, self.b3)
            if event.keysym == "Down":
                self.new_annotations(self.Zone1, self.Zone2, self.b1, self.b2, self.b3)
            if event.keysym == "Left":
                self.annoter("MUST_LINK", self.lfr)
                self.new_annotations(self.Zone1, self.Zone2, self.b1, self.b2, self.b3)

    def writeinboxes(self, box1, box2, liste):
        """
        Changes the text inside the boxes for the correction menu.

        Args:
            box1: First text box
            box2: Second text box
            liste: Selectable list
        """
        idselect = liste.size() - int(liste.curselection()[0]) - 1
        box1.config(state="normal")
        box2.config(state="normal")
        box1.delete("1.0", "end")
        box2.delete("1.0", "end")
        print("ID:" + str(idselect))
        box1.insert("end", self.questions[int(DICTSAVE["constraints"][idselect]["ID1"])])
        box2.insert("end", self.questions[int(DICTSAVE["constraints"][idselect]["ID2"])])
        box1.config(state="disabled")
        box2.config(state="disabled")

    def supprimerannotation(self, liste):
        """
        Removes an annotation/constraint from the app.

        Args:
            liste: Selectable list inside the menu.
        """
        idselect = liste.size() - int(liste.curselection()[0]) - 1
        global DICTSAVE
        del DICTSAVE["constraints"][idselect]
        liste.delete(int(liste.curselection()[0]))

    def corrections(self):
        """
        Opens the correction menu where the user can remove past annotations.
        """
        window = tk.Tk()
        window.title("Corrections")
        window.geometry("200x400")
        lb = tk.Listbox(window, selectmode="SINGLE")
        txt1 = tk.Text(window, width=30, height=1, state="disabled")
        txt2 = tk.Text(window, width=30, height=1, state="disabled")
        b1 = tk.Button(window, text="Sélectionner", command=lambda: [self.writeinboxes(txt1, txt2, lb)])
        b2 = tk.Button(window, text="Supprimer l'annotation", command=lambda: [self.supprimerannotation(lb)])
        lb.pack()
        for i in reversed(DICTSAVE["constraints"]):
            lb.insert("end", str(i["ID1"]) + " " + str(i["ID2"]))
        b1.pack()
        txt1.pack()
        txt2.pack()
        b2.pack()
        window.mainloop()

    def Get_questions(self):
        """
        Loads all of the questions in string forms to be used in the text boxes.
        """
        with open(INIFILEPATH) as dataset:
            reader = csv.reader(dataset)
            self.questions = list(reader)
            print(self.questions)

    def Get_IDs(self):
        """
        Gets the IDs for the next questions pairing.

        Returns:
            couple of IDs for the next annotation
        """
        ID1 = int(self.samples[self.number][0])
        ID2 = int(self.samples[self.number][1])
        self.number = self.number + 1
        print(ID1, ID2)
        return (ID1, ID2)

    def inibindings(self):
        """
        Initializes the control window for keyboard support of annotations.
        """
        bindings = tk.Tk()
        bindings.bind("<KeyPress>", self.onKeyPress)
        text = tk.Label(
            bindings,
            text="Si vous souhaitez utiliser les touches du clavier pour l'annotation, gardez cette fenêtre active.",
        )
        text.pack(side=tk.TOP)
        bindings.mainloop()

    def new_annotations(self, Zone1, Zone2, b, c, e):
        """
        Asks the user for a new annotation if there are still pairings in the queue, otherwise asks them if they want to go to clustering.

        Args:
            Zone1: First text box
            Zone2: 2nd text box
            b: Button that can be loaded, unloaded
            c: Button that can be loaded, unloaded
            e: Button that can be loaded, unloaded
        """
        if MANAGER.check_completude_of_constraints():
            tk.Label(self, text="Toutes les contraintes possibles ont été annotées.").pack(side=tk.TOP, padx=5, pady=5)
        else:
            if self.number < len(self.samples):
                (ID1, ID2) = self.Get_IDs()
                Zone1.config(state="normal")
                Zone1.delete("1.0", "end")
                print(self.questions[ID1][0])
                Zone1.insert("end", self.questions[ID1][0])
                Zone1.config(state="disabled")
                Zone2.config(state="normal")
                Zone2.delete("1.0", "end")
                Zone2.insert("end", self.questions[ID2][0])
                Zone2.config(state="disabled")
                self.ID1 = ID1
                self.ID2 = ID2
            else:
                d = tk.Button(
                    self,
                    text="Continuer l'Annotation",
                    command=lambda: [
                        self.ini_sampling(MANAGER, NBANNOTATIONS),
                        self.new_annotations(Zone1, Zone2, b, c, e),
                        d.pack_forget(),
                        b.pack(side=tk.LEFT, padx=5, pady=5),
                        c.pack(side=tk.RIGHT, padx=5, pady=5),
                        e.pack(side=tk.BOTTOM, padx=5, pady=5),
                    ],
                )
                Zone1.delete("1.0", "end")
                Zone2.delete("1.0", "end")
                e.pack_forget()
                b.pack_forget()
                c.pack_forget()
                d.pack(side=tk.TOP, padx=5, pady=5)
                self.number = 0
                self.isup = 0

    def annoter(self, annotype, label):
        """
        Registers the user's annotation as a constraint in the app.

        Args:
            annotype: string that indicates wether it's a MUST_LINK or CANNOT_LINK
            label: Label object where the error message will show
        """
        global DICTSAVE
        DICTSAVE["constraints"].append({"ID1": self.ID1, "ID2": self.ID2, "type": annotype})
        if not MANAGER.add_constraint(str(self.ID1), str(self.ID2), annotype):
            tk.Label(label, text="/!\\ ERREUR CONTRAINTE /!\\", fg="red").pack()

    def ini_sampling(self, manager, nb):
        """
        Initiates the sampler.

        Args:
            manager: Sample manager currently loaded in the app.
            nb: amount of pairs required.
        """
        self.isup = 1
        if REQRESULTS == 0:
            self.samples = SAMPLER.sample(manager, nb)
        else:
            self.samples = SAMPLER.sample(manager, nb, DICTSAVE["clusteringResults"][-1], RESULTINGVECTORS)
        print("Sampler Created")
        print(self.samples)

    def __init__(self, parent, controller):
        """
        Initializes the frame.

        Args:
            parent: parent App
            controller: Controller of the application
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.LabelFrame(self, text="Annotation", padx=20, pady=20)
        self.lfr = label1
        label1.pack(fill="both", expand="yes")
        tk.Label(
            label1,
            text="Les deux entrées suivantes ont été trouvées comme similaires. Donneriez-vous la même réponse au deux ? \n Sélectionner :\n - le bouton gauche pour oui\n - le bouton du centre pour je ne sais pas\n - le bouton de droite pour non",
        ).pack()
        Zone_de_texte = tk.Text(self, width=50, height=3, state="disabled")
        self.Zone1 = Zone_de_texte
        Zone_de_texte.pack()
        Zone_de_texte2 = tk.Text(self, width=50, height=3, state="disabled")
        self.Zone2 = Zone_de_texte2
        Zone_de_texte2.pack()
        b = tk.Button(
            self,
            text="OUI",
            command=lambda: [
                self.annoter("MUST_LINK", label1),
                self.new_annotations(Zone_de_texte, Zone_de_texte2, b, c, e),
            ],
        )
        self.b1 = b
        c = tk.Button(
            self,
            text="NON",
            command=lambda: [
                self.annoter("CANNOT_LINK", label1),
                self.new_annotations(Zone_de_texte, Zone_de_texte2, b, c, e),
            ],
        )
        self.b2 = c
        e = tk.Button(
            self, text="JE NE SAIS PAS", command=lambda: [self.new_annotations(Zone_de_texte, Zone_de_texte2, b, c, e)]
        )
        self.b3 = e
        a = tk.Button(
            self,
            text="Commencer",
            command=lambda: [
                self.ini_sampling(MANAGER, NBANNOTATIONS),
                self.Get_questions(),
                self.new_annotations(Zone_de_texte, Zone_de_texte2, b, c, e),
                a.pack_forget(),
                b.pack(side=tk.LEFT, padx=5, pady=5),
                c.pack(side=tk.RIGHT, padx=5, pady=5),
                e.pack(side=tk.BOTTOM, padx=5, pady=5),
                self.inibindings(),
            ],
        )
        a.pack(side=tk.TOP, padx=5, pady=5)
        tk.Button(self, text="Sauvegarder", command=lambda: save()).pack(side=tk.BOTTOM, padx=5, pady=5)
        tk.Button(
            self,
            text="Clustering",
            command=lambda: [
                save(),
                Zone_de_texte.delete("1.0", "end"),
                Zone_de_texte2.delete("1.0", "end"),
                a.pack(side=tk.TOP, padx=5, pady=5),
                controller.show_frame("Clustering"),
            ],
        ).pack(side=tk.TOP, padx=5, pady=5)
        tk.Button(self, text="Corriger", command=lambda: [self.corrections()]).pack(side=tk.BOTTOM, padx=5, pady=5)


# ==============================================================================
# SESSION START FRAME
# ==============================================================================


class Commencer(tk.Frame):
    """
    Class for the beginning of a session frame, where the user can set preferences for the session to come.
    """

    def sauvcommand(self, label):
        """
        Saves the user's settings.

        Args:
            label: Label Object where the user's save path will be shown
        """
        changeSave2()
        label["text"] = SAVEFOLDERPATH

    def appliquercommand(self, scale, menu):
        """
        Applies the user's choice of parameters to the systems.

        Args:
            scale: Scale object that has the number of annotations per iteration
            menu: selection menu for sampling methods
        """
        global NBANNOTATIONS
        NBANNOTATIONS = scale.get()
        a = menu.get()
        global SAMPLER
        global REQRESULTS
        if a == "Random in same cluster":
            SAMPLER = sampling_factory("random_in_same_cluster")
            REQRESULTS = 1
        elif a == "Farthest in same cluster":
            SAMPLER = sampling_factory("farthest_in_same_cluster")
            REQRESULTS = 1
        elif a == "closest in different clusters":
            SAMPLER = sampling_factory("closest_in_different_clusters")
            REQRESULTS = 1
        print(a)

    def settings(self):
        """
        Opens the settings menu for the current session.
        """
        window = tk.Tk()
        window.title("Session Settings")
        window.geometry("200x400")
        appliquer = tk.Button(
            window, text="Appliquer", command=lambda: [self.appliquercommand(annot, select), window.destroy()]
        )
        label1 = tk.Label(window, text=SAVEFOLDERPATH)
        sauv = tk.Button(window, text="Modifier Emplacement de Sauvegarde", command=lambda: [self.sauvcommand(label1)])
        label2 = tk.Label(window, text="Annotations par itération:")
        annot = tk.Scale(window, from_=1, to=30, orient=HORIZONTAL)
        label3 = tk.Label(window, text="Méthode d'échantillonage:")
        select = tk.StringVar(window)
        select.set("Random")
        options = ["Random", "Random in same cluster", "Farthest in same cluster", "closest in different clusters"]
        echan = tk.OptionMenu(window, select, *options)
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
        """
        Initializes the json save file for the new session.
        """
        global DICTSAVE
        DICTSAVE = {
            "meta": {
                "session": SESSIONNAME,
                "inifilepath": INIFILEPATH,
                "savefolderpath": SAVEFOLDERPATH,
                "dateCreated": str(date.today()),
                "dateModified": str(date.today()),
            },
            "constraints": [],
            "clusteringResults": [],
        }
        # Clustering Initial avec les paramètres
        save()

    def ini_manager(self):
        """
        Initializes the constraints manager.
        """
        global MANAGER
        with open(INIFILEPATH) as file:
            lines = file.readlines()
            n = len(lines)
        ids = [str(i) for i in range(0, n)]
        MANAGER = managing_factory(ids)
        print(MANAGER.get_list_of_managed_data_IDs())

    def __init__(self, parent, controller):
        """
        Initializes the frame.

        Args:
            parent: parent App
            controller: Controller of the application
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(
            self,
            text="Afin de lancer le clustering avec les paramètres par défaut (recommandé),\n appuyez sur COMMENCER.\n Vous pouvez aussi choisir de modifier les paramètres du clustering\n en cliquant sur PARAMETRES",
        ).pack()
        tk.Button(
            self,
            text="COMMENCER",
            command=lambda: [self.ini_manager(), self.ini_json(), controller.show_frame("Clustering")],
        ).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self, text="PARAMETRES", command=lambda: [self.settings()]).pack(side=tk.RIGHT, padx=5, pady=5)


# ==============================================================================
# CLUSTERING FRAME
# ==============================================================================


class Clustering(tk.Frame):
    """
    Class for the clustering frame, where the user can configure then see the clustering unfold.
    """

    CLUSTERINGTYPE = "kmeans"
    nb_clusters = 3
    d = {"ini": "ini"}

    def appliqcommand(self, text, nb):
        """
        Command for the "Appliquer" Button. Changes the settings.

        Args:
            text: string of the clustering method.
            nb: number of clusters
        """
        self.CLUSTERINGTYPE = text
        self.nb_clusters = nb

    def settings(self):
        """
        Opens the settings menu for the current clustering.
        """
        window = tk.Tk()
        window.title("Session Settings")
        window.geometry("200x400")
        appliq = tk.Button(
            window, text="Appliquer", command=lambda: [self.appliqcommand(select.get(), clust.get()), window.destroy()]
        )
        label1 = tk.Label(window, text="Méthode de Classification:")
        select = tk.StringVar(window)
        select.set("kmeans")
        options = ["kmeans", "hierarchical", "spectral"]
        classi = tk.OptionMenu(window, select, *options)
        label2 = tk.Label(window, text="Nombre de clusters:")
        clust = tk.Scale(window, from_=2, to=20, orient=HORIZONTAL)
        clust.set(3)
        label1.pack(side=tk.TOP)
        classi.pack(side=tk.TOP)
        label2.pack(side=tk.TOP)
        clust.pack(side=tk.TOP)
        appliq.pack(side=tk.BOTTOM)
        window.mainloop()

    def clusterize(self, clusteringtype, controller, p, sbut, progress):
        """
        Runs the clustering after the user starts it.

        Args:
            clusteringtype: string with the clustering method
            controller: Controller of the application
            p: settings button
            sbut: button that starts the clustering
            progress: Progression bar
        """
        model = clustering_factory(clusteringtype)
        with open(INIFILEPATH) as dataset:
            reader = csv.reader(dataset)
            questions = list(reader)
        ini = []
        for i in questions:
            ini.append(i[0])
        print(ini)
        keys = [str(j) for j in range(0, len(ini))]
        if self.d == {"ini": "ini"}:
            a = dict(zip(keys, ini))
            print(a)
            self.d = vectorize(preprocess(a))
            global RESULTINGVECTORS
            RESULTINGVECTORS = self.d
        results = model.cluster(MANAGER, self.d, self.nb_clusters)
        global DICTSAVE
        DICTSAVE["clusteringResults"].append(results)
        d = tk.Button(
            self,
            text="Passer à l'annotation",
            command=lambda: [
                progress.pack_forget(),
                d.pack_forget(),
                f.pack_forget(),
                p.pack(side=tk.RIGHT, padx=5, pady=5),
                sbut.pack(side=tk.BOTTOM, padx=5, pady=5),
                controller.show_frame("Annotation"),
            ],
        )
        d.pack(side=tk.BOTTOM)
        f = tk.Button(self, text="Sauvegarder", command=lambda: save())
        f.pack(side=tk.BOTTOM)

    def bar(self, progress):
        """
        Method for the progress bar.

        Args:
            progress: Progression bar Tkinter object
        """
        progress["value"] = 20
        self.update_idletasks()
        time.sleep(1)

        progress["value"] = 40
        self.update_idletasks()
        time.sleep(1)

        progress["value"] = 50
        self.update_idletasks()
        time.sleep(1)

        progress["value"] = 60
        self.update_idletasks()
        time.sleep(1)

        progress["value"] = 80
        self.update_idletasks()
        time.sleep(1)
        progress["value"] = 100

    def __init__(self, parent, controller):
        """
        Initializes the frame.

        Args:
            parent: parent App
            controller: Controller of the application
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        progress = Progressbar(self, orient=HORIZONTAL, length=100, mode="determinate")
        tk.Label(
            self,
            text="L'annotation est terminée.\n Souhaitez-vous annoter d'autres couples,\n refaire un clustering ou terminer ?",
        ).pack()
        p = tk.Button(self, text="Paramètres", command=lambda: [self.settings()])
        p.pack(side=tk.RIGHT, padx=5, pady=5)
        sbut = tk.Button(
            self,
            text="Lancer le Clustering",
            command=lambda: [
                progress.pack(pady=10),
                self.clusterize(self.CLUSTERINGTYPE, controller, sbut, p, progress),
                self.bar(progress),
                sbut.pack_forget(),
                p.pack_forget(),
            ],
        )
        sbut.pack(side=tk.BOTTOM, padx=5, pady=5)


# ==============================================================================
# RUNNING THE APPLICATION
# ==============================================================================

if __name__ == "__main__":
    app = App()
    app.mainloop()
