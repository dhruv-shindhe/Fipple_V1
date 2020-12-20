from django.shortcuts import render, redirect
from .models import Store
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    # products = Store.objects.all().order_by('-date_posted')
    # context = {'products':products}
    # return render(request, 'store/home.html', context)
    if request.user.is_authenticated:
        name = request.user.username
        # user = User.objects.filter(username=name).first()
        # insta_link = "https://www.instagram.com/"+user.profile.instagram_ID
        # product = Store.objects.filter(author=user).order_by('-date_posted')
        # img_url = user.profile.image.url
        # user_name = name
        # context = {'products':product, 'img_url':img_url, 'user_name':user_name, 'insta_link':insta_link}
        return redirect('/'+name+'/store')
    else:
        return redirect('/home')


def mystore(request, name):
    user = User.objects.filter(username=name).first()
    product = Store.objects.filter(author=user).order_by('-date_posted')
    img_url = user.profile.image.url
    insta_link = "https://www.instagram.com/"+user.profile.instagram_ID
    user_name = name
    context = {'products':product, 'img_url':img_url, 'user_name':user_name, 'insta_link':insta_link}
    return render(request,'store/store_list.html',context)


def terms_and_conditions(request):
    return render(request, 'store/terms_and_conditions.html')


def privacy_policy(request):
    return render(request, 'store/privacy_policy.html')

def contact(request):
    return render(request, 'store/contact.html')


def about(request):
    return render(request, 'store/about.html')

def home_1(request):
    return render(request, 'store/home_1.html')



class StoreDetailView( DetailView):
    model = Store


class StoreCreateView(LoginRequiredMixin, CreateView):
    model = Store
    fields = ['title', 'description', 'image', 'affiliate_link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class StoreDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Store
    success_url = '/'

    def test_func(self):
        store = self.get_object()
        if store.author == self.request.user:
            return True
        return False


class StoreUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Store
    fields = ['title', 'description', 'image', 'affiliate_link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        store = self.get_object()
        if store.author == self.request.user:
            return True
        return False
