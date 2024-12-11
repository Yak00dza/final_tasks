class Car:
    def __init__(self, plate, mark, year):
        self.plate = plate
        self.mark = mark
        self.year = year

    def update(self, mark, year):
        self.mark = mark
        self.year = year

    def display(self):
        print('Registration number:', plate)
        print('Mark:', mark)
        print('Year of registration:', year)

cars = []

while True:
    inp = input().split()
    command = inp[0]
    if command == 'add':
        if len(inp) != 4:
            print('Invalid args')
        plate, mark, year = inp[1], inp[2], inp[3]
        for car in cars:
            if car.plate == plate:
                car.update(mark, year)
                break
        else:
            cars.append(Car(plate, mark, year))
    elif command == 'view':
        if len(inp) != 2:
            print('Invalid args')
        plate = inp[1]
        for car in cars:
            if car.plate == plate:
                car.display()
                break
        else:
            print('The car with this registration number was not found!')
