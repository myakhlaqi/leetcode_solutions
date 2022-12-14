#
# @lc app=leetcode id=359 lang=python3
#
# [359] Logger Rate Limiter
#

# @lc code=start
class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.cache and timestamp - self.cache[message] < 10:
            return False

        self.cache[message]=timestamp
        return True
# @lc code=end
logger = Logger()

# // logging string "foo" at timestamp 1
print(logger.shouldPrintMessage(1, "foo"))#; returns true; 

# // logging string "bar" at timestamp 2
print(logger.shouldPrintMessage(2,"bar"))#; returns true;

# // logging string "foo" at timestamp 3
print(logger.shouldPrintMessage(3,"foo"))#; returns false;

# // logging string "bar" at timestamp 8
print(logger.shouldPrintMessage(8,"bar"))#; returns false;

# // logging string "foo" at timestamp 10
print(logger.shouldPrintMessage(10,"foo"))

# // logging string "foo" at timestamp 11
print(logger.shouldPrintMessage(11,"foo"))#; returns true;

print(logger.shouldPrintMessage(15,"bar"))#; returns false;
