from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TicketModel

from ticketsystem.random_string_gen import usernameGenerator, passwordGenerator


# username and password filesave function
def fileSave(username, password):
    f = open('usernamePassword.txt', 'a+')
    f.write('%s, %s \n' % (username, password))
    f.close()


class IndexView(LoginRequiredMixin, View):
    template_name = 'ticket_sys/success-login.html'
    login_url = '/accounts/login'
    redirect_field_name = '/'

    def get(self, request):
        return render(request, self.template_name)


class IncorrectTicketIdView(View):
    template_name = 'ticket_sys/incorrect-ticket-id.html'

    def get(self, request):
        return render(request, self.template_name)


# class AdminView(View):
#     template_name = 'ticket_sys/admin.html'
#     model = TicketModel

#     def get(self, request):
#         return render(request, self.template_name)

@login_required
def adminView(request):
    ticket = User.objects.all()
    context = {
        'ticket': ticket
    }
    return render(request, 'ticket_sys/admin.html', context)


@login_required
def create_ticket(request):
    username = usernameGenerator()
    password = passwordGenerator()
    fileSave(username, password)
    ticket = User.objects.create_user(username=username, password=password)
    ticket.save()

    newUsername = User.objects.get(username=username).username

    output = '''
    <html>
      <head>
        <title>
          Generate Ticket ID
        </title>
      </head>
      <body>
        Generated Ticket ID: %s
      </body>
    </html>''' % (
        newUsername
    )

    return HttpResponse(output)
