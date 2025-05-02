# ДЗ 5.3. hashtag

import re

def generate_hashtag(user_input):
    
    cleaned = re.sub(r'[^\w\s]', '', user_input)
    
   
    hashtag = '#' + ''.join(word.capitalize() for word in cleaned.split())
    
    
    return hashtag[:140] if len(hashtag) > 140 else hashtag

print(generate_hashtag('Python Community'))  
print(generate_hashtag('i like python community!'))  
print(generate_hashtag('Should, I. subscribe? Yes!'))  