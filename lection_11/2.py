class Temperature:
    def __init__(self, celsius = -273.15, kelvins = 0.0, fahrenheit = -459.67) -> None:
        temp = kelvins + (celsius + (fahrenheit - 32) * 5/9 ) + 273.15 * 2
        if temp < -0.1:
            print("Non valid temperature")
            return()
        self.kelvins_temp = temp

    def change(self, celsius = 0, kelvins = 0, fahrenheit = 0):
        temp = self.kelvins_temp
        temp += celsius + kelvins + fahrenheit * 5/9
        if temp < -0.1:
            print("Non valid temperature change")
            return()
        self.kelvins_temp = temp

    def get_celsius(self):
        return (self.kelvins_temp - 273.15)
    
    def get_kelvins(self):
        return self.kelvins_temp
    
    def get_fahrenheit(self):
        return ((self.kelvins_temp - 273.15) * 9/5 + 32)
    


def main():
    rand_temp = Temperature(celsius = 0)
    print(rand_temp.get_celsius(), rand_temp.get_kelvins(), rand_temp.get_fahrenheit())
    rand_temp.change(fahrenheit= -77)
    print(rand_temp.get_celsius(), rand_temp.get_kelvins(), rand_temp.get_fahrenheit())
    rand_temp.change(kelvins= -230)
    print(rand_temp.get_celsius(), rand_temp.get_kelvins(), rand_temp.get_fahrenheit())
    rand_temp.change(kelvins= -1)
    print(rand_temp.get_celsius(), rand_temp.get_kelvins(), rand_temp.get_fahrenheit())


main()
