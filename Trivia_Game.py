#!/usr/bin/python3
#Brady Durham and Alex Jordan
#3/9/2020



import pickle
import tkinter as tk

'''Trivia Game with random questions for the user to answer covering multiple topics: Geography, History, Music, Games, and Random questions.'''



dictionary = []


TITLE_FONT = ("Times New Roman", "24")

BUTTON_FONT = ("Arial", "15")


class MainMenu(tk.Frame):

    def __init__(self):

        tk.Frame.__init__(self)

        self.lbl_title = tk.Label(self, text = "Welcome To Trivia Night! ", font = TITLE_FONT, bg="blue")

        self.lbl_title.grid(row = 0, column = 0, columnspan = 5, sticky = "news")

        

        '''History questions'''

        self.lbl_history = tk.Label(self, text = "History",

                             font = BUTTON_FONT)

        self.lbl_history.grid(row = 1, column = 0, sticky = "news")        

        

        self.btn_history = tk.Button(self, text = "100", font = BUTTON_FONT, bg ="yellow")

        self.btn_history.grid(row = 2, column = 0, sticky = "news")

        

        self.btn_history = tk.Button(self, text = "200", font = BUTTON_FONT, bg="orange")

        self.btn_history.grid(row = 3, column = 0, sticky = "news")

        

        self.btn_history = tk.Button(self, text = "300", font = BUTTON_FONT, bg="purple")

        self.btn_history.grid(row = 4, column = 0, sticky = "news")

        

        self.btn_history = tk.Button(self, text = "400", font = BUTTON_FONT, bg="green")

        self.btn_history.grid(row = 5, column = 0, sticky = "news")

        

        self.btn_history = tk.Button(self, text = "500", font = BUTTON_FONT, bg="red")

        self.btn_history.grid(row = 6, column = 0, sticky = "news")

        

        '''Geography questions'''

        self.lbl_geography = tk.Label(self, text = "Geography",

                             font = BUTTON_FONT)

        self.lbl_geography.grid(row = 1, column = 1, sticky = "news")        

        

        self.btn_geography = tk.Button(self, text = "100", font = BUTTON_FONT, bg="yellow")

        self.btn_geography.grid(row = 2, column = 1, sticky = "news")

        

        self.btn_geography = tk.Button(self, text = "200", font = BUTTON_FONT, bg="orange")

        self.btn_geography.grid(row = 3, column = 1, sticky = "news")

        

        self.btn_geography = tk.Button(self, text = "300", font = BUTTON_FONT, bg="purple")

        self.btn_geography.grid(row = 4, column = 1, sticky = "news")

        

        self.btn_geography = tk.Button(self, text = "400", font = BUTTON_FONT, bg="green")

        self.btn_geography.grid(row = 5, column = 1, sticky = "news")

        

        self.btn_geography = tk.Button(self, text = "500", font = BUTTON_FONT, bg="red")

        self.btn_geography.grid(row = 6, column = 1, sticky = "news")

        

        '''Music questions'''

        self.lbl_music = tk.Label(self, text = "Music",

                             font = BUTTON_FONT)

        self.lbl_music.grid(row = 1, column = 2, sticky = "news")        

        

        self.btn_music = tk.Button(self, text = "100", font = BUTTON_FONT, bg="yellow")

        self.btn_music.grid(row = 2, column = 2, sticky = "news")

        

        self.btn_music = tk.Button(self, text = "200", font = BUTTON_FONT, bg="orange")

        self.btn_music.grid(row = 3, column = 2, sticky = "news")

        

        self.btn_music = tk.Button(self, text = "300", font = BUTTON_FONT, bg="purple")

        self.btn_music.grid(row = 4, column = 2, sticky = "news")

        

        self.btn_music = tk.Button(self, text = "400", font = BUTTON_FONT, bg="green")

        self.btn_music.grid(row = 5, column = 2, sticky = "news")

        

        self.btn_music = tk.Button(self, text = "500", font = BUTTON_FONT, bg="red")

        self.btn_music.grid(row = 6, column = 2, sticky = "news")

        

        '''Video Game questions'''

        

        self.lbl_music = tk.Label(self, text = "Video Games",

                             font = BUTTON_FONT)

        self.lbl_music.grid(row = 1, column = 3, sticky = "news")        

        

        self.btn_music = tk.Button(self, text = "100", font = BUTTON_FONT, bg="yellow")

        self.btn_music.grid(row = 2, column = 3, sticky = "news")

        

        self.btn_music = tk.Button(self, text = "200", font = BUTTON_FONT,bg="orange")

        self.btn_music.grid(row = 3, column = 3, sticky = "news")

        

        self.btn_music = tk.Button(self, text = "300", font = BUTTON_FONT, bg="purple")

        self.btn_music.grid(row = 4, column = 3, sticky = "news")

        

        self.btn_music = tk.Button(self, text = "400", font = BUTTON_FONT, bg="green")

        self.btn_music.grid(row = 5, column = 3, sticky = "news")

        

        self.btn_music = tk.Button(self, text = "500", font = BUTTON_FONT, bg="red")

        self.btn_music.grid(row = 6, column = 3, sticky = "news")   

        

        

        '''Random questions'''

        

        self.lbl_music = tk.Label(self, text = "Random",

                             font = BUTTON_FONT)

        self.lbl_music.grid(row = 1, column = 4, sticky = "news")        

        

        self.btn_music = tk.Button(self, text = "100", font = BUTTON_FONT, bg="yellow")

        self.btn_music.grid(row = 2, column = 4, sticky = "news")

        

        self.btn_music = tk.Button(self, text = "200", font = BUTTON_FONT, bg="orange")

        self.btn_music.grid(row = 3, column = 4, sticky = "news")

        

        self.btn_music = tk.Button(self, text = "300", font = BUTTON_FONT, bg="purple")

        self.btn_music.grid(row = 4, column = 4, sticky = "news")

        

        self.btn_music = tk.Button(self, text = "400", font = BUTTON_FONT, bg="green")

        self.btn_music.grid(row = 5, column = 4, sticky = "news")

        

        self.btn_music = tk.Button(self, text = "500", font = BUTTON_FONT, bg="red")

        self.btn_music.grid(row = 6, column = 4, sticky = "news")        

        

        

        

        self.grid_columnconfigure(0, weight = 1)

        self.grid_columnconfigure(1, weight = 1)

        self.grid_columnconfigure(2, weight = 1)

        self.grid_columnconfigure(3, weight = 1)

        self.grid_columnconfigure(4, weight = 1)

        

class History(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        
        
        



        

        

        

if __name__ == "__main__":

        data_file = open("Trivia_Game.pickle", "rb")

        questions = pickle.load(data_file)

        data_file.close()

        root = tk.Tk()

        root.title("Game_Lib")

        root.geometry("1000x275")

        main_menu = MainMenu()

        main_menu.grid(row = 0, column = 0,

                               sticky = "news")            

        root.grid_columnconfigure(0, weight = 1)     

        root.mainloop()  


