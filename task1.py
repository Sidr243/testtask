import sys

def circular_array_path(n, m):
    path = []
    current = 1
    while True:
        path.append(str(current))
        next_pos = (current + m - 1) % n
        if next_pos == 0:
            break
        current = next_pos if next_pos != 0 else n
    return ''.join(path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python circular_array.py <n> <m>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("n and m must be integers")
        sys.exit(1)
    
    print(circular_array_path(n, m))
