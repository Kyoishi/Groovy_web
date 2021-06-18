from django import forms
from django.contrib import admin

from .models import Author, Book, Publisher


class BookAdminForm(forms.ModelForm):
    def clean_title(self):
        value = self.cleaned_data['title']
        if 'Django' not in value:
            raise forms.ValidationError(
                "タイトルには「Django」という文字を含めてください")
        return value


class BookAdmin(admin.ModelAdmin):
    # list_display = ('title', 'publisher', 'price')
    # ordering = ('-price',)
    # form = BookAdminForm
    fields = ('title', 'price', 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
