import easygui
import os
import PIL
import time

# Right click on import PIl and install it to your device

# Dictionary that stores the different combos available
combos = {
    "VALUE":
        {"Beef burger": 5.69,
         "Fries": 1.00,
         "Fizzy drink": 1.00
         },
    "CHEEZY":
        {"Cheeseburger": 6.69,
         "Fries": 1.00,
         "Fizzy drink": 1.00
         },
    "SUPER":
        {"Cheeseburger": 6.69,
         "Large fries": 2,
         "Smoothie": 2
         }
}

# Finds where the image is in the user's files
logo_image = os.environ['USERPROFILE'] + "\\Downloads\\burger logo.jpg"


def welcome():
    # Welcome and logo
    easygui.msgbox("WELCOME TO TRUMP'S BURGER TRUCK!", "Trump's burgers", image=logo_image)
    # Displays the different options for the combos
    menu_choices = easygui.buttonbox("Pick one of the below options for the Burger Menu", "Burger Menu Options",
                                     choices=("View Menu", "Add Combo", "Remove Combo", "Change Combo", "Exit Menu"))
    # If the user wants to exit the combos menu it waits 0.75sec then goes to main menu
    if menu_choices == "Exit Menu":
        time.sleep(0.75)
        welcome()

    # Calls the combo_print function
    elif menu_choices == "View Menu":
        time.sleep(0.75)
        combo_print()


def combo_print():
    for combo_id, combo_info in combos.items():
        print(f"\nCombo ID: {combo_id}")

        for key in combo_info:
            print(f"{key}: {combo_info[key]}")


def add_combo():
    # gets new combo name from user and adds to dict
    new_combo = easygui.enterbox("Enter the name of the new combo", "Combo Name", image=logo_image)
    combos[new_combo] = {}

    # Adds burger item to the new combo
    burger = easygui.enterbox("Enter the burger in combo", "Burger in Combo")
    burger_price = easygui.enterbox("Enter the Price of the burger (0.00)", "Burger Price")
    burger_price = float(burger_price)
    combos[new_combo][burger] = burger_price

    # Adds side item to the new combo
    burger = easygui.enterbox("Enter the side in combo", "Burger in Combo")
    burger_price = easygui.enterbox("Enter the Price of the side (0.00)", "Side Price")
    burger_price = float(burger_price)
    combos[new_combo][burger] = burger_price

    # Adds drink item to the new combo
    burger = easygui.enterbox("Enter the drink in combo", "Burger in Combo",)
    burger_price = easygui.enterbox("Enter the Price of the drink (0.00)", "Drink Price")
    burger_price = float(burger_price)
    combos[new_combo][burger] = burger_price

    print(combos)


add_combo()
