from re import match

GRUB_FILE_PATH = '/etc/default/grub'

class GrubFile:
  def __init__(self):
    file = open(GRUB_FILE_PATH, 'r')
    self._source = file.read()
    file.close()

    self._props = {}
    self._pos = 0

    self._parse()

  def _next_char(self):
    char = self._source[self._pos]
    self._pos += 1
    return char
  
  def _is_not_eoi(self):
    return self._pos != len(self._source)

  def _parse(self):
    while self._is_not_eoi():
      char = self._next_char()
      
      if char == '#':
        self._parse_comment()
      elif char.isalpha():
        self._parse_key_value()
  
  def _parse_comment(self):
    while self._is_not_eoi():
      char = self._next_char()
      if char == '\n':
        break
  
  def _parse_key_value(self, ):
    key = self._source[self._pos - 1]
    while self._is_not_eoi():
      char = self._next_char()
      if char.isalpha() or char == '_':
        key += char
      elif char == '=':
        break
    
    value = ''
    while self._is_not_eoi():
      char = self._next_char()
      if char == '\n':
        break
      else:
        value += char

    self._props[key] = value.strip('"')

  def __getitem__(self, key):
    return self._props[key]
  
  def __setitem__(self, key, value):
    self._props[key] = value
  
  def write(self):
    content = ''
    for key in self._props.keys():
      value = self._props[key]
      content += f'{key}={value if match('[0-9]+', value) else f'"{value}"'}\n'

    file = open(GRUB_FILE_PATH, 'w')
    file.write(content)
    file.close()
