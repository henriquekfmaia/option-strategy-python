import numpy as np


class Option:
  def __init__(self, side, option_type, strike, price, points=100, ext_borders=0.05):
    self.start(side, option_type, strike, price)
    self.set_min_max(strike, strike, ext_borders)

  def start(self, side, option_type, strike, price):
    self.side = self.get_side(side)
    self.mod_side = self.get_mod(self.side)
    self.option_type = self.get_option_type(option_type)
    self.mod_option_type = self.get_mod(self.option_type)
    self.strike = strike
    self.price = price
    # self.points = points
    # self.ext_borders = ext_borders

  def set_min_max(self, minimum, maximum, ext_borders):
    delta = maximum - minimum
    if delta == 0:
      self.minimum = minimum * (1 - ext_borders)
      self.maximum = maximum * (1 + ext_borders)
    else:
      self.minimum = minimum - delta * ext_borders
      self.maximum = maximum + delta * ext_borders

  def get_side(self, side):
    if(isinstance(side, str) and side.lower() == 'buy'):
      return True
    elif(isinstance(side, str) and side.lower() == 'sell'):
      return False
    elif(isinstance(side, bool)):
      return side
    else:
      raise Exception('Invalid value for "side".')

  def get_option_type(self, option_type):
    if(isinstance(option_type, str) and option_type.lower() == 'call'):
      return True
    elif(isinstance(option_type, str) and option_type.lower() == 'put'):
      return False
    elif(isinstance(option_type, bool)):
      return option_type
    else:
      raise Exception('Invalid value for "option_type".')

  def get_mod(self, boolean):
    if boolean:
      return 1
    else:
      return -1

  def get_result_point(self, market_price):
    base_return = (market_price - self.strike) * self.mod_option_type
    base_return = (abs(base_return) + base_return)/2
    base_return += -self.price
    base_return = base_return * self.mod_side
    return base_return

  def get_result_full(self, minimum, maximum, points=100):
    market = np.linspace(minimum, maximum, points)
    result = self.get_result_point(market)
    return result

  def get_result_full_std(self):
    self.get_result_full(self.minimum, self.maximum, self.points)
