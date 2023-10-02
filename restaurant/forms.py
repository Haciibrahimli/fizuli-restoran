from django import forms
from restaurant.models import Contact, Reserve


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("created_at", "updated_at", "slug")

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)


        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

        self.fields["name_and_surname"].widget.attrs.update({"placeholder": "your name and surname"})
        self.fields["subject"].widget.attrs.update({"placeholder": "subject"})
        self.fields['message'].widget.attrs.update({"placeholder": "Your message", "style": "height:150px"})
        self.fields["email"].widget.attrs.update({"placeholder": "your email"})


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        exclude = ("created_at", "updated_at", "slug")
        
    def __init__(self, *args, **kwargs):
        super(ReserveForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class":  "form-control"})


        self.fields["reserve_date"].widget.attrs.update({"class":  "form-control datetimepicker-input", 
                                                        
                                                        "placehold": "Reservasiya vaxti"})
        self.fields["name"].widget.attrs.update({"placeholder":  "Adiniz"})
        self.fields["name"].label = "Adiniz"
        self.fields["phone_number"].widget.attrs.update({"placeholder":  "Elaqe nomreniz"})
        self.fields["phone_number"].label = "Elaqe nomreniz"
        self.fields["count_of_guest"].widget.attrs.update({"placeholder":  "Qonaq sayi"})
        self.fields["count_of_guest"].label = "Qonaq sayi"
        self.fields["special_message"].widget.attrs.update({"placeholder":  "Xususi mesajiniz"})
        self.fields["special_message"].label = "Xususi mesajiniz"
