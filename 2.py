def are_collinear(x1, y1, x2, y2, x3, y3):
    determinant = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
    return determinant == 0

def midpoint(x1, y1, x2, y2, x3, y3):
    return (x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3

def main():
    try:
        print("Bod A:")
        x1, y1 = map(float, input().split())
        print("Bod B:")
        x2, y2 = map(float, input().split())
        print("Bod C:")
        x3, y3 = map(float, input().split())
        
        if x1 == x2 == x3 and y1 == y2 == y3:
            print("Všechny body se splývají.")
        elif are_collinear(x1, y1, x2, y2, x3, y3):
            print("Body leží na jedné přímce.")
            mid_x, mid_y = midpoint(x1, y1, x2, y2, x3, y3)
            if (x1 <= mid_x <= x3 or x3 <= mid_x <= x1) and (y1 <= mid_y <= y3 or y3 <= mid_y <= y1):
                print("Prostřední bod je bod B.")
            elif (x2 <= mid_x <= x1 or x1 <= mid_x <= x2) and (y2 <= mid_y <= y1 or y1 <= mid_y <= y2):
                print("Prostřední bod je bod A.")
            else:
                print("Prostřední bod je bod C.")
        else:
            print("Body neleží na jedné přímce.")
    except ValueError:
        print("ERROR.")

if __name__ == "__main__":
    main()
