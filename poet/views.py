from django.shortcuts import render
from db.db_helper import *


def home_page_view(request):
    """
    Provides some arithmetic functions
    """
    poet_generator = get_all_poetries()
    context = {
        'poets': poet_generator,
    }
    return render(request, 'poet/home_page.html', context=context)


def poet_books_view(request, poet_id):
    """
    get all books of one poet and make a view depent on it
    """
    works = get_all_works_of_a_poet(poet_id=poet_id)
    descrition = get_poet_info(poet_id=poet_id)
    context = {
        'poet_id': poet_id,
        'works': works,
        'description': descrition
    }
    return render(request, 'poet/poet_books.html', context=context)


def book_titles_view(request,poet_id, cat_id):
    titles = get_all_titles_of_a_work(cat_id)
    book_name = get_book_name_by_cat_id(cat_id)
    context = {
        'poet_id': poet_id,
        'titles': titles,
        'book_name': book_name
    }
    return render(request, 'poet/book_titles.html', context=context)


def poem_content_view(request,poet_id, cat_id, poem_id):
    verses = get_all_verses_of_a_poem(poem_id)
    context = {'verses': verses}
    return render(request, 'poet/poem_content.html', context=context)
