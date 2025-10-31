'''
Advent of Code 2024 - Day 19: Linen Layout
https://adventofcode.com/2024/day/19

For this problem, designs are made up of combinations of patterns.
The objective of part one is to return how many designs are possible to create with the given patterns.
The objective of part two is to return how many different sequences of patterns work to create each design.

For Samdesk


Results
-------------
input.txt (from Advent of Code)
    Part 1: 355
    Part 2: 732978410442050

input2.txt (from Samdesk)
    Part 1: 369
    Part 2: 761826581538190
'''


def solve_puzzle(patterns, designs, part_one):
    '''
    Idea:
    For each index in a design string, calculate how many possible valid pattern sequences there are up to that index
    For example: if there are 3 valid ways to reach index i, then finding a valid 2-char pattern means there are 3 valid ways to
        reach index i+2, and finding another valid 2-char pattern means there are 6 valid ways to reach index i+2

    Basically an iterative bottom-up dynamic programming approach.

    For part one, we can early-out once we've found a single possibility of reaching the end of a design sequence
    For part two, we continue counting all possible configurations
    '''
    
    total = 0
    
    for design in designs:
        memo = [0 for i in range(len(design) + 1)]
        memo[0] = 1         # 1 way to have 0 chars

        for index in range(len(design)):
            # Check pattern validity at index
            # Update memo of corresponding index if pattern is valid

            # Skip index if there are valid sequences to get there
            if memo[index] == 0:
                continue

            for pattern in patterns:
                if design.startswith(pattern, index):
                    memo[index + len(pattern)] += memo[index]
                    

        if part_one:
            if memo[-1] > 0:
                total += 1
        else:
            total += memo[-1]

    return total


def main():
    #filename = "input_test.txt"
    filename = "input.txt"
    #filename = "input2.txt"
    #filenames = {"input.txt, input2.txt"}
    
    
    # Process input file
    with open(filename, "r") as file:
        # First line is comma-separated list of available towels
        line = file.readline()
        patterns = [word.strip() for word in line.split(',')]

        # Skip a line
        file.readline()

        # Remaining lines are patterns
        designs = []
        for line in file:
            designs.append(line.strip())
    
    result = solve_puzzle(patterns, designs, part_one=True)
    print("Part 1 Result: " + str(result))

    result = solve_puzzle(patterns, designs, part_one=False)
    print("Part 2 Result: " + str(result))


if __name__ == "__main__":
    main()
    