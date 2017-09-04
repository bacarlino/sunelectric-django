from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Submit
from phonenumber_field import formfields as phone_forms
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    phone = phone_forms.PhoneNumberField(
        max_length=15,
        widget=PhoneNumberInternationalFallbackWidget,
        required=False
    )
    company = forms.CharField(max_length=50, required=False)
    message = forms.CharField(
        max_length=5000,
        widget=forms.Textarea,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout (
            Div(
                'name',
                'email',
                'phone',
                'company',
                css_class="col-md-offset-2 col-md-4"
            ),
            Div(
                'message',
                Submit('submit', 'Submit'),
                css_class="col-md-4"
            )
        )
        # self.helper.add_input(Submit('submit', 'Submit'))

        self.fields['phone'].widget.attrs.update({
            'pattern': '^([0-9]( |-)?)?(\(?[0-9]{3}\)?|[0-9]{3})( |-)?([0-9]{3}( |-)?[0-9]{4}|[a-zA-Z0-9]{7})$'
        })
