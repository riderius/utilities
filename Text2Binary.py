# Фунции взяты от сюда: http://bit.ly/functions_from_text2binary

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    print(bits.zfill(8 * ((len(bits) + 7) // 8)))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0')

function = int(input('1)Текст в Двоичный код\n2)Двоичный код в текст\n'))
if function == 1:
    bits = input('Вводите текст:\n')
    text_to_bits(bits)
elif function == 2:
    bits = input('Вводите текст:\n')
    text_from_bits(bits)
else:
    print('Данной функции НЕТ')