TASK 1
Input: text = (input('Enter the text: ')) prompts the user to enter text and stores it in the text variable.

Chained Operations: words = text.upper().strip().replace('A','E').split() performs a series of operations on the input text:

text.upper(): Converts the text to uppercase.
.strip(): Removes leading and trailing whitespace.
.replace('A','E'): Replaces all occurrences of 'A' with 'E'.
.split(): Splits the string into a list of words, using whitespace as the delimiter.
Output: print(words) prints the resulting list of words.

TASK 2
Original String: article = 'Python programming language' assigns the string "Python programming language" to the article variable.

Reversal: reverse_article = article[::-1] reverses the string using slicing. [::-1] creates a reversed copy of the string.

Print Reversed String: print('Inverted text',reverse_article) prints the reversed string.

Replacement: new_article = article.replace('programming','coding') replaces the substring "programming" with "coding" in the original string.

Print Modified String: print('Modified text:',new_article) prints the modified string.
