import sys

def min_moves(nums):
    nums_sorted = sorted(nums)
    median = nums_sorted[len(nums_sorted) // 2]
    return sum(abs(num - median) for num in nums)

def read_numbers_from_file(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python min_moves_to_equal_elements.py <input_file>")
        sys.exit(1)
    
    numbers = read_numbers_from_file(sys.argv[1])
    print(min_moves(numbers))
