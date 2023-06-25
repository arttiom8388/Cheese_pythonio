class Bludo:
    def __init__(self, amount: int, name: str, value: float, weight: float) -> None:
        self.amount = amount
        self.name = name
        self.value = value
        self.weight = weight


class Order:
    def __init__(self) -> None:
        self.bluda = []
        self.current_money = 0

    def add_bludo(self, bludo: Bludo):
        self.bluda.append(bludo)

    def total_amount(self):
        return len(self.bluda)
    
    def total_cost(self):
        return sum(bludo.value for bludo in self.bluda)
    
    def total_weight(self):
        return sum(bludo.weight for bludo in self.bluda)
    
    def pay(self, amm: int):
        self.current_money += amm

    def need_to_pay(self):
        return sum(bludo.value for bludo in self.bluda) - self.current_money


def main():
    bludo_1 = Bludo(1, "kartoshka", 3, 200)
    bludo_2 = Bludo(1, "kotleta", 5, 100)
    bludo_3 = Bludo(1, "chai", 2, 300)
    order = Order()
    print("amount:", order.total_amount())
    order.add_bludo(bludo_1)
    order.add_bludo(bludo_3)
    order.add_bludo(bludo_2)
    print("amount:", order.total_amount())
    print("total cost:", order.total_cost())
    print("weight:", order.total_weight())
    print("need to pay:", order.need_to_pay())
    order.pay(4)
    print("need to pay:", order.need_to_pay())
    order.pay(6)
    print("need to pay:", order.need_to_pay())

main()