def validator(password: str) -> bool:
    if len(password) < 8 :
        return False
    types = {
        "upper": set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        "lower": set("abcdefghijklmnopqrstuvwxyz"),
        "numbers": set("0123456789"),
        "specials": set("!@#$%^&*()-_=+[]{}|;:',.<>?/`~")
        }
  
    upper = any(char in types["upper"] for char in password)
    lower = any(char in types["lower"] for char in password)
    number = any(char in types["numbers"] for char in password)
    special = any(char in types["specials"] for char in password)

    return all([upper,lower,number,special])
