class Calculator(object):
    def __init__(self):
        pass
    
    def add(self, string):
        string = self._normalize_delimiters(string)
        if string:
            return self._add_number_in_string(string)
        else:
            return 0

    def _validate_numbers(self, numbers):
        if any(number<0 for number in numbers):
            raise ValueError
            
    def _normalize_delimiters(self, string):
        if string.startswith('//'):
            string = self._normalize_special_delimiters(string)
        string = string.replace('\n', ',')
        return string
        
    def _normalize_special_delimiters(self, string):
        delimiter_spec, string = string.split('\n', 1)
        delimiter = delimiter_spec[2:]
        string = string.replace(delimiter, ',')
        return string
        
    def _add_number_in_string(self, string):
        numbers = map(int,string.split(','))
        self._validate_numbers(numbers)
        return sum(numbers)
