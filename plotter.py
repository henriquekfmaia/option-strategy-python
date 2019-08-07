from strategy import Strategy
from matplotlib import pyplot as plt

def plot_strategy(strategy):
  x = strategy.get_market_prices_std()
  y = strategy.get_strategy_returns_std()
  plt.plot(x, y)
  plt.show()

def plot_options(strategy):
  x = strategy.get_market_prices_std()
  for opt in strategy.options:
    y = opt.get_result_full(strategy.minimum, strategy.maximum, strategy.points)
    plt.plot(x, y)
  plt.show()

strat_1 = Strategy()
strat_1.add_option('buy', 'call', 1950, 60)
strat_1.add_option('sell', 'call', 2050, 8)
plot_strategy(strat_1)
plot_options(strat_1)
