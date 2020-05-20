# https://leetcode.com/problems/online-stock-span/

from typing import List, Tuple

class Stock:
    def __init__(self, price: int, span: int):
        self.price = price
        self.span = span

# Time: O(Q) - where Q is the number of calls to StockSpanner.next.
#              There are Q pushes to the stack and, at most, Q pops
# Space: O(Q)
class StockSpanner:

    def __init__(self):
        self.stack: List[Stock] = []
        

    def next(self, price: int) -> int:
        cur_span = 0
        while self.stack and self.stack[-1].price <= price:
            stock = self.stack.pop()
            cur_span += stock.span
        final_span = cur_span + 1
        self.stack.append(Stock(price, final_span))
        return final_span

# Time: O(Q)
# Space: O(Q)
class StockSpanner2:
    def __init__(self):
        self.stack: List[Tuple] = []
    
    def next(self, price: int) -> int:
        cur_span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, span = self.stack.pop()
            cur_span += span
        self.stack.append((price, cur_span))
        return cur_span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

if __name__ == '__main__':
    obj = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    expected = [1, 1, 1, 2, 1, 4, 6]
    for i, p in enumerate(prices):
        assert(obj.next(p) == expected[i])