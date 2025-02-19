#Task 1

text = (input('Enter the text: '))
words = text.upper().strip().replace('A','E').split()

print(words)

#Task 2

article = 'Python programming language'
reverse_article = article[::-1]

print('Inverted text',reverse_article)  # Print inverted text on screen

new_article = article.replace('programming','coding')

print('Modified text:',new_article)  # Print modified text on screen

