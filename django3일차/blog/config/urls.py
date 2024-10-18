
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

    path('', include('blog.urls')),
    path('fb/', include('blog.fbv_urls')),
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