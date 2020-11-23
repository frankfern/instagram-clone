#django
from django.contrib import admin


#project
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Post Admin"""
    list_display = (
        'pk','user','profile',
        'title','photo'
    )

    list_display_links= ('pk','user','profile')

    list_editable = (
        'photo',
    )

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'title'
    )

    list_filter = (
        'created',
        'modified',  
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user','profile'),
                
            ),
        }),
        ('Content',{
            'fields': ('title','photo')

        }),
        ('Metadata',{
            'fields': ('created','modified'),
        }),
    )
    readonly_fields = ('created','modified')