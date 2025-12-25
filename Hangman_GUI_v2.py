'''Afterthought: Add a wallpaper like the rest of the games that i made
      Make that wallpaper dynamic(make it change onclick or some other idea)'''

import tkinter as tk
from tkinter import messagebox
import random
import winsound

with open("Hangman GUI words list.txt", 'r') as file:
    content = file.read().upper()  # Read content and convert to uppercase
    words_list = content.split()  # Split content into words


class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("1200x720")
        self.master.configure(bg='skyblue')
        self.word_list = words_list
        self.secret_word = self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7
        self.initialize_gui()

    def initialize_gui(self):
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")
        self.hangman_canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
        self.hangman_canvas.pack(pady=20)
        self.word_display = tk.Label(self.master, text="_ " * len(self.secret_word), font=("Helvetica", 39), bg='skyblue')
        self.word_display.pack(pady=(40, 10))
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)
        self.setup_alphabet_buttons()

    def setup_alphabet_buttons(self):
   
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 14, "bold")

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        upper_row = alphabet[:13]
        lower_row = alphabet[13:]

        self.buttons = {}

        upper_frame = tk.Frame(self.buttons_frame, bg='skyblue')
        upper_frame.pack(fill='x')
        lower_frame = tk.Frame(self.buttons_frame, bg='skyblue')
        lower_frame.pack(fill='x')

        for letter in upper_row:
            button = tk.Button(upper_frame, text=letter, command=lambda l=letter: [self.guess_letter(l), winsound.Beep(400, 100)],
                               activebackground="blue", width=4, height=2, bd=5, bg=button_bg, fg=button_fg, font=button_font)
            button.pack(side="left", padx=1, pady=1)
            self.buttons[letter] = button

        for letter in lower_row:
            button = tk.Button(lower_frame, text=letter, command=lambda l=letter: [self.guess_letter(l), winsound.Beep(400, 100)],
                               activebackground="blue", width=4, height=2, bd=5, bg=button_bg, fg=button_fg, font=button_font)
            button.pack(side="left", padx=1, pady=1)
            self.buttons[letter] = button

    def choose_secret_word(self):
        word = random.choice(self.word_list)
        #print(word)
        return word

    def update_hangman_canvas(self):
        self.hangman_canvas.delete("all")
        stages = [self.draw_head, self.draw_body, self.draw_left_arm, self.draw_right_arm,
                  self.draw_left_leg, self.draw_right_leg, self.draw_face]
        for i in range(len(self.incorrect_guesses)):
            if i < len(stages):
                stages[i]()

    def draw_head(self):
        self.hangman_canvas.create_oval(110, 40, 200, 120, width=5, outline="black")

    def draw_body(self):
        self.hangman_canvas.create_line(155, 120, 155, 200, width=5, fill="black")

    def draw_left_arm(self):
        self.hangman_canvas.create_line(155, 150, 105, 170, width=5, fill="black")

    def draw_right_arm(self):
        self.hangman_canvas.create_line(155, 150, 205, 170, width=5, fill="black")

    def draw_left_leg(self):
        self.hangman_canvas.create_line(155, 200, 115, 235, width=5, fill="black")

    def draw_right_leg(self):
        self.hangman_canvas.create_line(155, 200, 195, 235, width=5, fill="black")

    def draw_face(self):
        self.hangman_canvas.create_oval(110, 40, 200, 120, width=2, outline="black", fill='yellow')
        self.hangman_canvas.create_line(125, 70, 140, 80, width=5, fill="black")
        self.hangman_canvas.create_line(125, 80, 140, 70, width=5, fill="black")
        self.hangman_canvas.create_line(168, 80, 183, 70, width=5, fill="black")     
        self.hangman_canvas.create_line(168, 70, 183, 80, width=5, fill="black")
        self.hangman_canvas.create_arc(130, 85, 180, 105, start=0, extent=-180, width=5, fill="black")
        winsound.Beep(500, 1000)
        self.hangman_canvas.config(bg='red')

    def guess_letter(self, letter):
        button = self.buttons[letter]

        if letter in self.secret_word and letter not in self.correct_guesses:
            self.correct_guesses.add(letter)
            button.config(bg="#2cff05",fg='white')
        elif letter not in self.secret_word and letter not in self.incorrect_guesses:
            self.incorrect_guesses.add(letter)
            self.attempts_left -= 1
            self.update_hangman_canvas()
            button.config(bg="#c30f16",fg='white')

        self.update_word_display()
        self.check_game_over()

    def update_word_display(self):
        displayed_word = " ".join([letter if letter in self.correct_guesses else "_" for letter in self.secret_word])
        self.word_display.config(text=displayed_word)

    def check_game_over(self):
        if set(self.secret_word).issubset(self.correct_guesses):
            self.display_game_over_message("Congratulations, you've won!")
            self.restart()
        elif self.attempts_left == 0:
            self.display_game_over_message(f"Game over! The word was: {self.secret_word}")
            self.restart()

    def display_game_over_message(self, message):
        stylish_font = ("Arial", 24, "italic")
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica", 12, "bold")

        self.buttons_frame.pack_forget()

        self.game_over_label = tk.Label(self.master, text=message, font=stylish_font, fg="red", bg='skyblue')
        self.game_over_label.pack(pady=(10, 20))

    def restart(self):
        choice = messagebox.askyesno("RESTART", "Do you want to Restart the game?")
        if not choice:
            self.master.quit()
            self.master.destroy()
        else:
            self.reset_game()

    def reset_game(self):
        self.secret_word = self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7

        self.hangman_canvas.delete("all")
        self.hangman_canvas.config(bg='white')

        self.update_word_display()

        for button in self.buttons.values():
            button.configure(state=tk.NORMAL, bg="#4a7a8c")

        if hasattr(self, 'game_over_label') and self.game_over_label.winfo_exists():
            self.game_over_label.pack_forget()

        self.buttons_frame.pack()


root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
