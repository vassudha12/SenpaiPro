from django.shortcuts import render

from django.http import HttpResponse

from .models import Book


def index(request):
    return HttpResponse("Hello world")


def book_by_id(request):
    #book = Book.objects.get(pk=book_id)
    book = Book.objects.all()
    return render(request,'book_details.html',{'books':book})
    # return HttpResponse(f"Book:{book.title}, published on {book.pub_date}")

#do min do

# def book_by_id(request):
#   book = Book.objects.all()
#   return render(request, 'list.html', name())
