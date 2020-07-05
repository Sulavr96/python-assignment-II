class Mario:
    def __init__(self, hair_color, hat_color, shirt_color, pant_color, mustache_color,
                 mustache_size):
        self.hair_color = hair_color
        self.hat_color = hat_color
        self.shirt_color = shirt_color
        self.pant_color = pant_color
        self.mustache_color = mustache_color
        self.mustache_size = mustache_size

    def get_character(self):
        return {
                "Hair color": self.hair_color,
                "Colour of Hat": self.hat_color,
                "Shirt Color": self.shirt_color,
                "Pant Color": self.pant_color,
                "Mustache Color": self.mustache_color,
                "Mustache size": self.mustache_size
                }


mario = Mario('Brown', 'Red', 'Red', 'Blue', 'Black', 'Long')

print(mario.get_character())
