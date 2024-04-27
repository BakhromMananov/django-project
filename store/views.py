from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from .decorators import login_required

# Create your views here.
def index(request):
    items = Item.objects.all()
    tags= Tags.objects.all()
    categories = Category.objects.all()
    
    selected_cat = request.GET.get('options')


    if selected_cat:
        items = items.filter(category__id=selected_cat)
        print(items)

    
    search_query = request.GET.get('title')

    if search_query:
        items = items.filter(title__icontains = search_query)

    return render(request, 'store/index.html', {'title': 'Amazon', 'items': items, 'tags': tags, 'categories': categories})

def user_login(request):
    categories = Category.objects.all()

    if request.user.is_authenticated:
        return redirect('home')
    
    form = LoginForm()
    message= None

    if request.method == 'POST':
        
        form=LoginForm(data=request.POST)
        print(form)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user=authenticate(username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, f'Welcome to Amazon "{user}"')
                return redirect('home')
            message = 'User does not exist or pass is incorrect'

    return render(request, 'store/login.html', {'categories': categories, 'form': form, 'message': message})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('home')


def register(request):
    categories = Category.objects.all()
    return render(request, 'store/register.html', {'categories': categories})

@login_required()
def create(request):
    mes = None
    categories = Category.objects.all()
    if request.method == 'POST':
        form=CreatePost(request.POST, request.FILES)
        
        if form.is_valid():
            image = form.cleaned_data['image']
            title=form.cleaned_data['title']
            slug=form.cleaned_data['slug']
            content=form.cleaned_data['content']
            category=form.cleaned_data['category']
            price=form.cleaned_data['price']
            rating=form.cleaned_data['rating']
            messages.success(request, f'The news "{title}" has been successfully created!')
           

            new_item=Item.objects.create(image=image, title=title, slug=slug, content=content, category=category, price=price, rating=rating)
            
            return redirect('home')
        mes = messages.error(request, 'Post created')

    else:
        form=CreatePost()

    
    
    return render(request, 'store/create.html', {'form': form, 'mes': mes, 'categories': categories} )



# def create(request):
#     cats = Category.objects.all()
#     tags=Tags.objects.all()
#     context = {
#         'cats': cats,
#         'tags': tags
#     }
    
#     if request.method == 'POST':
#         print(request.POST)

#         cat_id=int(request.POST.get('category'))
#         tag_ids=list(map(int, request.POST.getlist('tags')))
#         tag_items=set(Tags.objects.filter(id__in=tag_ids))
#         image = request.FILES.get('image')
#         data= {
#             'image': request.FILES.get('image'), 
#             'title': request.POST.get('title'),
#             'slug': request.POST.get('title'),
#             'content': request.POST.get('content'),
#             'category': Category.objects.get(id=cat_id),
#             'price': request.POST.get('price'),
#             'rating': request.POST.get('rating'), 
#         }

#         item = Item.objects.create(**data)
#         item.tags.add(*tag_items)
#         item.image.save(image.name, image)
#         print(tags)

#         return redirect('home')
    
#     return render(request, 'store/create.html', context=context)


def item(request, item_id):
    item_id = int(item_id)
    item=Item.objects.filter(id =item_id)

    return render(request, 'store/item.html', {'item': item} )

@login_required()
def edit(request, item_id):
    item_id = int(item_id)
    item=get_object_or_404(Item, id=item_id)

    # print(request.POST.get('category'))
    
    if request.method == 'POST':

        category_id = int(request.POST.get('category'))
        category = get_object_or_404(Category, id=category_id)
        tag_ids=list(map(int, request.POST.getlist('tags')))
        tags = Tags.objects.filter(id__in=tag_ids)
        image=request.FILES.get('image')

        if image:
            item.image.save(image.name, image)

        item.tags.clear()
        item.tags.add(*tags)

        item.title=request.POST.get('title')
        item.content = request.POST.get('content')
        item.price=request.POST.get('price')
        item.rating=request.POST.get('rating')
        item.category = category
        item.tags.set(tags)
        item.save()

        return redirect('home')

    tags=Tags.objects.all()
    category=Category.objects.all()
    
    return render(request, 'store/edit.html', {'item': item, 'categories': category, 'tags': tags} )

@login_required()
def delete(request, item_id):
    item_id = int(item_id)
    item=get_object_or_404(Item, id =item_id)
    item.delete()
    

    return redirect('home')


