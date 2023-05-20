class Auto:
    color = ""
    weight = 0
    def __init__(self, brand: str, age: int, mark: str) -> None:
        self.brand = brand
        self.age = age
        self.mark = mark
    def drive(self):
        print("Car", self.brand, self.mark,"drives")
    def stop(self):
        print("Car", self.brand, self.mark,"stops")
    def use(self):
        self.age += 1
    def current_age(self):
        return(self.age)
     
def main():
    auto_1 = Auto("MAZ", 5, "MAZ 1234")
    auto_2 = Auto("KOMAZ", 15, "KOMAZ 5678")
    auto_1.drive()
    auto_2.stop()
    print(auto_1.current_age())
    auto_1.use()
    print(auto_1.current_age())

main()
