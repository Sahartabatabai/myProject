from django.shortcuts import render

# Create your views here.
from .forms import CreateBookForm
from .models import Book
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages



def home(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            title = formdata['title']
            author = formdata['author']
            author2 = formdata['author2']

           
            if len(author) != len(author2):
                print("Authors differ in length by more than one character.")
            else:
                diff_count = sum(a != b for a, b in zip(author, author2))
                if diff_count > 1:
                    print("Authors differ by more than one character.")
                else:
              
                    Book.objects.create(title=title, author=author, author2=author2)
                    return HttpResponseRedirect('/success')
    else:
        form = CreateBookForm()
    return render(request, 'myapp3/createbook.html', {'form': form})







def success(request):
   return render(request, 'myapp3/success.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp3/book_list.html', {'books': books})


# View for editing a book
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        # Handle the book editing logic here
        # Update book fields and save it
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()

        return redirect('book_list')  # Redirect to the book list page

    return render(request, 'myapp3/edit_book.html', {'book': book})

# View for deleting a book
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        # Handle the book deletion logic here
        book.delete()

        return redirect('book_list')  # Redirect to the book list page

    return render(request, 'myapp3/delete_book.html', {'book': book})
