from django import forms
from django.contrib.auth.forms import UserCreationForm
from LMS.models import Labour,Trades,User

class labourregisterform(UserCreationForm):
    trade = forms.ModelChoiceField(
        queryset=Trades.objects.all(),
        widget=forms.RadioSelect,
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'trade')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_labour = True
        if commit:
            user.save()
            labour = Labour.objects.create(user=user, trade=self.cleaned_data['trade'])
        return user
    


class Managerregisterform(UserCreationForm):
      class Meta(UserCreationForm.Meta):
        model = User
    

      def save(self, commit=True):
        user = super().save(commit=False)
        user.is_Manager = True
        if commit:
            user.save()
        return user