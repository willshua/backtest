"""
backtest
----------------------------

A simple back testing module
"""

__all__ = [
    "returns", 
    "sharpe", 
    "drawdown",
]
__version__ = "0.0.1"
__author__ = "Wills Hua"


from analyzer import returns, sharperatio, drawdown
