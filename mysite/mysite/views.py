from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return render(request, 'bootlash.html')


def text_analyzer(request):
    # Get the text
    dj_text = request.GET.get('texta', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    print(dj_text)
    print(removepunc)
    print(fullcaps)
    print(newlineremover)

    #Check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        result = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', result)

    elif fullcaps == 'on':
        analyzed = ''
        for char in dj_text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == 'on':
        analyzed = ''
        for char in dj_text:
            if char != '\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(dj_text):
            if not (dj_text[index] ==' ' and dj_text[index+1] ==' '):
                analyzed = analyzed + char
        params = {'purpose': 'Removed extra spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse('<h1 align="center">no input given for remove punchuations  </h1>')


# def capfirst(request):
#     return HttpResponse('capitalize first')
#
#
# def newlineremove(request):
#     return HttpResponse('capitalize first')
#
#
# def spaceremove(request):
#     return HttpResponse('space remover')
#
#
# def charcount(request):
#     return HttpResponse('charcount ')
