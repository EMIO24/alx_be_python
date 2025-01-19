try:
    file = open('python', 'w')
    content = file.write('I am a python programmer')
    print(content)
    
    
except FileNotFoundError:
    print("Open a already existing file")
    