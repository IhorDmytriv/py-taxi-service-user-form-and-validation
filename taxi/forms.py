from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from taxi.models import Driver


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "license_number", )


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number", )

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != 8:
            raise ValidationError("License number must consist of exactly 8 characters.")

        elif not license_number[:3].isalpha() or not license_number[:3].isupper():
            raise ValidationError("The first 3 characters must be uppercase letters.")

        elif not license_number[-5:].isdigit():
            raise ValidationError("The last 5 characters must be digits.")

        return license_number