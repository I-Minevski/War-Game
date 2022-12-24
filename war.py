from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox

root = Tk()
root.title("War Game")
root.geometry("900x600")
root.configure(background="green")

frame = Frame(root, bg="green")
frame.pack(pady=20)

# Resize Cards
def resize_cards(card):
    # Open the image
    card_img = Image.open(card)

    # Resize The Image
    card_resize_image = card_img.resize((150, 218))

    # output the card
    global card_image
    card_image = ImageTk.PhotoImage(card_resize_image)

    # Return that card
    return card_image


# Shuffle function
def shuffle():
    # Create a deck of cards
    global deck
    deck = [f"{rank}-{suit}"
            for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
            for suit in ["C", "D", "H", "S"]]
    random.shuffle(deck)
    # Create players
    global player1, player2
    player1 = deck[:26]
    player2 = deck[26:]


# Deal Out Cards
def deal():
    try:
        # Output Card To Screen
        global player1_image
        player1_image = resize_cards(f'D:\codene\Python\Kinter\STC\Images\cards\{player1[0]}.png')
        player1_label.config(image=player1_image)

        # Output Card To Screen
        global player2_image
        player2_image = resize_cards(f'D:\codene\Python\Kinter\STC\Images\cards\{player2[0]}.png')
        player2_label.config(image=player2_image)

        global cards_on_table
        cards_on_table = []
        cards_on_table.extend([player1[0], player2[0]])
        player1.remove(player1[0])
        player2.remove(player2[0])

        result = hand(cards_on_table[0], cards_on_table[1])

        if result == 1:
            player1.extend(cards_on_table)
        elif result == 2:
            player2.extend(cards_on_table)
        else:
            war_function()

        global turns
        #turns += 1
        print(turns)
        if turns >= 10:
            card_btn["state"] = DISABLED
            if len(player1) > len(player2):
                root.title("Player 1 wins!")
            elif len(player1) < len(player2):
                root.title("Player 2 wins!")

    except:
        if len(player1) == 0:
            root.title("Player 2 wins!")
        elif len(player2) == 0:
            root.title("Player 1 wins!")

    print(len(player1), len(player2))


# Compare Both Players' Cards
def hand(player1_card, player2_card):
    pairs = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    player1_score = player1_card.split("-")[0]
    player2_score = player2_card.split("-")[0]

    if player1_score.isdigit():
        player1_score = int(player1_score)
    else:
        player1_score = pairs[player1_score]

    if player2_score.isdigit():
        player2_score = int(player2_score)
    else:
        player2_score = pairs[player2_score]

    # Remove the cards that are on the table from both decks


    if player1_score > player2_score:
        result_label.config(text="Player 1 wins!")
        return 1
    elif player2_score > player1_score:
        result_label.config(text="Player 2 wins!")
        return 2
    else:
        result_label.config(text="It's a War!")
        return "war"


