from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Test

class TestAdminForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

class TestAdmin(admin.ModelAdmin):
    form = TestAdminForm

admin.site.register(Test, TestAdmin)