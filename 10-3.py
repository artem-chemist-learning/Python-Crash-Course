file_path = 'C:/Users/artem/Documents/Source Code/Python-Text-Book/Test files/test10-3.txt'
with open(file_path, 'a', encoding="utf8") as f:
    while True:
        new_guest = input('Guest name (q to stop): ')
        if new_guest == 'q':
            break
        else:
            f.write(new_guest+'\n')

