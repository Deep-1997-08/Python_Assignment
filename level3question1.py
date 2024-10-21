def write_to_file(filename):
    with open(filename, 'w') as file:
        content = input("Enter the content you want to write into the file:\n")
        file.write(content)
        
def read_even_length_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        even_length_lines = []
        for line in lines:
            words = line.split()
            even_length_words = [word for word in words if len(word) % 2 == 0]
            even_length_lines.append(' '.join(even_length_words))
        
        return '\n'.join(even_length_lines)
    
    except FileNotFoundError:
        return "The file does not exist."

filename = 'doc.txt'
write_to_file(filename)

result = read_even_length_words(filename)
print(result)
