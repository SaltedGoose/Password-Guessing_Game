from tkinter import *
import random

def forward():
    global stored_attempts
    if guess_display_box['text'] != 'Invalid attempt':
        current_index = stored_attempts.index(guess_display_box['text'])
        if current_index + 1 < len(stored_attempts):
            guess_display_box['text'] = stored_attempts[current_index + 1]

def backwards():
    global stored_attempts
    if guess_display_box['text'] != 'Invalid attempt':
        current_index = stored_attempts.index(guess_display_box['text'])
        if current_index - 1 > -1:
            guess_display_box['text'] = stored_attempts[current_index - 1]

def myFunc(e):
  return e['score']

def view_highscores(difficulty_table):
    if not game_in_progress:
        current_highscore_table = ''''''
        easy = []
        medium = []
        hard = []
        if difficulty_table == 'easy':
            print('easy')
            with open ('easy.txt', 'r') as reader:
                storage = reader.readlines()
            print(storage)
            for index in storage:
                currentPlayer = index.split(' ')
                nameAndScore = {'name' : currentPlayer[0] , 'score' : currentPlayer[1].strip()}
                easy.append(nameAndScore)

            easy.sort(key=myFunc)
            for player_score in easy:
                current_highscore_table += str(player_score) + '\n'
            guess_display_box['text'] = current_highscore_table

        elif difficulty_table == 'medium':
            print('medium')
            with open ('medium.txt', 'r') as reader:
                storage = reader.readlines()
            print(storage)
            for index in storage:
                currentPlayer = index.split(' ')
                nameAndScore = {'name' : currentPlayer[0] , 'score' : currentPlayer[1].strip()}
                medium.append(nameAndScore)

            medium.sort(key=myFunc)
            for player_score in medium:
                current_highscore_table += str(player_score) + '\n'
            guess_display_box['text'] = current_highscore_table

        elif difficulty_table == 'hard':
            print('hard')
            with open ('hard.txt', 'r') as reader:
                storage = reader.readlines()
            print(storage)
            for index in storage:
                currentPlayer = index.split(' ')
                nameAndScore = {'name' : currentPlayer[0] , 'score' : currentPlayer[1].strip()}
                hard.append(nameAndScore)

            hard.sort(key=myFunc)
            for player_score in hard:
                current_highscore_table += str(player_score) + '\n'
            guess_display_box['text'] = current_highscore_table

def randomNumber(difficulty):
    global password
    global selected_difficulty
    global game_in_progress
    global stored_attempts
    stored_attempts.clear()
    selected_difficulty = ''
    if difficulty == 'easy':
        selected_difficulty = 'easy'
        num1 = random.randint(1,9)
        num2 = random.randint(0,9)
        while True:
            if num2 != num1:
                break
            else:
                num2 = random.randint(0,9)
        num3 = random.randint(0,9)
        while True:
            if (num3 != num2) and (num3 != num1):
                break
            else:
                num3 = random.randint(0,9)
        num4 = random.randint(0,9)
        while True:
            if (num4 != num3) and (num4 != num2) and (num4 != num1):
                break
            else:
                num4 = random.randint(0,9)
        guess_label['text'] = 'please enter a guess (4 numbers)'
        password = str(num1) + str(num2) + str(num3) + str(num4)

    elif difficulty == 'medium':
        selected_difficulty = 'medium'
        num1 = random.randint(1,9)
        num2 = random.randint(0,9)
        while True:
            if num2 != num1:
                break
            else:
                num2 = random.randint(0,9)
        num3 = random.randint(0,9)
        while True:
            if (num3 != num2) and (num3 != num1):
                break
            else:
                num3 = random.randint(0,9)
        num4 = random.randint(0,9)
        while True:
            if (num4 != num3) and (num4 != num2) and (num4 != num1):
                break
            else:
                num4 = random.randint(0,9)
        num5 = random.randint(0,9)
        while True:
            if (num5 != num4) and (num5 != num3) and (num5 != num2) and (num5 != num1):
                break
            else:
                num5 = random.randint(0,9)
        guess_label['text'] = 'please enter a guess (5 numbers)'
        password = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)

    elif difficulty == 'hard':
        selected_difficulty = 'hard'
        num1 = random.randint(1,9)
        num2 = random.randint(0,9)
        while True:
            if num2 != num1:
                break
            else:
                num2 = random.randint(0,9)
        num3 = random.randint(0,9)
        while True:
            if (num3 != num2) and (num3 != num1):
                break
            else:
                num3 = random.randint(0,9)
        num4 = random.randint(0,9)
        while True:
            if (num4 != num3) and (num4 != num2) and (num4 != num1):
                break
            else:
                num4 = random.randint(0,9)
        num5 = random.randint(0,9)
        while True:
            if (num5 != num4) and (num5 != num3) and (num5 != num2) and (num5 != num1):
                break
            else:
                num5 = random.randint(0,9)
        num6 = random.randint(0,9)
        while True:
            if (num6 != num5) and (num6 != num4) and (num6 != num3) and (num6 != num2) and (num6 != num1):
                break
            else:
                num6 = random.randint(0,9)
        guess_label['text'] = 'please enter a guess (6 numbers)'
        password = str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6)

    #print(password)
    game_in_progress = TRUE
    


