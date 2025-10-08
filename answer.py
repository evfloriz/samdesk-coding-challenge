'''
Advent of Code 2024 - Day 4: Ceres Search

For Samdesk
'''

def part_one(input):
    '''
    Idea:
    - Find every X, and for every X check for M A S in all 8 possible directions
        - Some directions not possible close to the edges

    Potential improvement:
    - Could speed up by finding the least used letter, as that is the max number of XMAS strings possible
    - Would require an initial count of letters
    - In this case X has the least anyway
    '''
    result = 0

    x = len(input)
    y = len(input[0])
    for i in range(x):
        for j in range(y):
            if (input[i][j] == "X"):
                '''
                valid_direction indices correspond to the following directions:
                0 1 2
                3 _ 4
                5 6 7
                '''
                valid_direction = [True] * 8

                # Boundary checking
                if (i < 3):
                    valid_direction[0] = False
                    valid_direction[1] = False
                    valid_direction[2] = False
                
                if (i > x - 4):
                    valid_direction[5] = False
                    valid_direction[6] = False
                    valid_direction[7] = False

                if (j < 3):
                    valid_direction[0] = False
                    valid_direction[3] = False
                    valid_direction[5] = False

                if (j > y - 4):
                    valid_direction[2] = False
                    valid_direction[4] = False
                    valid_direction[7] = False

                # Check if neighbors are valid characters and set valid direction to false as we don't need to check further
                for index, letter in enumerate(["M", "A", "S"], start=1):
                
                    if valid_direction[0] and input[i-index][j-index] != letter:
                        valid_direction[0] = False
                        
                    if valid_direction[1] and input[i-index][j] != letter:
                        valid_direction[1] = False
                        
                    if valid_direction[2] and input[i-index][j+index] != letter:
                        valid_direction[2] = False
                    
                    if valid_direction[3] and input[i][j-index] != letter:
                        valid_direction[3] = False
                    
                    if valid_direction[4] and input[i][j+index] != letter:
                        valid_direction[4] = False

                    if valid_direction[5] and input[i+index][j-index] != letter:
                        valid_direction[5] = False
                        
                    if valid_direction[6] and input[i+index][j] != letter:
                        valid_direction[6] = False
                    
                    if valid_direction[7] and input[i+index][j+index] != letter:
                        valid_direction[7] = False

                # Add number of remaining valid directions to result as this is the number of valid strings starting from input[i][j]
                result += sum([int(value) for value in valid_direction])

    return result


def part_two(input):
    '''
    Idea
    - find every A not including the ones on the outermost edges of the input
    - check the four diagonal positions for each A
    - make both diagonals valid values
    '''
    result = 0

    x = len(input)
    y = len(input[0])
    for i in range(1, x - 1):
        for j in range(1, y - 1):
            if (input[i][j] == "A"):
                
                if (((input[i-1][j-1] == 'M' and input[i+1][j+1] == 'S') or 
                    (input[i-1][j-1] == 'S' and input[i+1][j+1] == 'M')) and
                   ((input[i-1][j+1] == 'M' and input[i+1][j-1] == 'S') or 
                    (input[i-1][j+1] == 'S' and input[i+1][j-1] == 'M'))):
                   
                   result += 1
                    
    return result


def main():
    filename = "input.txt"
    input = []
    
    # Process input file into array
    with open(filename, "r") as file:
        for line in file:
            line_array = []
            for c in line.strip():
                line_array.append(c)
            input.append(line_array)
    
    part_one_result = part_one(input)
    print("Part one result: " + str(part_one_result))       # Part one result is 2483

    part_two_result = part_two(input)
    print("Part one result: " + str(part_two_result))       # Part one result is 1925


if __name__ == "__main__":
    main()