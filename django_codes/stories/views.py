from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from stories.models import Recipe, Category, Tag
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from stories.forms import CommentForm, SubCommentForm
from django.urls import reverse_lazy

# Create your views here.

# def recipes(request):
#     # print('Liked Posts: ', request.session.get('liked_posts'))
#     recipe = Recipe.objects.all()
#     context = {
#         'recipe_list' : recipe
#     }
#     return render(request, 'recipes.html', context)


class RecipeListView(ListView):
    template_name = 'recipes.html'
    model = Recipe
    context_object_name = 'recipes'
    paginate_by = 2
    # recipe_list


def stories(request):
    return render(request, 'stories.html')

# def recipe_detail(request, pk):
#     recipe = get_object_or_404(Recipe, id = pk)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     context = {
#         'recipe' : recipe,
#         'categories' : categories,
#         'tags' : tags
#     }
#     return render(request, 'single.html', context)


class RecipeDetailView(FormMixin, DetailView):
    template_name = 'single.html'
    model = Recipe
    form_class = CommentForm
    subform = SubCommentForm
    # success_url = reverse_lazy('recipe_detail')

    def get_success_url(self) -> str:
        return reverse_lazy('recipe_detail', kwargs = {'pk' : self.object.pk})

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if 'parent' in request.POST:
            form = self.subform
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.parent_id = self.request.POST.get('parent', None)
        form.instance.recipe = self.object
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

# def like_post(request, pk):
#     request.session['liked_posts'] = request.session.get('liked_posts', ' ') + str(pk) + ' '
#     messages.add_message(request, messages.SUCCESS, "Liked!")
#     return render(request, 'recipes.html')

def like_post(request, pk):
    response = HttpResponse('test')
    response.set_cookie('liked_posts', request.COOKIES.get('liked_posts', ' ') + str(pk) + ' ')
    return response