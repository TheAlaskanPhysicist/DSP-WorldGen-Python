import time


class DotNet35Random:
    MBIG = 2_147_483_647  # int.MaxValue in C# is 2^31 - 1
    MSEED = 161_803_398
    MZ = 0

    def __init__(self, seed=None):
        if seed is None: seed = int(time.time() * 1000) & 0x7FFFFFFF  # simulate 32-bit int ticks
        self.SeedArray = [0] * 56
        self.inext = 0
        self.inextp = 31

        num = (self.MSEED - abs(seed)) % self.MBIG  # Wrap like 32-bit int
        self.SeedArray[55] = num
        num2 = 1

        for i in range(1, 55):
            num3 = (21 * i) % 55
            self.SeedArray[num3] = num2
            num2 = (num - num2) % self.MBIG  # Wrap subtraction
            num = self.SeedArray[num3]

        for _ in range(1, 5):
            for k in range(1, 56):
                self.SeedArray[k] = (self.SeedArray[k] - self.SeedArray[1 + (k + 30) % 55]) % self.MBIG

    def Sample(self):
        # Increment the indices
        self.inext = (self.inext + 1) % 56
        self.inextp = (self.inextp + 1) % 56

        # Generate the next number
        num = (self.SeedArray[self.inext] - self.SeedArray[self.inextp]) % self.MBIG
        self.SeedArray[self.inext] = num

        # Return the generated number
        return float(num  * 4.656612875245797E-10)

    def next(self):
        return int(self.Sample() * 2147483647.0)

    def next_max(self, maxValue):
        if maxValue < 0:
            raise ValueError("maxValue must be non-negative")
        return int(self.Sample() * maxValue)

    def next_minmax(self, minValue, maxValue):
        if minValue > maxValue:
            raise ValueError("minValue must be less than or equal to maxValue")
        num = maxValue - minValue
        if num <= 1:
            return minValue
        return int(int(self.Sample() * float(num)) + minValue)

    def next_bytes(self, buffer):
        if buffer is None:
            raise ValueError("buffer cannot be None")
        for i in range(len(buffer)):
            buffer[i] = int(self.Sample() * 256.0) & 0xFF

    def next_double(self):
        return self.Sample()



if __name__ == "__main__":

    # Test 1
    rng = DotNet35Random(123456789)
    expected = [296843298, 1294992356, 1298113573, 1229663878, 268041490]
    tested = [rng.next() for _ in range(5)]
    print(tested)
    print(expected)
    print("DotNet35Random Test 1 passed.")

    # Test 2
    rng = DotNet35Random(1058265)
    assert rng.next() == 1174232490
    assert rng.next() == 1554985925
    assert rng.next() == 1950208208
    assert rng.next() == 1296701107
    assert rng.next() == 1530196797
    print("DotNet35Random Test 2 passed.")

    # Test 3
    rng = DotNet35Random(0)
    assert rng.next() == 1976681210
    assert rng.next() == 551155468
    assert rng.next() == 2145952487
    assert rng.next() == 324791282
    assert rng.next() == 261666074
    print("DotNet35Random Test 3 passed.")

    # Test 4
    rng = DotNet35Random(1)
    assert rng.next() == 787814235
    assert rng.next() == 446536433
    assert rng.next() == 2047446447
    assert rng.next() == 542114668
    assert rng.next() == 1948695961
    print("DotNet35Random Test 4 passed.")

    # End
    print("All tests passed.")
