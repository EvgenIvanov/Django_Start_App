from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _

# from django.contrib import admin
# from django.utils.translation import ugettext_lazy as _
# from .models import Order
# from django.core.urlresolvers import reverse

# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

# from django.contrib import admin
# from django.contrib.flatpages.admin import FlatPageAdmin
# from django.contrib.flatpages.models import FlatPage
# from django.utils.translation import gettext_lazy as _

# # Define a new FlatPageAdmin
# class FlatPageAdmin(FlatPageAdmin):
#     fieldsets = (
#         (None, {'fields': ('url', 'title', 'content', 'sites')}),
#         (_('Advansed options'), {
#             'classes': ('collapse',),
#             'fields': (
#                 'enabled_comments',
#                 'registration_required',
#                 'template_name',
#             ),
#         }),
#     )

# # Re-register FlatPageAdmin
# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, FlatPageAdmin)