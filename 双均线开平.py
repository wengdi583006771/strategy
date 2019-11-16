from tqsdk import TqApi, TqSim,TqBacktest, BacktestFinished
from tqsdk.ta import MA
import time
from datetime import date



def 判断是否符合开仓(klines):
    二十日均线=MA(klines,20)
    四十日均线=MA(klines,40)
    if (二十日均线.iloc[-1].ma>四十日均线.iloc[-1].ma)and(二十日均线.iloc[-2].ma<四十日均线.iloc[-1].ma):
        return 1
    else:
        return 0
def 判断是否符合平仓(klines):
    二十日均线=MA(klines,20)
    四十日均线=MA(klines,40)
    if (二十日均线.iloc[-1].ma<四十日均线.iloc[-1].ma)and(二十日均线.iloc[-2].ma>四十日均线.iloc[-1].ma):
        return 1
    else:
        return 0
acc = TqSim()
try:
    api=TqApi(acc, backtest=TqBacktest(start_dt=date(2019, 10, 5), end_dt=date(2019, 11, 15)))
    klines = api.get_kline_serial("SHFE.rb2001", 300,1000)
    while True:
        api.wait_update()
        klines = api.get_kline_serial("SHFE.rb2001", 300,1000)
        if 判断是否符合开仓(klines):
            当前多仓=api.get_position("SHFE.rb2001")
            当前委托=api.get_order()
            if 当前多仓['pos_long_his']==0 and 当前委托=={}:
                order = api.insert_order(symbol="SHFE.rb2001", direction="BUY", offset="OPEN",volume=1000)
                print('.......我开仓了.....')
                q=api.get_quote("SHFE.rb2001")
                print(q["datetime"])
        if 判断是否符合平仓(klines):
            当前多仓=api.get_position("SHFE.rb2001")
            if 当前多仓['pos_long_his']!=0:
                order = api.insert_order(symbol="SHFE.rb2001", direction="SELL", offset="CLOSE",volume=1000)
                print('.......我平仓了.....')
                q=api.get_quote("SHFE.rb2001")
                print(q["datetime"])
except BacktestFinished as e:
  # 回测结束时会执行这里的代码
  pass
api.close()

