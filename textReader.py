import os
import string
from collections import Counter
from tabulate import tabulate
from colorama import Fore, Style, init

# tabulate and coloroma must be installed first 
# pip install tabulate colorama

# Initializing the colorama
init()

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except Exception as e:
        print(Fore.RED + f"Error reading file: {e}" + Style.RESET_ALL)
        return None

def clean_text(text):
    # Removing punctuation while keeping the Unicode characters
    punctuations = string.punctuation + '።፣፤፥፦፧'    #it will filter all the punctuations including the punctuation found in amharic language such as ። ፣ ፤ ፥ ፦ ፧
    translator = str.maketrans('', '', punctuations)
    return text.translate(translator)

def word_frequency(text_lines):
    words = []
    for line in text_lines:
        clean_line = clean_text(line)
        words.extend(clean_line.split())
    
    word_count = Counter(words)
    return word_count.most_common()

def char_frequency(text_lines):
    text = ''.join(text_lines)
    text = clean_text(text)
    char_count = Counter(text.replace(" ", ""))
    return char_count.most_common(5)

def text_statistics(text_lines):
    total_lines = len(text_lines)
    total_words = sum(len(clean_text(line).split()) for line in text_lines)
    total_characters = sum(len(line) for line in text_lines)
    return total_lines, total_words, total_characters

def list_text_files():
    return [f for f in os.listdir() if f.endswith('.txt')]

def display_results(file_path):
    text_lines = read_file(file_path)
    if text_lines is None:
        return
    
    print(Fore.CYAN + "\nAnalyzing file:", file_path + Style.RESET_ALL)
    
    word_freq = word_frequency(text_lines)
    print(Fore.GREEN + "\nWord Frequency (in decreasing order):" + Style.RESET_ALL)
    print(tabulate(word_freq, headers=['Word', 'Frequency'], tablefmt='pretty'))
    
    char_freq = char_frequency(text_lines)
    print(Fore.GREEN + "\nTop 5 Character Frequency:" + Style.RESET_ALL)
    print(tabulate(char_freq, headers=['Character', 'Frequency'], tablefmt='pretty'))
    
    total_lines, total_words, total_characters = text_statistics(text_lines)
    stats = [
        ["Total Lines", total_lines],
        ["Total Words", total_words],
        ["Total Characters", total_characters]
    ]
    print(Fore.GREEN + "\nText Statistics:" + Style.RESET_ALL)
    print(tabulate(stats, tablefmt='pretty'))

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def about_developer():
    developers = [
        ["No.", "Name", "ID"],
        ["1", "Mesfin Aychiluhum", "1401775"],
        ["2", "Mhiret Kiros", "1401795"],
        ["3", "Elsa Abera", "1402648"],
        ["4", "Danawit Tarekegn", "1401100"],
        ["5", "Abigiya Elias", "1500002"],
        ["6", "Daniel Baye", "1401105"]
    ]
    
    print(Fore.YELLOW + "\n--- Developers ---" + Style.RESET_ALL)
    print(tabulate(developers, headers="firstrow", tablefmt="pretty", colalign=("left", "left", "left")))
    print("-----------------------------------")
    print("Department Of Software Engineering")
    print("Date : 12-10-2016 E.C")
    print("Team : Hardworkers Team")
    print("-----------------------------------")

def menu():
    while True:
        clear_console()
        print(Fore.BLUE + "\n --- Text File Analyzer Menu --- " + Style.RESET_ALL)
        print("1. Enter new file path with .txt file")
        print("2. Choose an existing text file in the current folder")
        print("3. About Developer")
        print("4. Exit")
        choice = input("Enter your choice (1, 2, 3, or 4): ")
        
        if choice == '1':
            file_path = input("Enter the full path of the text file: ")
            if os.path.isfile(file_path) and file_path.endswith('.txt'):
                display_results(file_path)
            else:
                print(Fore.RED + "Invalid file path or the file is not a .txt file. Please try again." + Style.RESET_ALL)
        
        elif choice == '2':
            text_files = list_text_files()
            if not text_files:
                print(Fore.RED + "No text files found in the current folder." + Style.RESET_ALL)
            else:
                print(Fore.BLUE + "\nAvailable text files:" + Style.RESET_ALL)
                for i, file in enumerate(text_files, start=1):
                    print(f"{i}. {file}")
                file_choice = input(f"Select a file by number (1-{len(text_files)}): ")
                if file_choice.isdigit() and 1 <= int(file_choice) <= len(text_files):
                    display_results(text_files[int(file_choice) - 1])
                else:
                    print(Fore.RED + "Invalid selection. Please try again." + Style.RESET_ALL)
        
        elif choice == '3':
            about_developer()
        
        elif choice == '4':
            print(Fore.GREEN + "Exiting the program. \nThankyou for using our app!" + Style.RESET_ALL)
            print(Fore.GREEN + "Good Bye!!" + Style.RESET_ALL)
            print(Fore.GREEN + "2016 E.C" + Style.RESET_ALL)
            break
        
        else:
            print(Fore.RED + "Invalid choice. Please enter 1, 2, 3, or 4." + Style.RESET_ALL)
        
        input("\nPress any key to continue...")

if __name__ == "__main__":
    menu()



