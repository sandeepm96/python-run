from operator import itemgetter

def get_points(n):
    li = []
    for i in range(n):
        l = raw_input().split()
        k = int(l[0])
        x, y, z = float(l[1]), float(l[2]), float(l[3])
        li.append([k, x, y, z])
    return sorted(li, key = itemgetter(3), reverse=True)

def perform_op(points, b):
    while True:
        inp = raw_input()
        if inp == "":
            break
        q = inp.split()
        c = q[0]
        k = int(q[1])
        if (c == 'f' or c == 'F'):
            for sublist in points[:b]:
                if sublist[0] == k:
                    print "%s = (%0.3f,%0.3f,%0.3f)" % (k, sublist[1], sublist[2], sublist[3])
                    break
            else:
                print "Point doesn't exist in the bucket."
        elif (c == 'r' or c == 'R'):
            for sublist in points[:b]:
                if sublist[0] == k:
                    if len(points) > b:
                        points.remove(sublist)
                        print "Point id %s removed." % k
                        break
                    else:
                        print "No more points can be deleted."
                        break
            else:
                print "Point doesn't exist in the bucket."
        else:
            print "Wrong input."

ip = raw_input().split()
n, b = int(ip[0]), int(ip[1])
points = get_points(n)
perform_op(points, b)
