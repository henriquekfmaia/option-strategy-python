import numpy as np
from option import Option

class Strategy:
  def __init__(self, points = 100, ext_borders=0.05):
    self.options = []
    self.minimum = 0
    self.maximum = 0
    self.points = points
    self.ext_borders = ext_borders

  def add_option(self, side, option_type, strike, price):
    option = Option(side, option_type, strike, price)
    self.options.append(option)
    self.set_min_max(option.minimum, option.maximum)

  def set_min_max(self, new_minimum, new_maximum):
    if self.minimum == 0:
      self.minimum = new_minimum
    minimum = min(self.minimum, new_minimum)
    maximum = max(self.maximum, new_maximum)
    if minimum != self.minimum or maximum != self.maximum:
      self.minimum = minimum
      self.maximum = maximum
      for opt in self.options:
        opt.set_min_max(self.minimum, self.maximum, self.ext_borders)

  def get_strategy_returns(self, minimum, maximum, points):
    strategy_returns = np.zeros(points)
    for opt in self.options:
      strategy_returns = strategy_returns + opt.get_result_full(minimum, maximum, points)
    return strategy_returns

  def get_strategy_returns_std(self):
    return self.get_strategy_returns(self.minimum, self.maximum, self.points)
  
  def get_market_prices_std(self):
    return np.linspace(self.minimum, self.maximum, self.points)
