#!/usr/bin/python3

# requires python 3.6 or above

import random
import time
import os
import argparse

BRIGHT_FOREGROUND_COLORS = [
    "\033[90m",  
    "\033[91m",  
    "\033[92m",  
    "\033[93m",  
    "\033[94m",  
    "\033[95m",  
    "\033[96m",  
    "\033[97m",  
]

BRIGHT_BACKGROUND_COLORS = [
    "\033[100m", 
    "\033[101m", 
    "\033[102m", 
    "\033[103m", 
    "\033[104m", 
    "\033[105m", 
    "\033[106m", 
    "\033[107m", 
]

DARK_FOREGROUND_COLORS = [
    "\033[30m",  
    "\033[31m",  
    "\033[32m",  
    "\033[33m",  
    "\033[34m",  
    "\033[35m",  
    "\033[36m",  
    "\033[37m",  
]

DARK_BACKGROUND_COLORS = [
    "\033[40m",  
    "\033[41m",  
    "\033[42m",  
    "\033[43m",  
    "\033[44m",  
    "\033[45m",  
    "\033[46m",  
    "\033[47m",  
]

MONOCHROME_FOREGROUND_COLORS = [
    "\033[90m",  
    "\033[37m",  
    "\033[97m",  
]

MONOCHROME_BACKGROUND_COLORS = [
    "\033[100m", 
    "\033[47m",  
    "\033[107m", 
]

BLACK_WHITE_FOREGROUND_COLORS = [
    "\033[30m",  
    "\033[37m",  
]

BLACK_WHITE_BACKGROUND_COLORS = [
    "\033[40m",  
    "\033[47m",  
]

RESET = "\033[0m"
CLEAR_SCREEN = "\033[2J\033[H"  

hiragana_chars = "".join([chr(i) for i in range(0x3040, 0x309F + 1)])
katakana_chars = "".join([chr(i) for i in range(0x30A0, 0x30FF + 1)])
JAPANESE_CHARACTERS = hiragana_chars + katakana_chars
LATIN_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:'\",.<>/?`~"
RUSSIAN_CHARACTERS = "".join([chr(i) for i in range(0x0400, 0x04FF + 1)])
ARABIC_CHARACTERS = "".join([chr(i) for i in range(0x0600, 0x06FF + 1)])
HANZI_KANJI_CHARACTERS = "".join([chr(i) for i in range(0x4E00, 0x9FFF + 1)])
TIFINAGH_CHARACTERS = "".join([chr(i) for i in range(0x2D30, 0x2D7F + 1)])
INUIT_CHARACTERS = "".join([chr(i) for i in range(0x1400, 0x167F + 1)])
BRAILLE_CHARACTERS = "".join([chr(i) for i in range(0x2800, 0x28FF + 1)])

extra_latin_chars_str = ""
extra_latin_chars_str += "".join([chr(i) for i in range(0x0080, 0x00FF + 1)]) 
extra_latin_chars_str += "".join([chr(i) for i in range(0x0100, 0x017F + 1)]) 
EXTRA_LATIN_CHARACTERS = LATIN_CHARACTERS + extra_latin_chars_str

CYRILLIC_EXTENDED_CHARACTERS = "".join([chr(i) for i in range(0x2DE0, 0x2DFF + 1)]) + \
                                 "".join([chr(i) for i in range(0xA640, 0xA69F + 1)])

GREEK_CHARACTERS = "".join([chr(i) for i in range(0x0370, 0x03FF + 1)]) + \
                   "".join([chr(i) for i in range(0x1F00, 0x1FFF + 1)])

SYMBOLS_CHARACTERS = "".join([chr(i) for i in range(0x25A0, 0x25FF + 1)]) + \
                     "".join([chr(i) for i in range(0x2600, 0x26FF + 1)]) + \
                     "".join([chr(i) for i in range(0x2700, 0x27BF + 1)])

EMPTY_BLOCK_CHARACTERS = "".join([chr(i) for i in range(0x2580, 0x259F + 1)]) 

def splatter_colors(use_dark_colors, char_set, glitchy_mode, monochrome_mode, black_white_mode):
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(CLEAR_SCREEN, end="") 

    if black_white_mode:
        foreground_colors = BLACK_WHITE_FOREGROUND_COLORS
        background_colors = BLACK_WHITE_BACKGROUND_COLORS
    elif monochrome_mode:
        foreground_colors = MONOCHROME_FOREGROUND_COLORS
        background_colors = MONOCHROME_BACKGROUND_COLORS
    elif use_dark_colors:
        foreground_colors = DARK_FOREGROUND_COLORS
        background_colors = DARK_BACKGROUND_COLORS
    else:
        foreground_colors = BRIGHT_FOREGROUND_COLORS
        background_colors = BRIGHT_BACKGROUND_COLORS

    if char_set == "latin":
        characters = LATIN_CHARACTERS
    elif char_set == "extra-latin":
        characters = EXTRA_LATIN_CHARACTERS
    elif char_set == "russian":
        characters = RUSSIAN_CHARACTERS
    elif char_set == "cyrillic-extended":
        characters = CYRILLIC_EXTENDED_CHARACTERS
    elif char_set == "arabic":
        characters = ARABIC_CHARACTERS
    elif char_set == "hanzi":
        characters = HANZI_KANJI_CHARACTERS
    elif char_set == "tifinagh":
        characters = TIFINAGH_CHARACTERS
    elif char_set == "inuit":
        characters = INUIT_CHARACTERS
    elif char_set == "braille":
        characters = BRAILLE_CHARACTERS
    elif char_set == "greek":
        characters = GREEK_CHARACTERS
    elif char_set == "symbols":
        characters = SYMBOLS_CHARACTERS
    elif char_set == "empty-blocks":
        characters = EMPTY_BLOCK_CHARACTERS
    else: 
        characters = JAPANESE_CHARACTERS

    try:
        while True:
            rows, cols = os.get_terminal_size()
            output_chars = []
            for _ in range(rows * cols): 
                fg_color = random.choice(foreground_colors)
                bg_color = random.choice(background_colors)
                char = random.choice(characters)

                if glitchy_mode:
                    glitch_chance = random.random()
                    if glitch_chance < 0.02: 
                        char = random.choice([" ", "\u2588", "\u2591", "\u2592", "\u2593"]) 
                        fg_color, bg_color = bg_color, fg_color 
                    elif glitch_chance < 0.05: 
                        char = random.choice(LATIN_CHARACTERS) 
                        fg_color = random.choice(BRIGHT_FOREGROUND_COLORS) 
                        bg_color = random.choice(BRIGHT_BACKGROUND_COLORS) 

                output_chars.append(f"{fg_color}{bg_color}{char}{RESET}")

            print(f"{CLEAR_SCREEN}{''.join(output_chars)}", end="")
            time.sleep(0.01)  
    except KeyboardInterrupt:
        print("\nSplatter stopped.")
        print(RESET) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
