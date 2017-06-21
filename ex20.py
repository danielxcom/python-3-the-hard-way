from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read()) # Print whole file. The marker is now at the end

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end='') # Concat variable and funtion. End with no new line

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file) # After print the marker is at the end

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
