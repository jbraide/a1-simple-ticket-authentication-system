from django.urls import path
from django.views.generic import RedirectView
from ticketsystem.views import IncorrectTicketIdView, IndexView
from . import views

app_name = 'ticketsystem'

urlpatterns = [
    path('', RedirectView.as_view(url='success/'), name='index'),
    path('success/', IndexView.as_view(), name='Success'),
    path('incorrect-ticket-id/', IncorrectTicketIdView.as_view(), name='incorrect'),
    path('generate/', views.create_ticket, name='create_ticket'),
    path('admins/', views.adminView, name='Administrator'),
    # path('admins/', AdminView.as_view(), name='Administrator')
]
