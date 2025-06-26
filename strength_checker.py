import re

def check_strength(password):                                                           # strength checker func
    try:
        if not password:
            return "Very Weak"
            
        length = len(password)
        score = 0
        
        # Length check
        if length >= 12:
            score += 2
        elif length >= 8:
            score += 1
            
        # Character diversity
        if re.search(r'[A-Z]', password):
            score += 1
        if re.search(r'[a-z]', password):
            score += 1
        if re.search(r'[0-9]', password):
            score += 1
        if re.search(r'[^A-Za-z0-9]', password):
            score += 1
            
        # Determine strength
        if score >= 6:
            return "Very Strong"
        elif score >= 4:
            return "Strong"
        elif score >= 3:
            return "Moderate"
        else:
            return "Weak"
    except:
        return "Unknown"