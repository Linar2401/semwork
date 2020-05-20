from abc import ABC


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Avg, Q, Count, F
from django.shortcuts import redirect

from django.shortcuts import render, get_object_or_404


from django.views import defaults
from django.views.generic import *


from books.forms import *
from books.models import *
from utils.models import Post


class BaseCreateView(LoginRequiredMixin, CreateView, ABC):
    login_url = reverse_lazy('utils:sign_in')
    template_name = 'books/create_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.name
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class BaseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, ABC):
    login_url = reverse_lazy('utils:sign_in')
    template_name = 'books/update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.name
        return context

    def test_func(self):
        return self.request.user == get_object_or_404(self.model, pk=self.kwargs.get('pk')).user


class BaseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView, ABC):
    login_url = reverse_lazy('utils:sign_in')
    template_name = 'books/delete_form.html'

    def test_func(self):
        return self.request.user == get_object_or_404(self.model, pk=self.kwargs.get('pk')).user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.name
        return context


class BookView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class BookUpdateView(BaseUpdateView):
    model = Book
    fields = ['name', 'description', 'genres', 'warnings', 'rating', 'image', 'file_fb2', 'file_txt', 'file_epub',
              'published']
    name = 'Book'


class BookDeleteView(BaseDeleteView):
    model = Book
    success_url = reverse_lazy('utils:profile')
    name = 'Book'


class BookCreateView(BaseCreateView):
    model = Book
    fields = ['name', 'description', 'genres', 'warnings', 'rating', 'image', 'file_fb2', 'file_txt', 'file_epub',
              'published']
    name = 'Book'


class BookCreateByRequestView(BookCreateView):
    def form_valid(self, form):
        result = super().form_valid(form)
        self.object.request = get_object_or_404(BookRequest, pk=self.kwargs.get('request_id'))
        self.object.save()
        return result


class ReviewView(DetailView):
    model = Review
    context_object_name = 'review'
    template_name = 'books/review_view.html'


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['text', 'mark']
    name = 'Review'
    login_url = reverse_lazy('utils:sign_in')
    template_name = 'books/create_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.name
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.book = get_object_or_404(Book, pk=self.kwargs.get('book_id'))
        self.object.book.user_score = Review.objects.filter(book=self.object.book).aggregate(result=Avg('mark'))[
            'result']
        self.object.save()
        return super().form_valid(form)

    def recalculate_rating(self):
        reviews = self.object.book.review_set
        score = 0


class ReviewUpdateView(BaseUpdateView):
    model = Review
    fields = ['text']
    name = 'Review'


class ReviewDeleteView(BaseDeleteView):
    model = Review
    success_url = reverse_lazy('utils:profile')
    name = 'Review'


class RequestView(DetailView):
    model = BookRequest
    context_object_name = 'request'
    template_name = 'books/request_view.html'


class BookRequestCreateView(BaseCreateView):
    model = BookRequest
    fields = ['name', 'genres', 'warnings', 'rating', 'text']
    name = 'Book Request'


class BookRequestUpdateView(BaseUpdateView):
    model = BookRequest
    fields = ['name', 'genres', 'warnings', 'rating', 'text']
    name = 'Book Request'


class BookRequestDeleteView(BaseDeleteView):
    model = BookRequest
    success_url = reverse_lazy('utils:profile')
    name = 'Book Request'


class BookRequestView(DetailView):
    model = BookRequest
    context_object_name = 'request'
    template_name = 'request_view.html'


class CollectionView(DetailView):
    model = BookCollection
    context_object_name = 'collection'
    template_name = 'books/collection_view.html'


class BookCollectionCreateView(LoginRequiredMixin, FormView):
    # model = BookCollection
    # fields = ['name', 'open']
    form_class = CollectionForm
    name = 'Book Collection'
    login_url = reverse_lazy('utils:sign_in')
    template_name = 'books/create_form.html'

    def form_valid(self, form):
        BookCollection.objects.create(name=form.cleaned_data.get('name'), user=self.request.user,
                                      open=form.cleaned_data.get('open'))
        return redirect(reverse_lazy('utils:profile'))


class BookCollectionUpdateView(BaseUpdateView):
    model = BookCollection
    fields = ['name', 'open', 'books']
    name = 'Book Collection'


class BookCollectionDeleteView(BaseDeleteView):
    model = BookCollection
    success_url = reverse_lazy('utils:profile')
    name = 'Book Collection'


class CommentCreateView(LoginRequiredMixin, FormView):
    # model = BookCollection
    # fields = ['name', 'open']
    form_class = CommentForm
    name = 'Form'
    login_url = reverse_lazy('utils:sign_in')
    template_name = 'books/create_form.html'

    def form_valid(self, form):
        Comment.objects.create(text=form.cleaned_data.get('text'), user=self.request.user,
                               book=get_object_or_404(Book, pk=self.kwargs.get('pk')), pub_date=datetime.datetime.now())
        return redirect(reverse_lazy('books:view', args=[self.kwargs.get('pk')]))


class BookListByAuthorView(TemplateView):
    model = Book
    template_name = "book_list.html"
    context_object_name = 'book_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = Book.objects.filter(user_id=self.kwargs.get('author_id'))
        context['is_author'] = self.request.user.id == self.kwargs.get('author_id')
        return context


class BookListByRequestView(TemplateView):
    model = Book
    template_name = "book_list.html"
    context_object_name = 'book_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = Book.objects.filter(request_id=self.kwargs.get('request_id'))
        context['is_author'] = self.request.user.id == self.kwargs.get('author_id')
        return context


class ReviewListByAuthorView(ListView):
    model = Review
    template_name = "review_list.html"
    context_object_name = 'review_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.queryset = Review.objects.filter(user=self.kwargs['author_id'])
        return context


class ReviewListByBookView(ListView):
    model = Review
    template_name = "review_list.html"
    context_object_name = 'review_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_id'] = get_object_or_404(Book, pk=self.kwargs['id']).id
        self.queryset = Review.objects.filter(book=self.kwargs['id'])
        return context


class RequestListByAuthorView(ListView):
    model = BookRequest
    template_name = "request_list.html"
    context_object_name = 'request_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.queryset = BookRequest.objects.filter(user=self.kwargs['author_id'])
        return context


class CollectionListByAuthorView(ListView):
    model = BookCollection
    template_name = "collection_list.html"
    context_object_name = 'collection_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.queryset = BookRequest.objects.filter(user=self.kwargs['author_id'])
        return context


def index(request):
    try:
        context = {
            'top_rated_books': Book.objects.filter(Q(user_score__gte=2.0), Q(file_fb2__isnull=False)).order_by(
                'user_score')[:6],
            'top_comment_books': Book.objects.annotate(
                count_comment=Count(F('comment'))).order_by('count_comment')[:6],
            'news': Post.objects.order_by('-pub_date')[:3]
        }
    except:
        raise defaults.server_error
    return render(request, 'books/index.html', context)


class AllBooks(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'


class AllReviews(ListView):
    model = Review
    template_name = 'books/review_list.html'


class AllCollections(ListView):
    model = BookCollection
    template_name = 'books/collection_list.html'


class AllRequest(ListView):
    model = BookRequest
    template_name = 'books/general_requests_list.html'
    context_object_name = 'reviews'