This script fills your terminal with a dynamic, colorful splatter of characters.
You can customize the character set, color scheme, and add glitch effects.
Press Ctrl+C to stop the splatter.

Color Scheme Options (choose one):
  --dark        Use a darker, less vibrant color palette for the splatter.
  --monochrome  Use a monochrome color scheme (dark gray, gray, light gray).
  --black-white Use a strict black and white color scheme.

Character Set Options (choose one, default is Japanese Hiragana/Katakana):
  --latin         Use basic Latin alphabet characters, numbers, and common symbols.
  --extra-latin   Use extended Latin characters, including accented letters and special symbols.
  --japanese      Use Japanese Hiragana and Katakana characters (default).
  --russian       Use Russian (Cyrillic) characters.
  --cyrillic-extended Use a broader range of Cyrillic characters, including historical and minority scripts.
  --arabic        Use Arabic script characters.
  --hanzi         Use common Hanzi/Kanji (Chinese/Japanese characters).
  --tifinagh      Use Tifinagh characters (used for Berber languages).
  --inuit         Use Inuit (Inuktitut Syllabics) characters.
  --braille       Use Braille patterns.
  --greek         Use Greek alphabet characters.
  --symbols       Use various geometric shapes, dingbats, and other symbols (often rendered as special glyphs by Nerd Fonts).
  --empty-blocks  Use Unicode block elements and shades to create abstract patterns.

Other Options:
  --glitchy       Introduce a random, 'glitchy' effect by occasionally swapping colors and characters.
""",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "--dark",
        action="store_true",
        help=argparse.SUPPRESS 
    )
    parser.add_argument(
        "--glitchy",
        action="store_true",
        help=argparse.SUPPRESS 
    )

    color_group = parser.add_mutually_exclusive_group()
    color_group.add_argument(
        "--monochrome",
        action="store_true",
        help=argparse.SUPPRESS 
    )
    color_group.add_argument(
        "--black-white",
        action="store_true",
        help=argparse.SUPPRESS 
    )

    char_group = parser.add_mutually_exclusive_group()
    char_group.add_argument(
        "--latin",
        action="store_const",
        const="latin",
        dest="char_set",
        help=argparse.SUPPRESS 
    )
    char_group.add_argument(
        "--extra-latin",
        action="store_const",
        const="extra-latin",
        dest="char_set",
        help=argparse.SUPPRESS 
    )
    char_group.add_argument(
        "--japanese",
        action="store_const",
        const="japanese",
        dest="char_set",
        help=argparse.SUPPRESS 
    )
    char_group.add_argument(
        "--russian",
        action="store_const",
        const="russian",
        dest="char_set",
        help=argparse.SUPPRESS 
    )
    char_group.add_argument(
        "--cyrillic-extended",
        action="store_const",
        const="cyrillic-extended",
        dest="char_set",
        help=argparse.SUPPRESS 
    )
    char_group.add_argument(
        "--arabic",
        action="store_const",
        const="arabic",
        dest="char_set",
        help=argparse.SUPPRESS 
    )
    char_group.add_argument(
        "--hanzi",
        action="store_const",
        const="hanzi",
        dest="char_set",
        help=argparse.SUPPRESS 
    )
    char_group.add_argument(
        "--tifinagh",
        action="store_const",
        const="tifinagh",
        dest="char_set",
        help=argparse.SUPPRESS 
    )
    char_group.add_argument(
        "--inuit",
        action="store_const",
        const="inuit",
        dest="char_set",
        help=argparse.SUPPRESS 
    )
    char_group.add_argument(
        "--braille",
        action="store_const",
        const="braille",
        dest="char_set",
        help=argparse.SUPPRESS 
    )
    char_group.add_argument(
        "--greek",
        action="store_const",
        const="greek",
        dest="char_set",
        help=argparse.SUPPRESS 
    )
    char_group.add_argument(
        "--symbols",
        action="store_const",
        const="symbols",
        dest="char_set",
        help=argparse.SUPPRESS 
    )
    char_group.add_argument(
        "--empty-blocks",
        action="store_const",
        const="empty-blocks",
        dest="char_set",
        help=argparse.SUPPRESS 
    )

    args = parser.parse_args()

    splatter_colors(args.dark, args.char_set if args.char_set else "japanese", args.glitchy, args.monochrome, args.black_white)
