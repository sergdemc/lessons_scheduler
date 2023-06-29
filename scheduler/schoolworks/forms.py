from django import forms
from .models import SchoolWork


class SignUpLessonForm(forms.ModelForm):
    TYPE_CHOICES = (
        ('lesson', 'Lessons'),
        ('consultation', 'Consultation'),
    )

    TIME_CHOICES = (
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['telegram_id'].initial = user.telegram_id

    telegram_id = forms.CharField(
        label='Your Telegram ID',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
    )
    type_sw = forms.ChoiceField(
        label='Type of schoolwork: for lessons min 4 hours, for consultation min 1 hour',
        choices=TYPE_CHOICES,
        widget=forms.RadioSelect
    )
    date_sw = forms.DateField(
        label='Date: Only Monday - Friday',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    time_sw = forms.ChoiceField(
        label='Time',
        choices=TIME_CHOICES,
        widget=forms.Select()
    )

    def clean_time_sw(self):
        time = self.cleaned_data['time_sw']
        if time not in [choice[0] for choice in self.TIME_CHOICES]:
            raise forms.ValidationError('Invalid time selected.')
        return time

    class Meta:
        model = SchoolWork
        fields = ['telegram_id', 'type_sw', 'date_sw', 'time_sw']
