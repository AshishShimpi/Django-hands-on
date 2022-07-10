from django.urls import path

from products.views import ( show_all_objects,
                             dynamic_lookup_view, 
                             product_delete_view, 
                             product_create_view ,
                             product_update_view
)

app_name = 'products'

urlpatterns = [

    path('', show_all_objects , name = 'product_view' ),
    path('create/' ,product_create_view , name = 'product_create'),
    path('<int:my_id>/' ,dynamic_lookup_view ,name = 'product_lookup'),
    path('<int:my_id>/update/', product_update_view , name = 'product_update'), 
    path('<int:my_id>/delete/' ,product_delete_view ,name = 'product_delete'),
       
]
