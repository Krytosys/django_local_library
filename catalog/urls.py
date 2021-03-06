
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [
    path('onloan/', views.AllLoanedBooksListView.as_view(), name="all-borrowed"),
]

urlpatterns += [
    path('addstaff/', views.staff_add_view, name="addStaff"),
    path('logs/', views.LogListView.as_view(), name='logs')
]

urlpatterns += [
    path('borrowed/<uuid:pk>/', views.borrowBook_view, name='borrowBook'),
    path('review/<int:pk>', views.reviewCreate_view, name='commentReview'),
    path('returned/<uuid:pk>/', views.returnBook_view, name='returnBook'),
]

urlpatterns += [
    path('author/modifyauthors/', views.AuthorsModify.as_view(), name='author_modify'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

urlpatterns += [
    path('book/modifybooks/', views.BooksModify.as_view(), name='book_modify'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]

urlpatterns+=[
    path('bookinstance/modifybooks/', views.BookInstanceModify.as_view(), name='bookinstance_modify'),
    path('bookinstance/create/', views.BookInstanceCreate.as_view(), name ='book_instance_create'),
    path('bookinstance/<uuid:pk>/update/', views.BookInstanceUpdate.as_view(), name ='book_instance_update'),
    path('bookinstance/<uuid:pk>/delete/', views.BookInstanceDelete.as_view(), name ='book_instance_delete'),
]

urlpatterns+=[
    path('language/modifybooks/', views.LanguageModify.as_view(), name='language_modify'),
    path('language/create/', views.LanguageCreate.as_view(), name ='language_create'),
    path('language/<int:pk>/update/', views.LanguageUpdate.as_view(), name ='language_update'),
    path('language/<int:pk>/delete/', views.LanguageDelete.as_view(), name ='language_delete'),
]

urlpatterns+=[
    path('genre/modifybooks/', views.GenreModify.as_view(), name='genre_modify'), 
    path('genre/create/', views.GenreCreate.as_view(), name ='genre_create'),
    path('genre/<int:pk>/update/', views.GenreUpdate.as_view(), name ='genre_update'),
    path('genre/<int:pk>/delete/', views.GenreDelete.as_view(), name ='genre_delete'),
]

urlpatterns += [
    path('profile/', views.UserProfile.as_view(), name='user_profile'),
]

urlpatterns += [
    path('signup/', views.signup_view, name="signup"),
    path('lockout/', views.lockout_view, name="lockout"),
    path('passwordreset/', views.passwordReset_view, name="reset"),
    path('emailreset/', views.emailRequest_view, name="email-reset"),
]