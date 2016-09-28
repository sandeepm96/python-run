from operator import itemgetter

def get_points(n):
    li = []
    for i in range(n):
        l = raw_input().split()
        k = int(l[0])
        x, y, z = float(l[1]), float(l[2]), float(l[3])
        li.append([k, x, y, z])
    return sorted(li, key = itemgetter(3), reverse=True)

ip = raw_input().split()
n, b = int(ip[0]), int(ip[1])
points = get_points(n)
print points[:b]
