file_path = 'C:/Users/artem/Documents/Source Code/Python-Text-Book/Test files/test.txt'
with open(file_path, 'r', encoding="utf8") as f:
    for line in f:
        line = line.replace('This', 'That')
        print (line.strip())

