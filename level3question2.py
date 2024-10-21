def write_to_file(filename):
    with open(filename, 'w') as file:
        content = input("Enter the content you want to write into the file:\n")
        file.write(content)

def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return "The file does not exist."

filename = 'demo.txt'

write_to_file(filename)

line_count = count_lines_in_file(filename)
print(f"\nNumber of lines in '{filename}': {line_count}")
