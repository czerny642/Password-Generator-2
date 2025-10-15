import secrets
import string

def generate_password(length=12, symbol=True, uppercase=True):
    # Kombinasi karakter yang digunakan untuk membuat password
    combination = string.ascii_lowercase + string.digits
    if uppercase:
        combination += string.ascii_uppercase
    if symbol:
        combination += string.punctuation

    new_password = ''
    for _ in range(length):
        new_password += secrets.choice(combination)
    return new_password

def contains_upper(s):
    # Mengecek apakah string mengandung huruf besar
    return any(c.isupper() for c in s)

def contains_symbols(s):
    # Mengecek apakah string mengandung simbol (punctuation)
    return any(c in string.punctuation for c in s)

if __name__ == '__main__':
    # Generate 5 random passwords dengan kriteria tertentu
    for i in range(1, 6):
        new_pass = generate_password(length=15, symbol=True, uppercase=True)
        specs = f'U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}'
        print(f'{i} -> {new_pass} ({specs})')

"""       
Output: 
1 -> J#V\=41%dO}F0%i (U: True, S: True)
2 -> iKvPV8B*FDGQZI. (U: True, S: True)
3 -> 6[YUUxXB_m0D[c: (U: True, S: True)
4 -> &/EZ'Hfb]~P^Y[4 (U: True, S: True)
5 -> -la{]f;(~&=zkyY (U: True, S: True)

"""

