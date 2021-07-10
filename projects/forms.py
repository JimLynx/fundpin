from django import forms
from .widgets import CustomClearableFileInput
from .models import Project, Category, Country


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        countries = Country.objects.all()
        cat_friendly_names = [(c.id, c.get_friendly_name())
                              for c in categories]
        country_friendly_names = [
            (country.id, country.get_friendly_name()) for country in countries]

        self.fields['category'].choices = cat_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
        self.fields['country'].choices = country_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
