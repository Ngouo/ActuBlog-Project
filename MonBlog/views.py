from django.shortcuts import render, redirect
from .models import PostModel
from .form import PostModelForm, PostUpdateForm, CommentForm
from django.template.defaultfilters import truncatewords
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.


@login_required
def homeBlog(request):
  posts = PostModel.objects.all()
  paginator = Paginator(posts, 5)
  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  
  if request.method == 'GET':
    title = request.GET.get("recherche")
    if title is not None:
      page_obj = PostModel.objects.filter(title__icontains=title)
      
  context = {
    'posts': posts,
    'page_obj':page_obj,
  }
  
  return render(request, 'MonBlog/index.html', context)


@login_required
def post_submit(request):
  if request.method == 'POST':
    form = PostModelForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.auteur = request.user
      instance.save()
      return redirect('homeBlog')
  else:
    form = PostModelForm()
  context = {
  #  'posts': posts,
    'form': form,
  }
  
  return render(request, 'MonBlog/post_submit.html', context)


@login_required
def post_detail2(request, pk):
  post = PostModel.objects.get(id=pk)
  if request.method == 'POST':
    c_form = CommentForm(request.POST)
    if c_form.is_valid():
      instance = c_form.save(commit=False)
      instance.user = request.user
      instance.post = post
      instance.save()
      c_form = CommentForm()
      redirect('post_detail2', pk=post.id)
  else:
    c_form = CommentForm()
  context = {
    "post": post,
    'c_form': c_form,
  }
  return render(request, 'MonBlog/post_detail.html', context)


@login_required
def post_edit(request, pk):
  post = PostModel.objects.get(id=pk)
  if request.method == 'POST':
    form = PostUpdateForm(request.POST, instance=post)
    if form.is_valid():
      form.save()
      return redirect('post_detail2', pk=post.id)
  else:
    form = PostUpdateForm(instance=post)      #"instance=post" permet de preciser que c'est bien l'article selectionné que l'on doit modifier
  context = {
    'post':post,
    'form': form
  }
  return render(request, 'MonBlog/post_edit.html', context)



@login_required
def post_delete(request, pk):
  post = PostModel.objects.get(id=pk)
  if request.method == 'POST':
    post.delete()
    return redirect("homeBlog")
  context = {
    'post': post
  }
  return render(request, 'MonBlog/post_delete.html', context)


def infos(request):
  return render(request, 'MonBlog/infos.html')


