"""
backtest
----------------------------

A simple back testing module
"""

__all__ = ["drawdown",
           "returns",
           "sharpe",
           ]
__version__ = "0.0.1"
__author__ = "Wills Hua <wills.hua96@gmail.com>"


from analyzer import drawdown, returns, sharpe
