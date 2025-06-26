from datetime import datetime

def save_password(password):                                                            # file handler func
    try:
        with open("passwords.txt", "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}: {password}\n")
        return True
    except:
        return False