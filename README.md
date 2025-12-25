# Hangman GUI Game

A classic Hangman game implemented in Python using Tkinter, featuring an interactive graphical interface, sound effects, and a dynamic hangman drawing that updates with each incorrect guess.

## Screenshots
<img width="1919" height="1007" alt="image" src="https://github.com/user-attachments/assets/a123637a-1433-43dc-82af-3c65a52a5685" />

---

## Features

- Graphical user interface built with Tkinter
- On-screen alphabet buttons for guessing letters
- Visual hangman drawing using a canvas
- Sound effects for button clicks and game over
- Random word selection from an external file
- Restart or exit option after game completion
- Clear visual feedback for correct and incorrect guesses

---
## How to Play

1. Launch the game.
2. A secret word is chosen randomly.
3. Click letters using the on-screen buttons.
4. Correct guesses reveal letters in the word.
5. Incorrect guesses draw parts of the hangman.
6. You have **7 incorrect attempts** before losing.
7. Win by guessing the word before the hangman is completed.

---

## Requirements

- Python **3.8 or higher**
- Windows OS (required for `winsound` module)
- Built-in Python libraries only:
  - `tkinter`
  - `random`
  - `winsound`

---

## Word List Format

- The file `Hangman GUI words list.txt` should contain words separated by spaces or new lines.
- All words are automatically converted to **uppercase**.
- Example:
  
    PYTHON
  
    COMPUTER
  
    HANGMAN
  
    PROGRAMMING
---

## Running the Game

```bash
python hangman_gui.py
```
---

## Sound Effects

- A short beep plays when a letter button is clicked.
- A longer alert sound plays when the hangman is fully drawn, indicating game over.
- Note: Sound functionality relies on the winsound module and works only on Windows.
---
## Restart System

- After winning or losing, the player is asked whether to restart the game.
- Choosing No closes the application.
- Choosing Yes resets:
    - The secret word
    - Correct and incorrect guesses
    - Hangman drawing
    - Alphabet button states
---
## Future Improvements

- Add a background wallpaper
- Make the background dynamic and interactive
- Add difficulty levels
- Enable keyboard input
- Add score tracking
