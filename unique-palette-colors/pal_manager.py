import os

class PalManager:
    def __init__(self, size):
        self.size = size
        self.red = []
        self.green = []
        self.blue = []
        self.duplicate_red = []
        self.duplicate_green = []
        self.duplicate_blue = []
        
    def add_value(self, value):
        value = value.strip()
        [r, g, b] = value.split(' ')
        
        if(r in self.red):
            self.duplicate_red.append(r)

        if(g in self.green):
            self.duplicate_green.append(g)
        
        if(b in self.blue):
            self.duplicate_blue.append(b)

        self.red.append(r)
        self.green.append(g)
        self.blue.append(b)

    def print(self):

        def __remove_duplicates(the_list):
            newList = list(dict.fromkeys(the_list))
            return newList

        bgColors = {
            'red': '\33[41m',
            'green': '\33[42m',
            'blue': '\33[44m',
            'end': '\033[0m',
        }

        os.system('color')

        colors = ['red', 'green', 'blue']
        duplicate_string ='Number of duplicats for color {}:{} duplicate values:{}'
        no_duplicate_string = 'No duplicates for {}'
        print('Number of colors in palette:{}'.format(self.size))
        
        for color in colors:
            duplicate = getattr(self, 'duplicate_' + color)
            if(len(duplicate)> 0):
                print(bgColors[color] + duplicate_string.format(color.upper(), len(duplicate), __remove_duplicates(duplicate)) + bgColors['end'])
            else:
                print(bgColors[color] + no_duplicate_string.format(color.upper()) + bgColors['end'])

    