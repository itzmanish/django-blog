from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2',)

    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs['class'] = 'form-control'
    #     self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
    #     self.fields['first_name'].label = ""
        # self.fields['last_name'].widget.attrs['class'] = 'form-control'
    #     self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
    #     self.fields['last_name'].label = ""
        # self.fields['username'].widget.attrs['class'] = 'form-control'
    # self.fields['username'].widget.attrs['placeholder'] = 'Username'
    #     self.fields['username'].label = ""
    #     self.fields['username'].help_text = '<div class="form-group"><small class="form-text text-muted">Required. less than 15 words.. excluding @/./+/-</small></div>'
        # self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    #     self.fields['password1'].label = ""
    #     self.fields['password1'].help_text = '<div class="form-group"><small class="form-text text-muted"><ul><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul></small></div >'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    #     self.fields['password2'].label = ""
    #     self.fields['password2'].help_text = '<div class="form-group"><small class="form-text text-muted">Enter the same password as before, for verification.</small></div>'
