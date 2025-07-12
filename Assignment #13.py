# 1. Create a file named data.txt, write 3 lines of text in it
with open("data.txt", "w") as file:
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

    # 2. Open data.txt in read mode, read all lines, and print each line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

        # 3. Use readlines() to read all lines and print each line with its line number
with open("data.txt", "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        print(f"{i + 1}: {line.strip()}")

        # 4. Append a new line to data.txt, then read and print updated content
with open("data.txt", "a") as file:
    file.write("This is the new line.\n")
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
        
        # 5. Use with open() to read and print each line with numbers
with open("data.txt", "r") as file:
    for i, line in enumerate(file):
        print(f"{i + 1}: {line.strip()}")

          
        # 6. Write numbers 1 to 10 to numbers.txt, read and print the sum
with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i}\n")
sum_of_numbers = 0
with open("numbers.txt", "r") as file:
    for line in file:
        sum_of_numbers += int(line.strip())
print(f"The sum of numbers in numbers.txt is: {sum_of_numbers}")
        
        # 7. Write even numbers from 1 to 50 to even_numbers.txt
with open("even_numbers.txt", "w") as file:
    for i in range(2, 51, 2):
        file.write(f"{i}\n")

        # 8. Write student names to students.txt, then read and print name lengths
with open("students.txt", "w") as file:
    file.write("ANEES\n")
    file.write("ASIM\n")
    file.write("AHMAD\n")
    file.write("ARMAN\n")
with open("students.txt", "r") as file:
    for line in file:
        name = line.strip()
        print(f"{name}: {len(name)}")

        # 9. Write and search for "Python" in info.txt
with open("info.txt", "w") as file:
    file.write("This file contains information about programming.\n")
    file.write("We are learning Python.\n")
search_term = "Python"
found = False
with open("info.txt", "r") as file:
    for line in file:
        if search_term in line:
            found = True
            break
if found:
    print("Python found")
else:
    print("Not found")
         
         # 10. Read data.txt, convert to uppercase, write to output.txt
with open("data.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())
print("Converted data.txt to uppercase and saved to output.txt")