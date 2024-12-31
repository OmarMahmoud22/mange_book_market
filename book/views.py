from django.shortcuts import render , get_object_or_404 , redirect
from .models import Books , Category
from .form import BookForm , CateoryForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        # Handle BookForm
        bookform = BookForm(request.POST, request.FILES)
        if bookform.is_valid():
            book_title = bookform.cleaned_data.get('title')
            if not Books.objects.filter(title=book_title).exists():
              bookform.save()
        

        add_cat = CateoryForm(request.POST)
        if add_cat.is_valid():
            Category_name = add_cat.cleaned_data.get('name')
            if not Category.objects.filter(name=Category_name).exists():
                add_cat.save()
        
    context = {
        'books': Books.objects.all(),
        'category': Category.objects.all(),
        'form': BookForm(),  # New form instance
        'form_cat': CateoryForm(),  # New form instance with fixed typo
        'count_of_books' : Books.objects.filter(active=True).count(),
        'sold' : Books.objects.filter(status='SOLD').count(),
        'rental' : Books.objects.filter(status='RENTAL').count(),
        'ava' : Books.objects.filter(status='AVAILABLE').count(),
    }

    return render(request, 'book/index.html', context)

@login_required
def books(request):
    search = Books.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search= search.filter(title__icontains = title)


    catecory = Category.objects.all()
    return render(request , 'book/books.html' , {'books':search , 'category' : catecory})

@login_required
def delete(request , id):
    book = get_object_or_404(Books , id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('/')
    return render(request , 'book/delete.html')

@login_required
def update(request , id):
    book = get_object_or_404(Books , id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES , instance=book)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book)    
    return render(request , 'book/update.html' , {'book_form_update' : book_save})

@login_required
def book_details(requset , year , month , day , slug):
    book = get_object_or_404(Books,
                             slug=slug,
                            publish__year= year
                             ,publish__month=month,
                             publish__day = day,
                             
                             
                             )
    return render(requset , 'book/details.html' , {'book' : book})