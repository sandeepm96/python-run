from scipy.spatial import ConvexHull

def get_points(n):
    p = []
    for i in range(n):
        cord = raw_input().split()
        cord = [int(x) for x in cord]
        p.append(cord)
    return p

def print_vertices(p, v):
    print len(v)
    for x in v:
        print p[x]

n = input()
p = get_points(n)
hull = ConvexHull(p)
print_vertices(p, hull.vertices)
