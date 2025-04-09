from django import template

register = template.Library()

censored_words = ['редиска', 'Редиска']

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError("Фильтр может быть применен только к строкам!")

    words = value.split()
    censored_text = []
    for word in words:
        if word in censored_words:
            censored_word = word[0] + '*' * (len(word) - 1)
            censored_text.append(censored_word)
        else:
            censored_text.append(word)
    return ' '.join(censored_text)