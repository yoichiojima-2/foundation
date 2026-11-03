class Solution:
    def best_time_to_buy_and_sell_stock(self, prices):
        best = 0
        min_price = float("inf")
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > best:
                best = p - min_price
        return best
