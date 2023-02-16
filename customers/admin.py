from django.contrib import admin

from customers.models import Gallery, Icon, Pricing, Profile, Services, Testimonial

admin.site.register(Gallery)
admin.site.register(Icon)
admin.site.register(Profile)
admin.site.register(Pricing)
admin.site.register(Services)
admin.site.register(Testimonial)
