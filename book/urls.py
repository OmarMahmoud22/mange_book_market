from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='index' ),
    path('books/' , views.books , name='book' ),
    path('delete/<int:id>' , views.delete , name='delete' ),
    path('update/<int:id>' , views.update , name='update' ),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>' , views.book_details , name ='detalis')
]
