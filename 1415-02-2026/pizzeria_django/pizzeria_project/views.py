from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Witaj w pizzerii</h1>")

def booklist(request):
    books = [
        {'title': 'Python Crash Course', 'author': 'Eric Matthes'},
        {'title': 'Fluent Python', 'author': 'Luciano Ramalho'},
        {'title': 'Fluent Python 3', 'author': 'Luciano Ramalho'},
    ]
    return render(request, 'books/book_list.html', {'books': books})