def war_function():
    # Open new window for the war
    messagebox.showinfo("War!", "Equal cards. Draw 3 more to determine the winner!")
    war = Toplevel()
    war.title("WAR!")

    # Create Frames for the Cards
    # war.geometry("900x500")
    war.configure(background="green")

    war_frame = Frame(war, bg="green")
    war_frame.pack(pady=20)

    player1_war_frame = LabelFrame(war_frame, text="Player 1", bd=0)
    player1_war_frame.grid(row=0, column=0, padx=20, pady=20, ipadx=20)
    player2_war_frame = LabelFrame(war_frame, text="Player 2", bd=0)
    player2_war_frame.grid(row=1, column=0, padx=20, pady=20, ipadx=20)

    player1_c1_frame = LabelFrame(player1_war_frame, text="Card 1", bd=0)
    player1_c1_frame.grid(row=0, column=0, padx=20, ipadx=20)
    player1_c2_frame = LabelFrame(player1_war_frame, text="Card 2", bd=0)
    player1_c2_frame.grid(row=0, column=1, padx=20, ipadx=20)
    player1_c3_frame = LabelFrame(player1_war_frame, text="Card 3", bd=0)
    player1_c3_frame.grid(row=0, column=2, padx=20, ipadx=20)

    player2_c1_frame = LabelFrame(player2_war_frame, text="Card 1", bd=0)
    player2_c1_frame.grid(row=0, column=0, padx=20, ipadx=20)
    player2_c2_frame = LabelFrame(player2_war_frame, text="Card 2", bd=0)
    player2_c2_frame.grid(row=0, column=1, padx=20, ipadx=20)
    player2_c3_frame = LabelFrame(player2_war_frame, text="Card 3", bd=0)
    player2_c3_frame.grid(row=0, column=2, padx=20, ipadx=20)

    # Resize the cards
    global p1_c1, p1_c2, p1_c3, p2_c1, p2_c2, p2_c3
    p1_c1 = resize_cards(f'D:\codene\Python\Kinter\STC\Images\cards\{player1[0]}.png')
    p1_c2 = resize_cards(f'D:\codene\Python\Kinter\STC\Images\cards\{player1[1]}.png')
    p1_c3 = resize_cards(f'D:\codene\Python\Kinter\STC\Images\cards\{player1[2]}.png')

    p2_c1 = resize_cards(f'D:\codene\Python\Kinter\STC\Images\cards\{player2[0]}.png')
    p2_c2 = resize_cards(f'D:\codene\Python\Kinter\STC\Images\cards\{player2[1]}.png')
    p2_c3 = resize_cards(f'D:\codene\Python\Kinter\STC\Images\cards\{player2[2]}.png')

    cards_on_table.extend([player1[0], player1[1], player1[2], player2[0], player2[1], player2[2]])

    # Put Cards in the Frames
    p1_label_c1 = Label(player1_c1_frame, image=p1_c1)
    p1_label_c1.pack(pady=20)
    p1_label_c2 = Label(player1_c2_frame, image=p1_c2)
    p1_label_c2.pack(pady=20)
    p1_label_c3 = Label(player1_c3_frame, image=p1_c3)
    p1_label_c3.pack(pady=20)

    p2_label_c1 = Label(player2_c1_frame, image=p2_c1)
    p2_label_c1.pack(pady=20)
    p2_label_c2 = Label(player2_c2_frame, image=p2_c2)
    p2_label_c2.pack(pady=20)
    p2_label_c3 = Label(player2_c3_frame, image=p2_c3)
    p2_label_c3.pack(pady=20)

    # Save the third cards of both players
    player1_card = player1[2]
    player2_card = player2[2]

    # Remove the cards that are on the table from both decks
    player1.remove(player1[2])
    player1.remove(player1[1])
    player1.remove(player1[0])
    player2.remove(player2[2])
    player2.remove(player2[1])
    player2.remove(player2[0])

    result = hand(player1_card, player2_card)

    if result == 1:
        result_label.config(text="Player 1 wins the war!")
        player1.extend(cards_on_table)
    elif result == 2:
        result_label.config(text="Player 2 wins the war!")
        player2.extend(cards_on_table)
    else:
        war_function()


# Shuffle the initial deck
shuffle()

global turns
turns = 0

# Create Frames for the Cards
player1_frame = LabelFrame(frame, text="Player 1", bd=0)
player1_frame.grid(row=0, column=0, padx=20, ipadx=20)

player2_frame = LabelFrame(frame, text="Player 2", bd=0)
player2_frame.grid(row=0, column=1, padx=20, ipadx=20)

# Put Cards in the Frames
player1_label = Label(player1_frame, text="")
player1_label.pack(pady=20)

player2_label = Label(player2_frame, text="")
player2_label.pack(pady=20)

result_label = Label(root, text="", font=("Helvetica", 14), bg="green")
result_label.pack(pady=20)

# Create Buttons
shuffle_btn = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_btn.pack(pady=20)

card_btn = Button(root, text="Get Card", font=("Helvetica", 14), command=deal)
card_btn.pack(pady=20)

# Display Cards on Start
player1_image = resize_cards(f'D:\\codene\\Python\\Kinter\\STC\\Images\\cards\\0card_back.png')
player1_label.config(image=player1_image)

player2_image = resize_cards(f'D:\\codene\\Python\\Kinter\\STC\\Images\\cards\\0card_back.png')
player2_label.config(image=player2_image)

root.mainloop()
