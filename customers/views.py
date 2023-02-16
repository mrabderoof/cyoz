from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

from django.core.paginator import Paginator
from customers.filters import ProfileFilter

from customers.forms import ProfileForm, form_validation_error
from customers.models import Profile


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'customers/profile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.zite = form.cleaned_data.get('zite')
            profile.user.slug = form.cleaned_data.get('slug')

            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('profile')

# def profiles(request):
#     story_list = Profile.objects.order_by('user')
#     story_filter = ProfileFilter(request.GET, queryset=story_list)

#     paginator = Paginator(story_filter.qs, 10)

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = { "page_obj": page_obj, "filter": story_filter, 'value':'profiles'}

# return render(request, "views/profiles.html", context)

def profile_view(request, slug):
    context = {}
    # content = Profile.objects.get(slug=slug)
    # context = { "data": content }
    return render(request, "views/profile_detail_view.html", context)
