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

def render(pixels,array,r,g,b):
    pixels.fill((0,0,0))
    for i in array.array:
        pixels[i] = (r,g,b)
    pixels.show()

