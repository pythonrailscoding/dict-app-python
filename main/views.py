from django.shortcuts import render
from PyDictionary import PyDictionary

def index(request):
    return render(request, 'index.html', {})

def dict(request):
    word = request.POST['word']
    dictionary = PyDictionary()
    synonyms = dictionary.synonym(word)
    antonym = dictionary.antonym(word)
    meaning = dictionary.meaning(word)
    # print(synonyms, antonym, meaning)
    return render(request, 'dict.html', {'synonym': synonyms, 'antonym': antonym, 'meaning': meaning, 'word': word})
