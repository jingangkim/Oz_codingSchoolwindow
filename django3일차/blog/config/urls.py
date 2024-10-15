
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import include, path, reverse
from django.views import View
from django.views.generic import RedirectView, TemplateView

from blog import views
from blog import cb_views

from member import views as member_views


# class AboutView(TemplateView):
#     template_name = 'about.html'
#
#
# class TestView(View):
#     def get(self, request):
#         return render(request, 'test_get.html')
#
#     def post(self, request):
#         return render(request, 'test_post.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    # FBV blog
    path('', views.blog_list, name="blog_list"),
    path('<int:pk>/', views.blog_detail, name="blog_detail"),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:pk>/update/', views.blog_update, name='blog_update'),
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    # CBV blog
    path('cb/', cb_views.BlogListView.as_view(), name='cb_blog_list'),
    path('cb/<int:pk>/', cb_views.BlogDetailView.as_view(), name='cb_blog_detail'),
    path('cb/create/', cb_views.BlogCreateView.as_view(), name='cb_blog_create'),

    # auth
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', member_views.sign_up, name='signup'),
    path('login/', member_views.login, name='login'),


    # path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    # path('about/', AboutView.as_view(), name='about'),
    # path('redirect/', RedirectView.as_view(pattern_name='about'), name='redirect'),
    # path('test/', TestView.as_view(), name='test'),
    # path('redirect2/', lambda req: redirect(reverse('about'))),
]