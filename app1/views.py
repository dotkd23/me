from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CarouselItem, FeaturedItem, Testimonial
from .forms import CarouselItemForm, FeaturedItemForm, TestimonialForm
from django.contrib.auth import logout
from django.views import View

def home_view(request):
    carousel_items = CarouselItem.objects.all()
    return render(request, 'home.html', {'carousel_items': carousel_items})

def carousel_items(request):
    if request.method == 'POST':
        # Delete all carousel items
        CarouselItem.objects.all().delete()
        messages.success(request, 'All carousel items have been deleted.')
        return redirect('app1:carousel_items')

    if request.method == 'POST' and 'make_featured' in request.POST:
        # Get carousel item ID from form
        carousel_item_id = request.POST.get('carousel_item_id')
        carousel_item = get_object_or_404(CarouselItem, id=carousel_item_id)

        # Create a new FeaturedItem from the carousel item
        featured_item = FeaturedItem(
            image=carousel_item.image,
            title=carousel_item.title,
            description=carousel_item.description,
            link=carousel_item.link
        )
        featured_item.save()

        messages.success(request, 'Carousel item has been made a featured item.')
        return redirect('app1:carousel_items')

    carousel_items = CarouselItem.objects.all()
    return render(request, 'carousel_items.html', {'carousel_items': carousel_items})

def make_featured(request):
    if request.method == 'POST':
        carousel_item_id = request.POST.get('carousel_item_id')
        carousel_item = CarouselItem.objects.get(id=carousel_item_id)
        featured_item = FeaturedItem()
        featured_item.title = carousel_item.title
        featured_item.image = carousel_item.image
        featured_item.save()
        carousel_item.featured = True
        carousel_item.save()
        return redirect('app1:carousel_items')

def featured_items(request):
    featured_items = FeaturedItem.objects.all()
    if not featured_items:
        message = "There are unfortunately no items that are being featured at the moment"
        return render(request, 'featured_items.html', {'message': message})
    return render(request, 'featured_items.html', {'featured_items': featured_items})

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials})

def featured_item_detail(request, pk):
    featured_item = get_object_or_404(FeaturedItem, pk=pk)
    # Update the context variables as needed for your template
    context = {
        'featured_item': featured_item
    }
    return render(request, 'featured_item_detail.html', context)

class CarouselItemDetailView(View):
    def get(self, request, pk):
        carousel_item = get_object_or_404(CarouselItem, pk=pk)
        return render(request, 'carousel_item_detail.html', {'carousel_item': carousel_item})

def testimonial_detail(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    return render(request, 'testimonial_detail.html', {'testimonial': testimonial})

def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonial_list.html', {'testimonials': testimonials})

def carousel_item_create(request):
    if request.method == 'POST':
        form = CarouselItemForm(request.POST, request.FILES)
        if form.is_valid():
            carousel_item = form.save(commit=False)
            carousel_item.user = request.user 
            # Set is_featured field based on user input
            is_featured = request.POST.get('is_featured') == 'on'
            carousel_item.is_featured = is_featured
            carousel_item.save()
            messages.success(request, 'Carousel item has been created.')
            return redirect('app1:home')  # Redirect to homepage
    else:
        form = CarouselItemForm()
    return render(request, 'carousel_item_create.html', {'form': form})

def featured_item_create(request):
    form = FeaturedItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('featured_items')
    return render(request, 'featured_item_form.html', {'form': form})

def testimonial_create(request):
    form = TestimonialForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    return render(request, 'testimonial_form.html', {'form': form})

def carousel_item_update(request, pk):
    carousel_item = get_object_or_404(CarouselItem, pk=pk)
    form = CarouselItemForm(request.POST or None, request.FILES or None, instance=carousel_item)
    if form.is_valid():
        form.save()
        return redirect('carousel_items')
    return render(request, 'carousel_item_form.html', {'form': form})

def featured_item_update(request, pk):
    featured_item = get_object_or_404(FeaturedItem, pk=pk)
    form = FeaturedItemForm(request.POST or None, request.FILES or None, instance=featured_item)
    if form.is_valid():
        form.save()
        return redirect('featured_items')
    return render(request, 'featured_item_form.html', {'form': form})

def testimonial_update(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    form = TestimonialForm(request.POST or None, request.FILES or None, instance=testimonial)
    if form.is_valid():
        form.save()
        return redirect('testimonials')
    return render(request, 'testimonial_form.html', {'form': form})

def carousel_item_delete(request, pk):
    carousel_item = get_object_or_404(CarouselItem, pk=pk)
    if request.method == 'POST':
        carousel_item.delete()
        return redirect('carousel_items')
    return render(request, 'carousel_item_confirm_delete.html', {'carousel_item': carousel_item})

def featured_item_delete():
    pass

def logout_view(request):
    logout(request)
    # Redirect to the desired URL after logout
    return redirect('app1:home') 