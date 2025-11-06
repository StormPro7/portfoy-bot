class Plane:

    def __init__(self, year, color, airline="Turkish Airlines"):
        self.year = year
        self.color = color
        self.airline = airline


    def info(self):
        print("Year of plane is", self.year)
        print("Color is", self.color)
        print("Airline is", self.airline)


plane = Plane(year=2020, color="white")

plane.info()