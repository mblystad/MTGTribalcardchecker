import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import Calendar
from PIL import Image  # Import PIL's Image class for handling images
from mtgsdk import Card, Set


# Function to get sets released in a specific date range
def get_sets_released_in_range(start_date, end_date):
    all_sets = Set.all()
    selected_sets = []
    for mtg_set in all_sets:
        try:
            release_date = datetime.strptime(mtg_set.release_date, '%Y-%m-%d')
            if start_date <= release_date <= end_date:
                selected_sets.append(mtg_set)
        except TypeError:
            continue
    return selected_sets


# Function to get cards of a specific subtype from a set of MTG sets
def get_cards_from_sets(sets, subtype):
    cards = []
    for mtg_set in sets:
        set_code = mtg_set.code
        set_name = mtg_set.name
        set_cards = Card.where(set=set_code, subtypes=subtype).all()
        for card in set_cards:
            card.set_name = set_name  # Attach the set name to each card for later use
        cards.extend(set_cards)
    return cards


# Function to check for new tribal cards in the selected date range and write to file
def check_cards():
    tribe = combo.get()  # Get the selected tribe from the dropdown
    if not tribe:
        messagebox.showerror("Input Error", "Please select a tribe.")
        return

    try:
        start_date = datetime.strptime(cal_start.get_date(), '%Y-%m-%d')
        end_date = datetime.strptime(cal_end.get_date(), '%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Input Error", "Please select valid dates.")
        return

    sets_in_range = get_sets_released_in_range(start_date, end_date)
    tribe_cards = get_cards_from_sets(sets_in_range, tribe)

    # Extract unique card names
    unique_cards = list({card.name for card in tribe_cards})

    # Write tribal card details and unique cards to a file
    file_name = f"{cal_start.get_date()}_to_{cal_end.get_date()}_new_{tribe.lower()}.txt"
    with open(file_name, 'w') as file:
        if tribe_cards:
            card_lines = []  # To store lines about cards (for duplicate removal)
            file.write(f"Total Cards found: {len(tribe_cards)}\n\n")  # Write total number of tribe cards

            for card in tribe_cards:
                line = f"Name: {card.name}, Type: {card.type}, Subtypes: {card.subtypes}, Set: {card.set_name}\n"
                if line not in card_lines:  # Only add if not a duplicate
                    card_lines.append(line)

            # Write the filtered (unique) list to the file
            file.writelines(card_lines)

            # Write unique card list formatted for Moxfield
            file.write("\nUnique Cards for Moxfield Import:\n")
            for card in unique_cards:
                file.write(f"1 {card}\n")

            messagebox.showinfo("Success", f"New {tribe} cards have been written to {file_name}")
        else:
            file.write(f"No new {tribe} cards found in this date range.\n")
            messagebox.showinfo("Info", f"No new {tribe} cards found in this date range.")


# Create the GUI using customtkinter
ctk.set_appearance_mode("Dark")  # Force the dark theme
ctk.set_default_color_theme("blue")  # Available themes: 'blue', 'green', 'dark-blue'

root = ctk.CTk()
root.title("Freesh Tribal Card Checker")
root.geometry("600x900")  # Increase the window size to fit everything comfortably

# Open the image and create CTkImage with size parameter
image_path = "logo.PNG"
image = Image.open(image_path)

# Pass the desired size to CTkImage directly
ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(200, 200))  # Resize to 200x200

# Add a label to display the image
logo_label = ctk.CTkLabel(root, image=ctk_image, text="")  # Set the image in the label
logo_label.pack(pady=20)  # Add padding to give breathing space around the image

# Set a modern bold font for the entire app
font_bold = ctk.CTkFont(size=16, weight="bold")
font_regular = ctk.CTkFont(size=14)

# Add a label for the dropdown list title with a bold font
ctk.CTkLabel(root, text="Select a Tribe:", font=font_bold).pack(pady=10)

# Add the dropdown (Combobox) for tribe selection
combo = ctk.CTkComboBox(
    root,
    values=[
        "Angel", "Beast", "Cat", "Cleric", "Demon", "Dinosaur", "Dragon", "Elf", "Elemental", "Fairie", "Goblin",
        "Human", "Knight", "Merfolk", "Minotaur", "Rat", "Sliver", "Soldier", "Spirit", "Vampire", "Warrior",
        "Wizard", "Zombie"
    ],
    font=font_regular,  # Apply a regular but modern font to combobox
    dropdown_font=font_regular  # Ensure the dropdown list also uses the same font
)
combo.pack(pady=10)

# Add a calendar widget for start date selection with a bold label
ctk.CTkLabel(root, text="Select Start Date:", font=font_bold).pack(pady=10)
cal_start = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal_start.pack(pady=10)  # Adjust padding for better appearance

# Add a calendar widget for end date selection with a bold label
ctk.CTkLabel(root, text="Select End Date:", font=font_bold).pack(pady=10)
cal_end = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal_end.pack(pady=10)  # Adjust padding for better appearance

# Add a button to trigger the card check with a bold font and modern size
check_button = ctk.CTkButton(root, text="Check for Cards", command=check_cards, width=200, height=50, font=font_bold)
check_button.pack(pady=30)  # Add extra padding at the bottom to balance the UI layout

# Start the customtkinter main loop
root.mainloop()