def check_answer(current_guess):
    global loop
    global game_in_progress
    global stored_attempts
    guess_entry_box.delete(0, END)
    position = 0
    count = 0
    if len(current_guess) == len(password):
        if name_entry.get() != '':
            for char in password:
                if char in current_guess:
                    count +=1
            for i in range(0, len(password)):
                if password[i] == current_guess[i]:
                    position += 1

            guess_display_box['text'] = ''

            if position == len(password):
                player_name = name_entry.get()
                if selected_difficulty == 'easy':
                    print('easy')
                    easy = {}
                    with open ('easy.txt', 'r') as reader:
                        storage = reader.readlines()
                    print(len(storage))
                    if len(storage) > 0:
                        print('adding score')
                        for index in storage:
                            currentPlayer = index.split(' ')
                            easy[currentPlayer[0]] = currentPlayer[1].strip()
                        keys = easy.keys()
                        if (player_name in keys):
                            if int(easy[player_name]) > loop:
                                easy[player_name] = str(loop)
                        else:
                            print('new player score')
                            easy[player_name] = str(loop)
                    else:
                        easy[player_name] = str(loop)
                    keys = easy.keys()
                    with open ('easy.txt','w') as writer: 
                        for key in keys:
                            writer.write(key + ' ' + easy[key])
                            writer.write('\n')
                elif selected_difficulty == 'medium':
                    medium = {}
                    with open ('medium.txt', 'r') as reader:
                        storage = reader.readlines()
                    if (len(storage) > 0):
                        for index in storage:
                            currentPlayer = index.split(' ')
                            medium[currentPlayer[0]] = currentPlayer[1].strip()
                        keys = medium.keys()
                        if (player_name in keys):
                            if int(medium[player_name]) > loop:
                                medium[player_name] = str(loop)
                        else:
                            medium[player_name] = str(loop)
                    else:
                        medium[player_name] = str(loop)
                    keys = medium.keys()
                    with open ('medium.txt', 'w') as writer: 
                        for key in keys:
                            writer.write(key + ' ' + medium[key])
                            writer.write('\n')
                elif selected_difficulty == 'hard':
                    hard = {}
                    with open ('hard.txt', 'r') as reader:
                        storage = reader.readlines()
                    if len(storage) > 0:
                        for index in storage:
                            currentPlayer = index.split(' ')
                            hard[currentPlayer[0]] = currentPlayer[1].strip()
                        keys = hard.keys()
                        if (player_name in keys):
                            if int(hard[player_name]) > loop:
                                hard[player_name] = str(loop)
                        else:
                            hard[player_name] = str(loop)
                    else:
                        hard[player_name] = str(loop)
                    keys = hard.keys()
                    with open ('hard.txt', 'w') as writer: 
                        for key in keys:
                            writer.write(key + ' ' + hard[key])
                            writer.write('\n')
                
                guess_display_box['text'] += '\npassword correct'
                game_in_progress = False

            elif count == len(password) and position < len(password):
                guess_display_box['text'] += f'''
        \n ================================================== 
    attempt: {loop} (4 numbers) 
    your attempt was: {current_guess} 
    you got {count} correct, however {position} were in the right positon 
        =================================================== '''
                loop += 1

            elif count == 0 and position == 0:
                guess_display_box['text'] += f'''
        \n ================================================== 
    attempt: {loop} (4 numbers) 
    your attempt was: {current_guess} 
    you got {count} correct 
        ==================================================== '''
                loop += 1

            else:
                guess_display_box['text'] += f'''
        \n ================================================== 
    attempt: {loop} (4 numbers) 
    your attempt was: {current_guess} 
    you got {count} correct, however {position} were in the right positon 
        ==================================================== '''
                loop += 1

            if loop == 11:
                guess_display_box['text'] += f'''
        \n ================================================== 
    the password was: {password} 
        ==================================================== '''
                loop += 1
                game_in_progress = False

            stored_attempts.append(guess_display_box['text'])
        else:
            guess_display_box['text'] = 'Please enter your name'
    else:
        guess_display_box['text'] = 'Invalid attempt'
