alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
length = len(alphabet)
flag = True
while flag is True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  def caesar(text, shift, direction):
    final_list = ""
    if direction == 'encode':
      for i in text:
        if i in alphabet:
          index = alphabet.index(i)
          index += shift
          if index >= length:
            index -= length
          final_list += alphabet[index]
        else:
          final_list += i
      print(f"The encoded text is: {final_list}")
    elif direction == 'decode':
      for i in text:
        if i in alphabet:
          index = alphabet.index(i)
          index -= shift
          final_list += alphabet[index]
        else:
          final_list += i
      print(f"The decoded text is: {final_list}")
  caesar(text, shift, direction)
  play = input("Type 'yes' if u want to go again else type 'no'. ").lower()
  if play == 'no':
    flag = False
    print("See u next time. Have a good day!")