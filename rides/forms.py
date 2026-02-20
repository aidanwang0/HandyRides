from django import forms


class RideForm(forms.Form):
    """Search form for finding registrants by state and optionally by city."""
    state = forms.CharField(
        label='State (2-letter abbreviation)',
        max_length=2,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. NY (where from), NJ (destination)'})
    )
    city = forms.CharField(
        label='City',
        max_length=64,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Brooklyn, Princeton'})
    )
