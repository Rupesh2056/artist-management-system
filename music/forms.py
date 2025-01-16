from django import forms

from base.utils import BaseForm
from music.models import Artist

forms.ModelChoiceField

class AlbumCreateForm(BaseForm,forms.Form):
    title = forms.CharField()
    artist_id = forms.ChoiceField(choices = [],label="Artist")
    release_date = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d",
                               attrs={'type': 'date',
                                    #   'max': str((timezone.now() + timedelta(days=365)).date())
                                      },),
        help_text='Select a date',
        input_formats=["%Y-%m-%d"],
      
    )

    def __init__(self,*args,choices=None,**kwargs):
        super().__init__(*args,**kwargs)
        if choices:
            self.fields["artist_id"].choices = choices

class ArtistAlbumCreateForm(BaseForm,forms.Form):
    '''
    Used when creating by artist user.
    '''
    title = forms.CharField()
    release_date = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d",
                               attrs={'type': 'date',
                                    #   'max': str((timezone.now() + timedelta(days=365)).date())
                                      },),
        help_text='Select a date',
        input_formats=["%Y-%m-%d"],
      
    )


class MusicCreateForm(BaseForm,forms.Form):
    GENRE_CHOICES = (
        (None,"Select Genre"),
        ("rnb","RNB"),
        ("classic","Classic"),
        ("jazz","Jazz"),
        ("rock","Rock"),
        ("funk","Funk"),
        ("metal","Metal"),
    )
    title = forms.CharField()
    album_id = forms.ChoiceField(choices = [],label="Album")
    genre = forms.ChoiceField(choices=GENRE_CHOICES)

    def __init__(self,*args,choices=None,**kwargs):
        super().__init__(*args,**kwargs)
        if choices:
            self.fields["album_id"].choices = choices
