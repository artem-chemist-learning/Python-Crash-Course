def show_memebers(names):
    names.append('Nikulin')
    for i in range(len(names)):
        names[i] = names[i] +'!'
        print(names[i])

magicians = ['Copperfield', 'Houdini ', 'Potter']
print(magicians)
show_memebers(magicians[:])
print(magicians)

