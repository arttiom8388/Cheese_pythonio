class Cipher:
    def __init__(self) -> None:
        self.crypto_str_1 = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
        self.crypto_str_2 = "C R Y P T O A B D E F G H I J K L M N Q S U V W X Z"
        self.crypto_arr_1 = self.crypto_str_1.split(" ") + self.crypto_str_1.lower().split(" ")
        self.crypto_arr_2 = self.crypto_str_2.split(" ") + self.crypto_str_2.lower().split(" ")
        if len(self.crypto_arr_1) != len(self.crypto_arr_2):
            print("cryptomap error")
            return
        self.encoding_lib = {}
        self.decoding_lib = {}
        for i in range(len(self.crypto_arr_1)):
            self.encoding_lib[self.crypto_arr_1[i]] = self.crypto_arr_2[i]
            self.decoding_lib[self.crypto_arr_2[i]] = self.crypto_arr_1[i]
    def encode(self, input_str: str) -> str:
        rez = ""
        for x in input_str:
            rez += str(self.encoding_lib.get(x, x))
        return rez
    def decode(self, input_str: str) -> str:
        rez = ""
        for x in input_str:
            rez += str(self.decoding_lib.get(x, x))
        return rez

def main():
    cipher = Cipher()
    print(cipher.encode("Hello, world"))
    print(cipher.decode("Fjedhc dn atidsn"))
    print()
    text = "Time is the continued sequence of existence and events that occurs in an apparently irreversible succession from the past, through the present, into the future. It is a component quantity of various measurements used to sequence events, to compare the duration of events or the intervals between them, and to quantify rates of change of quantities in material reality or in the conscious experience. Time is often referred to as a fourth dimension, along with three spatial dimensions.       special symbols: 123{[/*!?;..."
    text = cipher.decode(text)
    print(text)
    print()
    text = cipher.encode(text)
    print(text)
main()
