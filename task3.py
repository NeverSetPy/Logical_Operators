# Takes any number user inputs and prints stars across that amount of rows.
# Used 'Star Patterns with Python Loops Part 1 - Left Half Pyramid' YT video by Jovian for explanation of how code works.

height = int(input('Height of pattern:'))

for i in range (0, height): 
    for j in range(i+1):
        print('*', end='')
    print()
        