loop = 1
stored_attempts = []
game_in_progress = False

mainscreen = Tk()
mainscreen.title('Password-Guessing-Game')
mainscreen.geometry('600x425')
#mainscreen.attributes('-fullscreen', True)

#left side
frame1 = Frame(master=mainscreen, width=200, height=200, bg="red")
frame1.pack(fill=BOTH, side=LEFT)
frame1.pack_propagate(FALSE)

name_label = Label(master=frame1, bg='red', width=200, text='please enter your name', fg='white')
name_label.pack(anchor=N)

name_entry = Entry(master=frame1, bg='white', width=200)
name_entry.pack(anchor=N)

difficulty = Label(master=frame1, bg='red', width=200, text='please select a difficulty', fg='white')
difficulty.pack(anchor=N)
easy = Button(master=frame1, text='Easy', width=200, bg='white', command= lambda: randomNumber('easy'))
medium = Button(master=frame1, text='Medium', width=200, bg='white', command= lambda: randomNumber('medium'))
hard = Button(master=frame1, text='Hard', width=200, bg='white', command= lambda: randomNumber('hard'))
easy.pack(anchor=N)
medium.pack(anchor=N)
hard.pack(anchor=N)

guess_label = Label(master=frame1, bg='red', width=200, text='', fg='white')
guess_label.pack(anchor=N)

guess_entry_box = Entry(master=frame1, bg='white', width=200)
guess_entry_box.pack(anchor=N)

submit = Button(master=frame1, text='Submit', width=20, padx=50, pady=30, bg='blue', fg='white', command= lambda: check_answer(guess_entry_box.get()))
submit.pack(anchor=N)

highscores = Label(master=frame1, bg='red', width=200, text='Highscore Tables', fg='white')
highscores.pack(anchor=N)

highscore_table_easy = Button(master=frame1, text='Easy', width=200, bg='white', command= lambda: view_highscores('easy'))
highscore_table_medium = Button(master=frame1, text='Medium', width=200, bg='white', command= lambda: view_highscores('medium'))
highscore_table_hard = Button(master=frame1, text='Hard', width=200, bg='white', command= lambda: view_highscores('hard'))
highscore_table_easy.pack(anchor=N)
highscore_table_medium.pack(anchor=N)
highscore_table_hard.pack(anchor=N)

#right side
frame_2 = Frame(master=mainscreen, width=400, height=600, bg='red')
frame_2.pack(side=LEFT)
frame_2.pack_propagate(FALSE)

guess_display_box = Label(master=frame_2, text='''''', bg="white", anchor=NW, height=24)

go_forward = Button(master=frame_2, text= 'Forward', width=200, bg='blue', fg='white', command= lambda: forward())
go_back = Button(master=frame_2, text= 'Back', width=200, bg='blue', fg='white', command= lambda: backwards())

guess_display_box.pack(fill=BOTH)
go_forward.pack(anchor=N)
go_back.pack(anchor=N)

mainscreen.mainloop()

