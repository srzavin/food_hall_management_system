from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpRequest
from django.contrib.auth.models import User, Group
from .models import *
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.




def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to the user page
        else:
            messages.info(request, "Username or Password is Incorrect")
    return render(request, 'Store\login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')


def create_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            user = form.save()

            group_name = form.cleaned_data['group']
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            return redirect('login')
    context = {'form': form}
    return render(request, 'Store\createUser.html', context)


def store_view(request):
    username = request.user.username
    try:
        user = User.objects.get(username=username)
        groups = user.groups.all()

        group_names = [group.name for group in groups]
        print("WORKIGN ")
        print(group_names)

    except:
        print("NOT WORKIGN ")
        pass
    ebooks = {'eBooks': Ebook.objects.all(), 'username': username}

    return render(request, 'Store\index.html', ebooks)

def cart_view(request):
    username = request.user.username
    user = User.objects.get(username=username)
    objs = Cart.objects.filter(user_id = user.id).select_related('product')
    userprods = Cart.objects.filter(user_id= user.id)
    totalPrice = 0
    if request.method == "POST":
        productAdd = request.POST.get('Add')  #adds product to the list\
        productSub = request.POST.get('Remove')
        checkout = request.POST.get('checkout')

        if productAdd != None:
            tempqty = Cart.objects.get(user_id=user.id, product_id=productAdd).quantity
            tempqty += 1
            Cart.objects.filter(product_id=productAdd, user_id=user.id).update(quantity=tempqty)
        elif productSub != None:
            tempqty = Cart.objects.get(user_id=user.id, product_id=productSub).quantity
            tempqty -= 1
            if tempqty == 0:
                Cart.objects.filter(product_id=productSub, user_id=user.id).delete()
            else:
                Cart.objects.filter(product_id=productSub, user_id=user.id).update(quantity=tempqty)
        elif checkout!=None:
            print("incheckout")
            order = Orders(user_id=1, product_id=1 , tableNumber=1, quantity=1, totalPrice =1 , paymentStatus="paid" , orderStatus="Finished")
            order.save()






            return redirect('checkout')

        return HttpResponseRedirect(reverse('cart'))

    for items in userprods:
        unitprc = items.product.price
        totalPrice += unitprc * items.quantity
    ctx = { 'username': username, 'cartV': objs, 'totalPrice':totalPrice}
    return render(request, 'Store\cart.html', ctx)

def menu_view(request):
    username = request.user.username
    store = request.POST.get('shop')
    userO = User.objects.get(username=username)

    if request.method == 'POST':

        id = request.POST.get('id')
        product_id = request.POST.get("food_id")

        try:
            prod_exists = Cart.objects.filter(user_id= userO.id, product_id = product_id).exists()
            if prod_exists == False:
                product = Cart(product_id=product_id, user_id=userO.id, quantity=1)
                product.save()
            else:
                tempqty = Cart.objects.get(user_id= userO.id, product_id=product_id).quantity
                tempqty+=1
                Cart.objects.filter(product_id=product_id, user_id=userO.id).update(quantity=tempqty)
            messages.info(request, "Product added to the cart!")

        except:
            pass


    menu = redir(store, id)
    ctx = {'menu': menu, 'store': store, 'username': username}
    return render(request, 'Store\menu.html',ctx)


def checkout(request):
    username = request.user.username

    ctx = {'username': username}
    return render(request, 'Store\checkout.html', ctx)
