from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.http import HttpResponse
from django.contrib.auth import views as auth_views, login, get_user_model
from django.shortcuts import render

from grocery_store.user_profile.forms import RegisterUserForm, LoginUserForm

UserModel = get_user_model()


# Create your views here.
class OnlyAnonymousMixins:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse(self.get_success_url())

        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(OnlyAnonymousMixins, views.CreateView):
    template_name = 'user_profile/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        # if 'next' in self.request.POST:
        #     return self.request.POST['next']
        # return self.success_url

        return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    template_name = 'user_profile/login-page.html'
    form_class = LoginUserForm

    # success_url = ''
    # def get_success_url(self):


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    template_name = 'user_profile/profile-details-page.html'
    model = UserModel

    profile_image = static('images/person.png')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile_image'] = self.get_profile_image()

        return context


class ProfileEditView(views.UpdateView):
    model = UserModel
    template_name = 'user_profile/profile-edit-page.html'
    fields = ('first_name', 'last_name', 'gender', 'profile_picture')

    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('profile details', kwargs={'pk': pk})


# @method_decorator(login_required, name='dispatch')
class ProfileDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'user_profile/profile-delete-page.html'
    success_url = reverse_lazy('profile_list')
