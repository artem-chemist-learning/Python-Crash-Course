def print_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf8') as f:
            file = f.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in file:
            print(line.strip())


file_1 = 'C:/Users/Documents/Source Code/Python-Text-Book/Test files/Cats.txt'
file_2 = 'C:/Users/artem/Documents/Source Code/Python-Text-Book/Test files/Dogs.txt'
files_to_read = [file_1, file_2]

for file in files_to_read:
    print_file(file)