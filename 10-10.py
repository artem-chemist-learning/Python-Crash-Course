def count_word(file_name, word):
    total = (False, 0)
    sum_result = 0
    try:
        with open(file_name, 'r', encoding='utf8') as f:
            file = f.readlines()
    except FileNotFoundError:
        return total
    else:
        for line in file:
            increment = line.lower().count(word)
            sum_result+=increment
        total = (True, sum_result)
        return total
            


file_1 = 'C:/Users/artem/Documents/Source Code/Python-Text-Book/Test files/Anna Karenina.txt'
file_2 = 'C:/Users/artem/Documents/Source Code/Python-Text-Book/Test files/The call of the wild.txt'
files_to_read = [file_1, file_2]

for file in files_to_read:
    word_to_count = 'dog'
    total_count = count_word(file, word_to_count)
    if total_count[0] == True:
        str_count = str(total_count[1])
        print('Total number of {} is {}'. format(word_to_count, str_count))