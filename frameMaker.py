class frame:
    def __init__(self, data):
        self.binary = data
        self.array = []
        counter = 0
        for i in self.binary:
            mask = 0b10000000
            while mask>0:
                if i & mask == mask:
                    self.array.append(counter)
                counter = counter + 1
                mask = mask >> 1

        print(self.array)

value = (
        0b01100110,
        0b00011000,
        0b01000010,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b11111111,)

picture = frame(value)

