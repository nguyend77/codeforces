def distance(point1, point2):
    return ((point1[0]-point2[0]) ** 2 + (point1[1]-point2[1]) ** 2) ** 0.5
def midpoint(point1, point2):
    return ((point1[0]+point2[0])/2,(point1[1]+point2[1])/2)

class Problem:
    points = [] # [A, B, C]
    sides = [] # [BC, AC, AB]
    def __init__(self, a, b, c):
        self.points.append(a)
        self.points.append(b)
        self.points.append(c)
        self.sides.append(distance(b,c))
        self.sides.append(distance(a,c))
        self.sides.append(distance(a,b))
    def solve(self):
        solution = (0,0)
        if self.sides[0]==self.sides[1]: # equilateral triangle
            solution = midpoint(self.points[0],self.points[1])
        elif self.sides[0]==self.sides[2]: # equilateral triangle
            solution = midpoint(self.points[0],self.points[2])
        elif self.sides[1]==self.sides[2]: # equilateral triangle
            solution = midpoint(self.points[1],self.points[2])
        else:
            max_length = max(self.sides)
            max_index = self.sides.index(max_length)
            vector = [0, 0]
            for i in range(3):
                if i != max_index:
                    vector[0] += self.points[i][0]
                    vector[1] += self.points[i][1]
                solution = (vector[0]-self.points[max_index][0],vector[1]-self.points[max_index][1])
        print(f'{solution[0]} {solution[1]}')

stadium1 = [int(x) for x in input().split()]
A = (stadium1[0], stadium1[1])
stadium2 = [int(x) for x in input().split()]
B = (stadium2[0], stadium2[1])
stadium3 = [int(x) for x in input().split()]
C = (stadium3[0], stadium3[1])
X = Problem(A,B,C)
X.solve()
