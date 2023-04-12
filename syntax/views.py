from django.shortcuts import render
from pydictionary import Dictionary

# Create your views here.


# this is the view that will render search page
def searchView(request):
        # capturing the word from the form via the name search
    word = request.GET.get('search')
    # creating a dictionary object
    dict = Dictionary(word)
    # passing a word to the dictionary object
    meanings = dict.meanings()
    # getting a synonym and antonym  
    synonyms = dict.synonyms()
    antonyms = dict.antonyms()
    # bundling all the variables in the context  
    context = {
            'word': word,
            'meanings':meanings,
            'synonyms':synonyms,
            'antonoyms':antonyms
        }
    return render(request, 'syntax/DictionaryPage.html', context)

def homePage(request):
    return render(request, 'syntax/homePage.html')

def DictionaryPage(request):
    return render(request, 'syntax/DictionaryPage.html')
