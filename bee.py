class Bee:
    def __init__(self, wings = 2, color = None):
        self.wings = {"wings":wings}
        if not color:
            self.color = {"black", "yellow"}
        else:
            self.color = color