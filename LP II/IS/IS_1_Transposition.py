# # Transposition Cipher
# # !pip install pyperclip

# import math

# plainttext = input("Enter your plain text: ")
# key = int(input("Enter key: "))
# ciphertext = [''] * key


# for column in range(key):
#     pointer = column;
#     while pointer < len(plainttext):
#         ciphertext[column] += plainttext[pointer]
#         pointer+=key

# print(''.join(ciphertext))


# def decryptMessage(key, message):
#     numOfColumns = int(math.ceil(len(message) / key))
#     numOfRows = key
#     numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

#     text = [''] * numOfColumns
#     column = 0
#     row = 0

#     for symbol in message:
#         text[column] += symbol
#         column += 1
#         if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
#             column = 0
#             row += 1

#     return ''.join(text)


# myMessage = input("Enter cipher text: ")
# myKey = int(input("Enter key: "))
# text = decryptMessage(myKey, myMessage)
# print(text)
# # pyperclip.copy(text)




def encryptMessage(key, message):
   ciphertext = [''] * key
   
   for col in range(key):
      position = col
      while position < len(message):
        ciphertext[col] += message[position]
        position += key
      return ''.join(ciphertext)



myMessage = 'Hello World'

myKey = 4
ciphertext = encryptMessage(myKey, myMessage)

print("Cipher Text is")
print(ciphertext + '|')
# pyperclip.copy(ciphertext)