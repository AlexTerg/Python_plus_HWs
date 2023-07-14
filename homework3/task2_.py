from string import punctuation

text = '''Основы языка python — это своеобразный фундамент, 
без которого в мире программирования на Python, сложно будет добиться успехов. 
На данной странице, собраны статьи покрывающие практически всю основу Python. 
Весь материал по возможности обновляется, и дополняется. 
В случае если у вас возникнут вопросы, пишите в комментариях, буду рад вам помочь.'''

# marks = '''!()-[]{};?@#$%:'"\,./^&;*_'''

for val in text:
    if val in punctuation:
        text = text.replace(val, '')

text_lst = text.split()

text_dict = {i: text_lst.count(i) for i in text_lst}


sorted_dict = dict(
    sorted(text_dict.items(), key=lambda i: i[1], reverse=True)[:10])

print(sorted_dict)
