file_path = 'C:/Users/artem/Documents/Source Code/Python-Text-Book/Test files/test.txt'
with open(file_path, encoding="utf8") as f:
    file = f.read()
    print (file)
    f.seek(0) 
    
    for line in f:
        print(line.strip())
    
    f.seek(0) 
    lines = f.readlines()
    
    
for line in lines:
    print(line.strip())