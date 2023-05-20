class Counter:
    def __init__(self, start = 0, stop = "inf") -> None:
        self.value = start
        self.inf = True
        if stop != "inf":
            self.max = stop
            self.inf = False
    def get(self):
        return self.value
    def increment(self):
        if(self.inf == True):
            self.value += 1
        elif(self.value < self.max):
            self.value += 1
        else:
            print("Maximal value is reached.")

def main():
    a =  Counter(start=42)
    a.increment()
    print(a.get())
    b = Counter()
    b.increment()
    print(b.get())
    b.increment()
    print(b.get())
    c = Counter(start=42, stop=43)
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())

main()
