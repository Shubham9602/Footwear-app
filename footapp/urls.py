from footapp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
'''
urlpatterns = [
    path('about',views.about),
    path('contact',views.contact),
    path('base',views.base),
]
'''
urlpatterns=[
    path('products',views.products),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sort),
    path('pricefilter',views.pricefilter),
    path('product_detail/<pid>',views.product_detail),
    path('addtocart/<pid>',views.cart),
    path('viewcart',views.viewcart),
    path('updateqty/<x>/<cid>',views.updateqty),
    path('removecart/<cid>',views.removecart),
    path('placeorder',views.placeorder),
    path('fetchorder',views.fetchorder),
    path('makepayment',views.makepayment),
    path('paymentsuccess',views.paymentsuccess),
    path('search',views.search),
    path('contact',views.contact),
    path('about',views.about),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)