from django.shortcuts import render, redirect
from books_authors_app.models import *

def index(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request,'index.html', context)



def post_books(request):
    Book.objects.create(title = request.POST['title'], desc=request.POST['description'])

    return redirect('/')



def info(request, id):
    context = {
        'book_by_id': Book.objects.get(id=id),
        'authors': Author.objects.all(),
    }

    if request.POST:
        return (add_author(request,id))
    
    return render(request, 'info.html', context)



def add_author(request, id):
    if request.POST:
        author_id = int(request.POST['select_an_author'])
        this_author = Author.objects.get(id=author_id)
        this_book = Book.objects.get(id=id)
        this_author.books.add(this_book)
        this_book.save()

    return redirect('/books/' + str(id) )

# *****************************************************

def create_author(request):
    context = {
        'authors': Author.objects.all(),
    }    
    if request.POST:
        return(post_authors(request))
    return render(request, 'create_author.html', context)


    # Author.objects.create(first_name= request.POST['first_name'], last_name=request.POST['last_name'] , notes=request.POST['notes'] )

def post_authors(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    print(Author.objects.all())
    
    return redirect('/authors')

def info_author(request, id):
    context = {
        'author_by_id': Author.objects.get(id=id),
        'books': Book.objects.all(),
    }

    if request.POST:
        return (add_book(request,id))
    
    return render(request, 'info_author.html', context)


def add_book(request, id):
    if request.POST:
        book_id = int(request.POST['select_a_book'])
        this_author = Author.objects.get(id=id)
        this_book = Book.objects.get(id=book_id)
        this_author.books.add(this_book)
        this_book.save()

    return redirect('/authors/' + str(id) )