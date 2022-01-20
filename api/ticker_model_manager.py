from enum import Enum, auto, unique
class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

@unique
class Ticker(AutoName):
    AAPL = auto()
    TSLA = auto()
    VIX = "^VIX" #auto()
    GME = auto()
    SP500 = "^GSPC" #auto()





if __name__ == '__main__':   
    for tick in Ticker:
        print(tick == Ticker.AAPL)

    data = {Ticker.AAPL: "bæsjedata"} 
    print(data)

