# English to Pig Latin
print('Enter  the  English  message  to  translate  into  Pig  Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # 一份单词列表。
for word in message.split():
    # 把这个单词开头的非字母分开:
    prefixNonLetters = ''
    while  len(word)  >  0  and  not  word[0].isalpha():
        prefixNonLetters  +=  word[0]
        word  =  word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # 把这个单词后面的非字母分开:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters  +=  word[-1]
        word = word[:-1]

    # 记住这个单词是大写的还是大写的.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # 为了便于翻译，请将单词小写.

    # 把这个单词开头的辅音分开:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # 在单词后面加上的拉丁语结尾:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
       word = word.upper()
    if wasTitle:
       word  =  word.title()

    # 将单词设置为大写或标题大小写.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# 把所有的单词重新组合成一个字符串:
print(' '.join(pigLatin))
