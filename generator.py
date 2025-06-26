import random
import string

def generate_password(length=12, upper=True, lower=True, digits=True, special=True):    # password generator func
    try:
        chars = ''
        if upper:
            chars += string.ascii_uppercase
        if lower:
            chars += string.ascii_lowercase
        if digits:
            chars += string.digits
        if special:
            chars += string.punctuation
            
        if not chars:
            return None
            
        password = ''.join(random.choice(chars) for _ in range(length))
        return password
    except:
        return None