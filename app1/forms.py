from django import forms
from .models import CarouselItem, FeaturedItem, Testimonial


class CarouselItemForm(forms.ModelForm):
    class Meta:
        model = CarouselItem
        fields = ['title', 'description', 'image']

class FeaturedItemForm(forms.ModelForm):
    class Meta:
        model = FeaturedItem
        fields = ['title', 'description', 'image']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'quote', 'image']

class CarouselItemForm(forms.ModelForm):
    is_featured = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        required=False,
        initial=False,
        label='Is Featured'
    )

    class Meta:
        model = CarouselItem
        fields = ['title', 'image', 'description', 'is_active', 'is_featured']

