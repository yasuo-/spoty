from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from betterforms.multiform import MultiModelForm

from .models import Profile

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        )


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio",)


class ProfileAvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("avatar",)


class UserEditMultiForm(MultiModelForm):
    form_classes = {
        'avatar': ProfileAvatarForm,
        'user': UserEditForm,
        'profile': UserProfileForm,
    }
