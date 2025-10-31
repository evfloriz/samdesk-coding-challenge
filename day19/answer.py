'''
Advent of Code 2024 - Day 19: Linen Layout
https://adventofcode.com/2024/day/19

For Samdesk
'''

def find_patterns(input):
    return 0

def main():
    filename = "input_test.txt"
    input = []
    
    # Process input file into array
    with open(filename, "r") as file:
        for line in file:
            line_array = []
            for c in line.strip():
                line_array.append(c)
            input.append(line_array)
    
    result = find_patterns(input)
    print("Result: " + str(result))


if __name__ == "__main__":
    main()
    