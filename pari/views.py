from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
   ListView, 
   DetailView, 
   CreateView,
   UpdateView,
   DeleteView,
   
)
from django.shortcuts import render
from .models  import Post
from .models  import Tiquet
from .models  import Lotterie
from .models  import Resultat

def listiquet(request):
   context = {
      'tiquets': Tiquet.objects.all()
   }
   return render(request, 'pari/listik.html', context)

class TiquetListView(ListView):
   model = Tiquet
   template_name = 'pari/listik.html'
   context_object_name = 'tiquets'
   ordering = ['-datepari']

class TiquetCreateview(CreateView):
   model = Tiquet
   fields = ['Lotterie','numero1', 'numero2', 'mise']

   def form_valid(self, form):
      form.instance.recu = self.request.user
      return super().form_valid(form)

class TiquetDetailView(DetailView):
   model = Tiquet
   

def home(request):
   context = {
      'lotteries': Lotterie.objects.all()
   }
   return render(request, 'pari/index.html', context)
class LotterieView(ListView):
   model = Lotterie
   template_name = 'pari/index.html'
   context_object_name = 'lotteries'
   ordering = ['-ouverture']



def forum(request):
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'pari/forum.html', context)

class PostListView(ListView):
   model = Post
   template_name = 'pari/forum.html'
   context_object_name = 'posts'
   ordering = ['-datepost']


class ResultatView(ListView):
   model = Resultat
   template_name = 'pari/resultat.html'
   context_object_name = 'resultats'
   ordering = ['-ouverture']
   


class PostDetailView(DetailView):
   model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
   model = Post
   fields = ['titre', 'contenu']

   def form_valid(self, form):
      form.instance.auteur = self.request.user
      return super().form_valid(form)
  

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   model = Post
   fields = ['titre', 'contenu']

   def form_valid(self, form):
      form.instance.auteur = self.request.user
      return super().form_valid(form)
  
   def test_func(self):
      post = self.get_object()
      if self.request.user == post.auteur:
         return True
      return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Post
   success_url = '/forum'

   def test_func(self):
      post = self.get_object()
      if self.request.user == post.auteur:
         return True
      return False
