
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        lista = test.strip().split(' ')
        morse_dicc = {'---': 'O', '--.': 'G', '-...': 'B', '-..-': 'X',
        '.-.': 'R', '--.-': 'Q', '--..': 'Z', '.--': 'W', '..---': '2',
        '.-': 'A', '..': 'I', '-.-.': 'C', '..-.': 'F', '-.--': 'Y',
        '-': 'T', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U',
        '.----': '1', '-----': '0', '-.-': 'K', '-..': 'D', '----.': '9',
        '-....': '6', '.---': 'J', '.--.': 'P', '....-': '4', '--': 'M',
        '-.': 'N', '....': 'H', '---..': '8', '...-': 'V', '--...': '7', 
        '.....': '5', '...--': '3', '': ' '}
        converted ="" 
        for item in lista:
            converted += morse_dicc[item]
        print (converted)