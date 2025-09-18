



def top_words(text, n):

    words = {}
    for word in text.split(" "):
        cleansed_word = ""
        for letter in word.lower():
            if letter.isalpha():
                cleansed_word += letter
        if cleansed_word in words:
            words[cleansed_word] += 1
        else:
            words[cleansed_word] = 1
    sorted_words = sorted(words.items(), key=lambda item: item[1], reverse=True)
    
    top_words = []
    for i in range(n):
        top_words.append(sorted_words[i][0])
        
    return top_words


text = "Hello world! Hello Python. Python is great, and Python is fun."
print(top_words(text, 2))