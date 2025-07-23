import sys
import math

def calculate_position(circle_file, points_file):
    with open(circle_file, 'r') as f:
        center_x, center_y = map(float, f.readline().split())
        radius = float(f.readline())
    
    with open(points_file, 'r') as f:
        points = [tuple(map(float, line.split())) for line in f if line.strip()]
    
    results = []
    for x, y in points:
        distance_squared = (x - center_x)**2 + (y - center_y)**2
        radius_squared = radius**2
        
        if math.isclose(distance_squared, radius_squared, rel_tol=1e-9):
            results.append(0)
        elif distance_squared < radius_squared:
            results.append(1)
        else:
            results.append(2)
    
    return results

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python circle_point_position.py <circle_file> <points_file>")
        sys.exit(1)
    
    results = calculate_position(sys.argv[1], sys.argv[2])
    for result in results:
        print(result)
