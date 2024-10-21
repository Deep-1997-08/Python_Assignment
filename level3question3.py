def write_initial_content(filename):
    with open(filename, 'w') as file:
        content = input("Enter the content you want to write into the file:\n")
        file.write(content)

def JtoI(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        corrected_content = content.replace('J', 'I')
        
        with open(filename, 'w') as file:
            file.write(corrected_content)
        
        print("The content has been corrected and written back to the file.")
    
    except FileNotFoundError:
        print("The file does not exist.")

filename = 'WORDS.TXT'

write_initial_content(filename)
JtoI(filename)
