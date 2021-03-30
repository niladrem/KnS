class Twins:
    def __init__(self, p1=None, p2=None):
        self.p1 = p1
        self.p2 = p2

    def is_valid(self):
        return self.p1 is not None and self.p2 is not None

    def print_twins(self):
        print("Twins: %s, %s" % (str(self.p1), str(self.p2)))
