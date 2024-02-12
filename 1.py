import math

def calculate_pipe_length(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)

def validate_input(room_size, point1, point2):
    x_max, y_max, z_max = room_size
    for point in [point1, point2]:
        x, y, z = point
        if (x != 0 and x != x_max) and (y != 0 and y != y_max) and (z != 0 and z != z_max):
            return False
        if x < 20 or x > (x_max - 20) or y < 20 or y > (y_max - 20) or z < 20 or z > (z_max - 20):
            return False
    return True

def main():
    try:
        print("Rozměr místnosti:")
        room_size = tuple(map(int, input().split()))
        if any(size <= 0 for size in room_size):
            print("Nesprávný vstup.")
            return

        print("Bod 1:")
        point1 = tuple(map(int, input().split()))
        print("Bod 2:")
        point2 = tuple(map(int, input().split()))
        
        if not validate_input(room_size, point1, point2):
            print("Nesprávný vstup.")
            return

        pipe_length = calculate_pipe_length(point1, point2)
        hose_length = calculate_pipe_length((0, 0, 0), point1) + calculate_pipe_length((0, 0, 0), point2)
        
        print(f"Délka potrubí: {pipe_length:.6f}")
        print(f"Délka hadice: {hose_length:.6f}\n")
    except ValueError:
        print("ERROR.\n")

if __name__ == "__main__":
    while True:
        main()