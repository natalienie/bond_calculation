class bond_calculation:

    def __init__(self, yield_rate, coupon_rate, principle_amount, period):

        self.period = period
        self.yield_rate = yield_rate
        self.coupon_rate = coupon_rate
        self.principle_amount = principle_amount

    def get_proceed(self):

        sum1 = 0
        for i in range(1, self.period+1):
            sum1 += self.principle_amount * self.coupon_rate / (1+self.yield_rate) ** i
        sum2 = self.principle_amount / ((1 + self.yield_rate) ** self.period)

        return sum1 + sum2

    def get_bond_payable(self, n):

        if n < 1:
            return bond_calculation.get_proceed(self)
        else:
            return self.get_bond_payable(n-1) * (1+self.yield_rate) - (self.coupon_rate * self.principle_amount)

    def interests_spent_over_any_period(self, starting_n, ending_n):
        a = 0
        for i in range(starting_n, ending_n + 1):
            if i == 1:
                a += self.yield_rate * bond_calculation.get_proceed(self)
            else:
                a += self.yield_rate * bond_calculation.get_bond_payable(self, i)
        return a 
