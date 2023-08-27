import time

print("CODIFICADOR MORSE EM PYTHON")
print("*"*27)


dict_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

try:
    mensagem = str(input("Texto para ser codificado em morse:").upper())
    mensagem = " ".join(dict_morse[c] for c in mensagem.upper())
    print(mensagem)


    time.sleep(0.5)

    print('Tradução completa!')
    
except KeyError as e:
    char_error = str(e).replace("\'", '')
    print('{} = Caractere não reconhecido'.format(char_error))
    print('Tente novamente!')
except KeyboardInterrupt:
    
    print('')