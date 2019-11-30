from tqsdk import TqApi, TqSim,TqBacktest, BacktestFinished
from tqsdk.ta import MA
import time
from datetime import date

acc = TqSim()
品种="SHFE,rb2001"
一跳价格=1
一次下多少单子=1
当前状态='寻找开仓机会'
检测最近多少tick序列=10
波动开仓跳数=15
委托远离几条撤单=10
委托间隔多少秒撤单=120



保本损改变条件=20
止损=10
止盈=30



单跟1分钟超过多少平仓=20

止损临时=0
委托单子=0


def 开仓判断(行情,tick序列):
    global 委托单子,当前状态
    if 当前状态=='寻找开仓机会':
        mymax=max(tick序列['last_price'])
        mymin=min(tick序列['last_price'])
        if mymax-mymin>波动开仓跳数*一跳价格:
            当前状态='检测委托'
            if tick序列['last_price'][::-1].idxmax()>tick序列['last_price'][::-1].idxmain():
               委托单子=api.insert_order(symbol="DCE.m2005", direction="BUY", offset="OPEN", volume=5, limit_price=tick数据['bid_pricel'.tolist()[-1])
            else:
               委托单子=api.insert_order(symbol="DCE.m2005",direction="BUY", offset="OPEN", volume=5, limit_price=tick数据['bid_pricel'.tolist()[-1])
    

 
def 检测委托 (行情,tick序列):
    global 委托单子,当前状态
    if 当前状态=='检测委托':
        a=api.get_order(委托单子)
        委托价格1=a['limit_price']
        未成交手数1=a['volume_left']
        开单方向1=a['direction']
        当前价格=ick数据['bid_pricel'.tolist()[-1]
        if 未成交手数1 ==0：
            当前状态==''
            return 
        if 开单方向1=='BUY':


       
try:
    api=TqApi(acc, backtest=TqBacktest(start_dt=date(2019, 11, 1), end_dt=date(2019, 11, 8)))
    行情= api.get_kline_serial("SHFE.rb2001", 300,1000)
    tick序列=api.get_tick_serial( , )
    while True:
        api.wait_update()
        开仓判断(行情,tick序列)
        检测委托(行情,tick序列)
        平仓检测(行情,tick序列)


except BacktestFinished as e:
  # 回测结束时会执行这里的代码
  print(acc.trade_log)
  pass












# 开仓
# 10个tick波动限价单子


# 委托检测
# 远离挂单10跳
# 2分钟撤单
# 成交






# 持仓检测
# 20跳，改变止损



# 止盈止损
# 按照止盈平单
# 按照止损平单



# 波动平单
# 20跳平单