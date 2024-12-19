from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import CustomUser, Project, AvailableFor, Category, FieldResearch, ProjectGroup, ProjectApplyDetail

class CustomUserCreationForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('coordinator', 'Coordinator'),
        ('supervisor', 'Supervisor'),
    )
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "user_type")

    def save(self):
        user = super().save(commit=False)
        user_type = self.cleaned_data['user_type']

        if user_type == 'student':
            user.is_student = True
        elif user_type == 'coordinator':
            user.is_coordinator = True
        elif user_type == 'supervisor':
            user.is_supervisor = True

        user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "is_student", "is_student", "is_coordinator", "is_supervisor")



class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput())


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['available_for'].queryset = AvailableFor.objects.all()
        self.fields['categories'].queryset = Category.objects.all()
        self.fields['fields_of_research'].queryset = FieldResearch.objects.all()

    class Meta:
        model = Project
        fields = ['topic_number','title', 'description', 'available_for', 'categories', 'fields_of_research']


class ProjectGroupForm(forms.ModelForm):
    class Meta:
        model = ProjectGroup
        fields = ['name']


class ProjectApplyDetailForm(forms.ModelForm):
    class Meta:
        model = ProjectApplyDetail
        fields = ['why_interested', 'relevant_skills', 'how_to_contribute']