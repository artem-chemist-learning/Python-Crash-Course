from collections import OrderedDict

PiDict = OrderedDict();

PiDict['Class'] = 'A abstract description of a potential object '
PiDict['Inheretance'] = 'A process of using one class as a basis to create another'
PiDict['Module'] = 'A file that stores some code that might be linked to another file'
PiDict['Object'] = 'A materialized instance of a class'
PiDict['Instantiation'] = 'A process of creating an object fitting a description in the class defitinition'

for key, value in PiDict.items():
    print(value)