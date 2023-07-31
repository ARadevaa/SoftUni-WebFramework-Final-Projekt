from django.urls import path, include

from grocery_store.user_profile.views import RegisterUserView, LoginUserView, LogoutUserView, ProfileDetailsView, \
    ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register user"),
    path('login/', LoginUserView.as_view(), name="login user"),
    path('logout/', LogoutUserView.as_view(), name="logout user"),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile details'),
        path('edit/', ProfileEditView.as_view(), name='profile edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile delete')
    ]))
]