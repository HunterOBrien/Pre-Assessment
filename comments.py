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
        time.sleep(1.5)
        welcome()


# uses two for loops to print the combo with good formatting
def combo_print():
    for combo_id, combo_info in combos.items():
        print(f"\nCombo ID: {combo_id}")

        for key in combo_info:
            print(f"{key}: {combo_info[key]}")

# Goes through each item in the new combo asking item name and price
def add_combo():
    combo_id = easygui.enterbox("Enter Combo ID: ", "Adjuster "
                                                    "9000",
                                image=logo_image).upper()
    burger = easygui.enterbox("Enter Burger: ", "Adjuster 9000",
                              image=logo_image).capitalize()
    burger_price = easygui.enterbox(f"Enter Price for {burger}\nDon't use "
                                    f"$ sign",
                                    "Adjuster 9000", image=logo_image)
    side = easygui.enterbox("Enter Side: ", "Adjuster 9000",
                            image=logo_image).capitalize()
    side_price = easygui.enterbox(f"Enter Price for {side}\nDon't use "
                                  f"$ sign",
                                  "Adjuster 9000", image=logo_image)
    drink = easygui.enterbox("Enter Drink: ", "Adjuster 9000",
                             image=logo_image).capitalize()
    drink_price = easygui.enterbox(f"Enter Price for {drink}\nDon't use "
                                   f"$ sign",
                                   "Adjuster 9000", image=logo_image)
    burger_price = float(burger_price)
    side_price = float(side_price)
    drink_price = float(drink_price)
    total_price = burger_price + side_price + drink_price
    option = easygui.ynbox(f"Is the order correct?\n{combo_id}\n{burger}: "
                           f"${burger_price}\n{side}: ${side_price}\n{drink}: "
                           f"${drink_price}\nTotal Price: $"
                           f"{total_price:.2f}", "Adjuster 9000", image=logo_image)
    if option:
        pass
    else:
        add_combo()
    combos[combo_id] = {}
    combos[combo_id][burger] = burger_price
    combos[combo_id][side] = side_price
    combos[combo_id][drink] = drink_price


# deletes a combo selected in easyGUI
def delete_combo():
    combo_list = []
    for i in combos:
        combo_list.append(i)
    option = easygui.multchoicebox("What combo(s) do you want to delete?", "Combo Deleter",
                                   choices=combo_list + ["Back to main menu"], preselect=[])
    if option is None:
        return
    if "Back to main menu" in option:
        welcome()
    else:
        for combo_to_delete in option:
            del combos[combo_to_delete]
        easygui.msgbox("Combo(s) successfully deleted", "Combo Deleter", image=logo_image)

# edits an existing combo in the menu
def change_combo():
    combo_list = []
    # asks user what combo they want to edit
    for i in combos:
        combo_list.append(i)
    combo_to_edit = easygui.choicebox("What combo do you want to edit?", "Combo Editor", combo_list)

    # if user does not want to enter any combo, they  are taken back to main menu
    if combo_to_edit is None:
        return welcome()

    # allows the user to choose what part of the combo to edit
    options = ["Burger", "Side", "Drink"]
    choice = easygui.choicebox(f"What do you want to edit for {combo_to_edit}?", "Combo Editor", options)
    if choice == "Burger":
        while True:
            new_burger = easygui.enterbox("Enter new burger name:", "Combo Editor")
            if new_burger == "":
                easygui.msgbox("Please enter a valid burger name.", "Error", image=logo_image)
            elif new_burger in combos[combo_to_edit]:
                easygui.msgbox("This burger is already part of the combo.", "Error", image=logo_image)
            else:
                break
        while True:
            new_price = easygui.enterbox(f"Enter price for {new_burger}:", "Combo Editor")
            try:
                new_price = float(new_price)
            except ValueError:
                easygui.msgbox("Please enter a valid price.", "Error", image=logo_image)
            else:
                break
        combos[combo_to_edit][new_burger] = new_price
        del combos[combo_to_edit]["Beef burger"]
    elif choice == "Side":
        while True:
            new_side = easygui.enterbox("Enter new side name:", "Combo Editor")
            if new_side == "":
                easygui.msgbox("Please enter a valid side name.", "Error", image=logo_image)
            elif new_side in combos[combo_to_edit]:
                easygui.msgbox("This side is already part of the combo.", "Error", image=logo_image)
            else:
                break
        while True:
            new_price = easygui.enterbox(f"Enter price for {new_side}:", "Combo Editor")
            try:
                new_price = float(new_price)
            except ValueError:
                easygui.msgbox("Please enter a valid price.", "Error", image=logo_image)
            else:
                break
        combos[combo_to_edit][new_side] = new_price
        del combos[combo_to_edit]["Fries"]
    elif choice == "Drink":
        while True:
            new_drink = easygui.enterbox("Enter new drink name:", "Combo Editor")
            if new_drink == "":
                easygui.msgbox("Please enter a valid drink name.", "Error", image=logo_image)
            elif new_drink in combos[combo_to_edit]:
                easygui.msgbox("This drink is already part of the combo.", "Error", image=logo_image)
            else:
                break
        while True:
            new_price = easygui.enterbox(f"Enter price for {new_drink}:", "Combo Editor")
            try:
                new_price = float(new_price)
            except ValueError:
                easygui.msgbox("Please enter a valid price.", "Error", image=logo_image)
            else:
                break
        combos[combo_to_edit][new_drink] = new_price
        del combos[combo_to_edit]["Fizzy drink"]
    return welcome()


welcome()
