# from transliterate import translit
# ru_text = 'Лорем ипсум долор сит амет'
# text = translit(ru_text, language_code='ru', reversed=True)
# text
# 'Lorem ipsum dolor sit amet'

from googletrans import Translator


translator = Translator()
text = 'Кыргызстан'
print(translator.translate(text, src='ru', dest='en'))