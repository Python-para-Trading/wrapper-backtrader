
import backtrader as bt

from strategy import Strategy

class Cross(Strategy):
    params = (
        ('slow', 11),
        ('fast', 33),
    )

    def __init__(self):
        super(Cross, self).__init__()

        self.slow =  bt.indicators.SimpleMovingAverage(self.datas[0],
                                                       period=self.params.slow)

        self.fast =  bt.indicators.SimpleMovingAverage(self.datas[0],
                                                       period=self.params.fast)

    def next(self):
        if self.slow > self.fast and not self.position:
            self.buy()
        elif self.slow < self.fast and self.position:
            self.sell()
