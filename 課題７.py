import re
c = 'hogehoge'
print(''.join(re.split('a|e|i|o|u|A|E|I|O|U', c)))