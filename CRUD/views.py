from django.http import Http404
from CRUD.models import Crud
from django.views.generic import UpdateView, ListView, FormView, DetailView, DeleteView
from django.urls import reverse_lazy
from CRUD.forms import RegUserForm


class UserListView(ListView):

    model = Crud
    template_name = 'index.html'


class AddUserView(FormView):

    form_class = RegUserForm
    template_name = 'add_user_form.html'
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response


class GetUserDetailView(DetailView):

    template_name = 'got_user.html'

    def get_object(self, queryset=None):
        try:
            specific_user = Crud.objects.get(id=self.kwargs.get('user_id'))
        except Crud.DoesNotExist:
            raise Http404("User does not exist")
        return specific_user


class UpdateUserView(UpdateView):

    template_name = 'edit_user_form.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('user-list')

    def get_object(self, queryset=None):
        try:
            specific_user = Crud.objects.get(id=self.kwargs.get('user_id'))
        except Crud.DoesNotExist:
            raise Http404("User does not exist")
        return specific_user


class DeleteUserView(DeleteView):

    template_name = 'confirm_user_delete.html'
    success_url = reverse_lazy('user-list')

    def get_object(self, queryset=None):
        try:
            specific_user = Crud.objects.get(id=self.kwargs.get('user_id'))
        except Crud.DoesNotExist:
            raise Http404("User does not exist")
        return specific_user
