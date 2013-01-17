# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from dynsettings.models import DynSettings
from dynsettings.tools import parse_value


class DynSettingsAdminForm(forms.ModelForm):
    data = forms.CharField(max_length=502)

    def __init__(self, *args, **kwargs):
        super(DynSettingsAdminForm, self).__init__(*args, **kwargs)
        self.fields['value'].widget.attrs['disabled'] = True
        self.fields['type'].widget.attrs['disabled'] = True

    def clean_data(self):
        d = self.cleaned_data.get("data")

        d = parse_value(d)
        if (not d):
            raise forms.ValidationError("Invalid data format. Try python format values.")
        else:
            self.cleaned_data['type'] = d[0]
            self.cleaned_data['value'] = d[1]
        return d

    class Meta:
        model = DynSettings


class DynSettingsAdmin(admin.ModelAdmin):
    form = DynSettingsAdminForm


admin.site.register(DynSettings, DynSettingsAdmin)
