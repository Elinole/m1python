class Point:
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z

    def ToString(self):
        x = self.x
        y = self.y
        z = self.z
        if (z == None):
            print("%.2f" % x,
                ",",
                "%.2f" % y
            )
        else:
            print("%.2f" % x,
                ",",
                "%.2f" % y,
                ",",
                "%.2f" % z
            )

P1 = Point(1, -5, 6)
P1.ToString()