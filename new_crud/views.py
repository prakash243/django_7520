from django.shortcuts import render, redirect
from .models import *
import requests
from bs4 import BeautifulSoup

# Create your views here.
def newcrud(request):
    person_view = Person.objects.order_by('id')
    id = request.GET.get('id')
    # print(id)
    if id:
        person = Person.objects.get(id=id)
    context = {'person':person_view, 'persons':person if id else None}
    return render(request, 'newcrud.html', context)

def create(request):
    id = request.POST.get('id')
    if id:
        a = Person.objects.get(id=id)
    else:
        a = Person()
    a.name = request.POST['name']
    a.save()
    return redirect(newcrud)

def delete(request,pk):
    # id = request.POST.get('id')
    
    b = Person.objects.get(id=pk)
    if b:
        print(b)
        b.delete()
        return redirect(newcrud)
    return render(request, 'newcrud.html')

def delete1(request):
    id = request.GET.get('id')
    if id:
        c = Person.objects.get(id=id)
        print(c)
        c.delete()
        return redirect(newcrud)
    else:
        return render(request, 'newcrud.html')

def add_scraper(request):
    url = "https://www.imdb.com/chart/top/"

    r = requests.get(url)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')

    td = soup.find_all('td', class_='titleColumn')[5:]
    td_rating = soup.find_all('td',class_="ratingColumn imdbRating")


    # for rating in td_rating:
    #     rate = rating.strong.text


    for i in td:

        anchor = i.find_all('a')
        movie_name = i.a.text
        if not (Person.objects.filter(name=movie_name).exists()):

            m = Person.objects.create(name=movie_name)
        # print(i.a.text)
            for link in anchor:
                if link.get('href') != None:
                    links = "https://www.imdb.com" + link.get('href')
                    print(f"{i.a.text} -->> {links}" )
        else:
            return HttpRespose('All movie name already exists, we cannot add duplicate to your database')

    return render(request, 'index.html')
