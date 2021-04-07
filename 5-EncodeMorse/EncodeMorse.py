def encode_morse(message):
  char_to_dots = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
  }
  string = ""

  for char in message:
    if char.isalpha(): char = char.upper()
    if char in char_to_dots:
      string += char_to_dots[char] + " "
    else:
      string += char

  if string[-1] == " ":
    string = string[:-1]

  return string

  
  # string = ""
  # msg = message.upper()
  # for txt in message:
  #   for key,value in char_to_dots.items():
  #     if(text == key):
  #             string += (value+" ")
  # print("string : ",string)
  # return string