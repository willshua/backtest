"""
backtest
---------------------------------

一个不知道会是啥样的量化回测工具, 
还没想好取啥名, 更没想好怎么写.
"""

__all__ = [
    "drawdown",
    "returns",
    "sharpe",
    "trade",
]
__version__ = "0.0.0"
__author__ = "Wills Hua <wills.hua96@gmail.com>"


from analyzer import drawdown, returns, sharpe, trade
