from basket_app import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

app_name= "basket_app"

urlpatterns = [
    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name="logout"),
    path('category/<slug:slug>/',views.ProductView.as_view(), name='product'),
    path('add-to-cart/<int:pk>/',views.add_to_cart, name='add-to-cart'),
    path('cart/',views.CartView.as_view(), name='cart'),
    path('increase_qty/<int:pk>/',views.increase_qty, name='increase-qty'),
    path('decrease_qty/<int:pk>/',views.decrease_qty, name='decrease-qty'),
    path('remove_product/<int:pk>/',views.remove_product, name='remove-product'),
    path('fillup/',views.Orderform.as_view(), name='fillup'),
    path('order/',views.OrderView.as_view(), name='order'),
    path('ordered/<int:pk>/',views.OrderSummary.as_view(), name='orderdetail'),
    # path("category/<str:cname>",views.categories,name="category"),

    
]

