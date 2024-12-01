
from tqdm import tqdm
import time
import tkinter
import random
import pandas as pd
from tkinter import *
from PIL import Image, ImageTk


class CleaningTheData:
    def __init__(self):
        self.o_df = pd.read_csv('pokemon.csv')
        self.df_c = self.o_df.drop(['#', 'Type 2', 'Total', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary'],
                                    axis=1)
        self.selected_pokemon = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle",
                                 "Wartortle", "Blastoise",
                                 "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto",
                                 "Pidgeot"]

        self.df_c = self.df_c[self.df_c['Name'].isin(self.selected_pokemon)]
        self.df_c = self.df_c[['Name', 'Type 1', 'HP', 'Attack']]
        self.o_df.to_csv('pokemon.csv', index=False)
        self.df_c.to_csv('cleaned_data.csv', index=False)



class ChoosingWindow(Frame):
    def __init__(self, parent, player):
        Frame.__init__(self, parent)
        self.parent = parent
        self.player = player
        self.chosen_pokemon = None
        self.labels()
        self.list()
        self.choose()
        parent.geometry("350x250+300+300")
        parent.title("Pokemon!")

        self.photo_dic = {}
        for name in ["Bulbasaur", "Squirtle", "Charmander", "Caterpie", "Weedle", "Pidgey"]:
            image = ImageTk.PhotoImage(Image.open(f"{name}.png").resize((100, 100)))
            self.photo_dic[name] = image

    def labels(self):
        l1 = Label(self.parent, text=f"Player {self.player} chooses Pokemon !")
        l1.grid(row=0, column=0, columnspan=2, sticky='WES')

    def choose(self):
        self.b1 = Button(self.parent, text="Choose!", command=self.confirm_choice)
        self.b1.grid(row=2, column=1, sticky='WSE', padx=50)

    def list(self):
        list_of_pok = ["Bulbasaur", "Squirtle", "Charmander", "Caterpie", "Weedle", "Pidgey"]
        self.lb = Listbox(self.parent, selectmode="single")
        for i in list_of_pok:
            self.lb.insert(END, i)

        self.lb.grid(row=1, column=0, rowspan=2, pady=20, padx=10, ipady=0.5)
        self.lb.bind("<<ListboxSelect>>", self.update_image)

    def update_image(self, event=None):
        index = self.lb.curselection()
        if index:
            chosen_pokemon = self.lb.get(index[0])
            if chosen_pokemon in self.photo_dic:
                self.my_label = Label(self.parent, image=self.photo_dic[chosen_pokemon])
                self.my_label.image = self.photo_dic[chosen_pokemon]  # keep a reference!
                self.my_label.grid(row=1, column=1)

    def confirm_choice(self):
        index = self.lb.curselection()
        if index:
            self.chosen_pokemon = self.lb.get(index[0])
            print(f"Player {self.player} chooses {self.chosen_pokemon}!")
            self.parent.quit()

class fight(Frame):
    def __init__(self,root, parent,hp_pok1,hp_pok2, player1,player2):
        Frame.__init__(self, parent)
        self.parent=parent
        parent.geometry("350x250+300+300")
        parent.title("pokemon Battle")
        self.player1=player1
        self.player2=player2
        self.hp_pok1=hp_pok1
        self.hp_pok2=hp_pok2
        self.labels()
        self.buttons()
        self.switch()
        self.physical_attack()
        self.elemental_attack()
        self.update_hp()
        self.attack()
        self.root=root
        self.turn=1
    def labels(self):
        self.l1n=Label(root,text=f"player1:{player1.name}")
        self.l1hp=Label(root,text=f"hp:{player1.hp}")
        self.l1score=Label(root,text="score")
        self.l2n = Label(root, text=f"player2:{player2.name}")
        self.l2hp = Label(root, text=f"hp:{player2.hp}")
        self.l2score = Label(root, text="score")
        self.l1n .grid()
        self.l1hp.grid()
        self.l1score.grid()
        self.l2n .grid()
        self.l2hp .grid()
        self.l2score.grid()

    def buttons(self):
        self.buttons_physical=Button(root,text="physical",command=self.physical_attack)
        self.buttons_elemental=Button(root,text="elemental",command=self.elemental_attack)
        self.buttons_elemental.grid(row=0,column=5,sticky='E')
        self.buttons_physical.grid(row=0,column=5,sticky='W')
        self.buttons_elemental.grid(row=1, column=5, sticky='E')
        self.buttons_physical.grid(row=1, column=5, sticky='W')
    def switch(self):

        if self.turn==1:
            self.turn=2
            attacker=self.player1
            defender=self.player2
            self.buttons_physical.config(state=DISABLED)
            self.buttons_elemental.config(state=DISABLED)
        else:
            self.turn=1
            attacker=self.player2
            defender=self.player1
            self.buttons_physical.config(state=NORMAL)
            self.buttons_elemental.config(state=NORMAL)
    def physical_attack(self):
        damage=random.randint(75,100)
        self.hp_pok2-=damage
        self.update_hp()
    def elemental_attack(self):
        damage = random.randint(50, 100)
        if data==Attack:
            self.hp_pok2-=damage
            self.update_hp()
    def update_hp(self):
        self.l2hp.config(text=f"player2:{self.player2.name}HP:{self.hp_pok2}")
        if self.hp_pok2<=0:
            self.game_over()
        else:
            self.switch()
    def progress(self):
        for i in progressbar(range(100),0):
            time.sleep(0.1)



level_up_chain={
    "Bulbasaur":["Ivysaur","Venusaur"],
    "Charmander":["Charmeleon","Charizard"],
    "squirtle":["Wartortle","Blastoise"],
    "Caterpie":["metapod","Butterfree"],
    "Weedle":["kakuna","Breedrill"],
    "Pidgey":["Pidgeotto","Pidgeot"]

    }

    def attack(self):
        version=['Fire','Water','Grass','Normal','Bug']
        for i,k in enumerate(version):
            if water>fire:





def main():
    data = CleaningTheData()
    root1 = Tk()
    welcome_window_p1 = ChoosingWindow(root1, 1)
    welcome_window_p1.grid(row=0, column=0)
    root1.mainloop()
    p1_choice = welcome_window_p1.chosen_pokemon
    root1.destroy()

    root2 = Tk()
    welcome_window_p2 = ChoosingWindow(root2, 2)
    welcome_window_p2.grid(row=0, column=0)
    root2.mainloop()
    p2_choice = welcome_window_p2.chosen_pokemon
    root2.destroy()

    print(f"Player 1 chose: {p1_choice}")
    print(f"Player 2 chose: {p2_choice}")
    root3=Tk()
    player1= data.df_c[data.df_c['Name'] == p1_choice].iloc[0].to_dict()
    player2 = data.df_c[data.df_c['Name'] == p2_choice].iloc[0].to_dict()
    app = fight(root3, parent=root3, hp_pok1=hp_pok1['HP'],hp_pok2=hp_pok2['HP'], player1=player1, player2=player2)
    app.grid()
    root3.mainloop()




if __name__ == '__main__':
    main()
