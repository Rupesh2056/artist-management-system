from base.utils import ExportMixin
from django.views import View

from user.views import ArtistListView

class ArtistExportView(ExportMixin, View):
    fields = [
        "SN",
        "email",
        "full_name",
        "Address",
        "Phone",
        "DOB",
        "Gender",
        "First Album Release Year",
        "Created at",
        "Updated at",
    ]

    def get_queryset(self, *args, **kwargs):
        return ArtistListView.get_artist_list_queryset(self.request)
    
    name = "Artists"

    def write_rows(self, writer, queryset):
        for index,object in enumerate(queryset):
            
      
            
            writer.writerow(
                [
                    index +1,
                    object.email,
                    object.full_name,
                    object.address,
                    object.phone,
                    object.dob,
                    object.gender,
                    object.artist_profile.first_album_release_year,
                    object.created_at.strftime("%d %b %Y, %I:%M %p"),
                    object.updated_at.strftime("%d %b %Y, %I:%M %p"),
                ]
            )