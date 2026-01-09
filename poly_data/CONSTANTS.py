# Minimum position size to trigger position merging
# Positions smaller than this will be ignored to save on gas costs
MIN_MERGE_SIZE = 20

# Maximum absolute position size cap
# This limits the maximum position size regardless of max_size configuration
MAX_POSITION_SIZE = 500

# Liquidity threshold for ask price adjustment
# If ask liquidity is below this threshold, use best_ask instead of best_ask - tick_size
# This prevents placing orders when there's insufficient liquidity
LIQUIDITY_THRESHOLD = 500