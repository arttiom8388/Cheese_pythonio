class Queue():
    queue = [1, ]
    queue.pop()

    def add(self, *input_list):
        for i in range(len(input_list)):

            if type(input_list[i]) == type(1):
                if (input_list[i] % 8) != 0:
                    print("InvalidIntDivision   ", input_list[i])
                elif (input_list[i] > 9999) or (input_list[i] < -9999):
                    print("InvalidIntNumberCount   ", input_list[i])
                else:
                    self.queue.append(input_list[i])

            elif type(input_list[i]) == type(1.1):
                if abs(str(input_list[i]).find('.') - len(str(input_list[i]))) > 3:
                    print("InvalidFloat   ", input_list[i])
                else:
                    self.queue.append(input_list[i])

            elif type(input_list[i]) == type("1"):
                if len(input_list[i]) > 4:
                    print("InvalidTextLength   ", input_list[i])
                elif (input_list[i].find(input_list[i][1]) != 1) or (input_list[i].find(input_list[i][2]) != 2) or (input_list[i].find(input_list[i][3]) != 3):
                    print("DuplicatesInText   ", input_list[i])
                else:
                    self.queue.append(input_list[i])

            else:
                print(input_list[i], "# not int, float, str")


def main():
    q = Queue()
    q.add(1, 16, 280, 80000, 2.51, 1.875, "text", "data", "world")
    print(q.queue)

main()
