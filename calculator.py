class Calculator(object):
    def __init__(self):
        pass
    
    def add(self, string):
        if string.startswith('//'):
            delimiter_spec, string = string.split('\n', 1)
            delimiter = delimiter_spec[2:]
            string = string.replace(delimiter, ',')
        string = string.replace('\n', ',')
        if string:
            numbers = map(int,string.split(','))
            if any(number<0 for number in numbers):
                raise ValueError
            return sum(numbers)
        else:
            return 0
