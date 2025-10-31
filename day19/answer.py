'''
Advent of Code 2024 - Day 19: Linen Layout
https://adventofcode.com/2024/day/19

For this problem, designs are made up of combinations of patterns.
The objective of part one is to return how many designs are possible to create with the given patterns.
The objective of part two is to return how many different sequences of patterns work to create each design.

For Samdesk


Results
-------------------------------
input.txt (from Advent of Code)
    Part 1: 355
    Part 2: 732978410442050

input2.txt (from Samdesk)
    Part 1: 369
    Part 2: 761826581538190
-------------------------------
'''


def find_counts_per_design(patterns, designs):
    '''
    Idea:
    - For each index in a design string, calculate how many possible valid pattern sequences there are up to that index and store in memo
    - For example: if there are 3 valid ways to reach index i, then finding a valid 2-char pattern starting at index i means there are 3 valid
        ways to reach index i+2, and finding another valid 2-char pattern means there are 6 valid ways to reach index i+2
    - Basically an iterative bottom-up dynamic programming approach

    For memo:
    - 0-th index represents an empty string
    - final index is result for full design string
    
    Returns a list of number of ways to make each design
    '''
    
    counts_per_design = []
    
    for design in designs:
        memo = [0 for i in range(len(design) + 1)]
        memo[0] = 1         # 1 way to have 0 chars

        for index in range(len(design)):
            # Skip index if there are no valid sequences to get there
            if memo[index] == 0:
                continue

            # Check pattern validity and update memo at corresponding index if valid
            for pattern in patterns:
                if design.startswith(pattern, index):
                    memo[index + len(pattern)] += memo[index]

        counts_per_design.append(memo[-1])

    return counts_per_design


def part_one(counts_per_design):
    return sum([1 for count in counts_per_design if count > 0])


def part_two(counts_per_design):
    return sum(counts_per_design)


def main():
    filenames = [
        "input.txt",
        "input2.txt"
    ]
    
    for filename in filenames:
        with open(filename, "r") as file:
            # First line is comma-separated list of patterns
            line = file.readline()
            patterns = [word.strip() for word in line.split(',')]

            # Skip a line
            file.readline()

            # Remaining lines are designs
            designs = []
            for line in file:
                designs.append(line.strip())
        
        counts_per_design = find_counts_per_design(patterns, designs)
        
        result1 = part_one(counts_per_design)
        result2 = part_two(counts_per_design)

        print(filename)
        print("Part 1 Result: " + str(result1))
        print("Part 2 Result: " + str(result2))


if __name__ == "__main__":
    main()
    