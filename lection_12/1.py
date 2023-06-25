def calc(func):
    func = func.split(" ")
    if func[0] == "":
        func.pop(0)
    if len(func) == 4:
        if func[3] == "":
            func.pop(3)
    if len(func) != 3:
        return "InputFormulaError" 
    if not (func[0].isnumeric() & func[2].isnumeric()):
        return "InputNumberError"
    if not (func[1] == "+" or func[1] == "-" or func[1] == "*" or func[1] == "/"):
        return "InputOperatorError"
    if func[1] == "+":
        return float(func[0]) + float(func[2])
    elif func[1] == "-":
        return float(func[0]) - float(func[2])
    elif func[1] == "*":
        return float(func[0]) * float(func[2])
    else:
        return float(func[0]) / float(func[2])
        
def main():
    while 1:
        func = input('input function or "quit":')
        if func == "quit":
            break
        print(calc(func))

main()