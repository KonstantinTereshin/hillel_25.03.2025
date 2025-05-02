#ДЗ 7.2. Модифікувати рядок

def correct_sentence(text):
    if not text:  
        return text
    
    corrected = text[0].upper() + text[1:]
    
    if not corrected.endswith('.'):
        corrected += '.'
    return corrected

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')