from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'wordcount/index.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary={}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else :
            word_dictionary[word] = 1
    return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total':len(word_list), 'dictionary':word_dictionary.items()})

def alphabet(request):
    full_text = request.GET['fulltext']

    alphabet_dictionary={}
 
    for alphabet in full_text[:]:
        if(alphabet != ' ' and alphabet!="." and alphabet != ","):
            if alphabet in alphabet_dictionary:
                alphabet_dictionary[alphabet] += 1
            else :
                alphabet_dictionary[alphabet] = 1
    return render(request, 'wordcount/alphabet.html', {'fulltext': full_text, 'total':len(alphabet), 'dictionary':alphabet_dictionary.items()})