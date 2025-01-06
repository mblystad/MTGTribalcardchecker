# MTGTribalcardchecker
A simple app that checks for new tribal creature cards and writes these to a txt file. Based on the mtgsdk library. Written with a great deal of help from copilot/chatgtp. 



# Freesh Tribal Card Checker

## Overview

The **Freesh Tribal Card Checker** is a simple Python GUI application designed for Magic: The Gathering (MTG) enthusiasts. It allows users to check for new creature cards of specific tribes (e.g., Elf, Vampire, Dragon) released within a selected date range. The results include detailed card information and a list formatted for easy import into tools like Moxfield.

## Features

- **Date Range Selection**: Choose start and end dates using an intuitive calendar widget.
- **Tribe Filtering**: Select from a dropdown list of popular MTG tribes (e.g., Angel, Goblin, Zombie).
- **Set Filtering**: Automatically filters MTG sets released within the chosen date range.
- **Card Details Export**: Outputs card details to a text file, including:
  - Card names
  - Types
  - Subtypes
  - Sets they belong to
- **Unique Card List**: Generates a list of unique cards formatted for Moxfield imports.
- **Dark-Themed GUI**: A clean and modern user interface built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).

## Installation

### Prerequisites

1. Python 3.8 or newer
2. Install the required libraries:

   ```bash
   pip install customtkinter tkcalendar pillow mtgsdk
   ```

## Usage

1. Run the program:
   ```bash
   python main.py
   ```

2. Use the GUI to:
   - Select a tribe from the dropdown.
   - Pick a start and end date using the calendar widgets.
   - Click **Check for Cards** to fetch and save tribal cards.

3. The results will be saved in a text file named:
   ```
   YYYY-MM-DD_to_YYYY-MM-DD_new_<tribe>.txt
   ```

   Example: `2023-01-01_to_2023-12-31_new_elf.txt`

4. Check the output file for:
   - Detailed card information.
   - A Moxfield-compatible list of unique cards.

## Project Structure

```
├── main.py             # Main application script
├── logo.PNG            # Logo image displayed in the GUI
├── requirements.txt    # Python dependencies
```

## Future Improvements

- Add support for multiple tribes in one query.
- Include image previews of the cards in the GUI.
- Enhance filtering options (e.g., rarity, color).
- Add support for different MTG formats.

## Contributions

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests to improve the app.


## Acknowledgments

- **Magic: The Gathering SDK**: For providing access to card data.
- **CustomTkinter**: For the modern GUI framework.
- **Pillow**: For image handling.
- **Tkcalendar**: For the calendar widget. 

---

Happy deckbuilding! 🎴
