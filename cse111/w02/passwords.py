# Added a password strength visualization that shows the strenght as a bar of asterisks.
# Include additional feedback messages about which character types are missing from the password.

# CONSTANTS
UPPER = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
LOWER = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
DIGITS = ['0','1','2','3','4','5','6','7','8','9']
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "\"", "'", ",", ".", "<", ">", "?", "/", "`", "~"]

# Check if a word is present in a file
def word_in_file(word, filename, case_sensitive=False):
    if not filename:
        print(f'Error: {filename} not found.')
        return

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if case_sensitive:
                if line == word:
                    return True
            else:
                if line.lower() == word.lower():
                    return True
                
    return False

# Check if a word contains any character from a given list
def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    
    return False

# Determinate the complexity of a password
def word_complexity(word):
    complexity = 0

    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    
    return complexity

# Calculate the password strength
def password_strength(password, min_length=10, strong_length=16):
    missing_chars = []

    if word_in_file(password, 'wordlist.txt', case_sensitive=False):
        print('Password is a dictionary word and is not secure.')
        return 0
    
    if word_in_file(password, 'toppasswords.txt', case_sensitive=True):
        print('Password is a commonly used password and is not secure.')
        return 0
    
    if len(password) < min_length:
        print('Password is too short and is not secure.')
        return 1
    
    if len(password) >= strong_length:
        print('Password is long, length trumps complexity this is a good password')
        return 5
    
    complexity = word_complexity(password)
    strength = 1 + complexity

    # Additional feedback for missing character types
    if not word_has_character(password, UPPER):
        missing_chars.append('uppercase letter')
    if not word_has_character(password, LOWER):
        missing_chars.append('lowercase letter')
    if not word_has_character(password, DIGITS):
        missing_chars.append('digit')
    if not word_has_character(password, SPECIAL):
        missing_chars.append('special character')

    if missing_chars:
        print(f'Password needs: {', '.join(missing_chars)}')

    return strength

# Visualize the password strength
def visualize_strength(strength):
    # Create a bar of asterisks to represent password strength
    asterisks = '*' * strength
    print(f'Strength visualization: [{asterisks}] ({strength}/5)')

def main():
    while True:
        password = input('Enter a password to check its strength (or "q" to quit): ')

        if password.lower() == 'q':
            print('Exiting the password strength checker.')
            break

        strength = password_strength(password)
        print(f'Password strength: {strength}')
        visualize_strength(strength)

if __name__ == '__main__':
    main()