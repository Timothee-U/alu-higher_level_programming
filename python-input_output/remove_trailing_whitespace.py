def remove_trailing_whitespace(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line.rstrip() + '\n')  # Removes trailing spaces and writes the line back

# Call the function
remove_trailing_whitespace('2-append_write.py')
