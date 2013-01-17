from django.db import models
from django.db.models.fields import CharField
import datetime


class DynSettings(models.Model):
    name = CharField(max_length=100)
    value = CharField(max_length=500, blank=True)
    type = CharField(max_length=20, blank=True, default="NoneType")

    class Meta:
        verbose_name = u"DynSetting"
        verbose_name_plural = u"DynSettings"

    def __unicode__(self):
        return self.name

    def get(self):
        if(self.type == 'str'):
            return self.value
        elif(self.type == 'int'):
            return int(self.value)
        elif(self.type == 'float'):
            return float(self.value)
        elif(self.type == 'NoneType'):
            return None
        elif(self.type == 'bool'):
            return self.value == 'True'
        elif(self.type == 'datetime'):
            return datetime.datetime.strptime(self.value, '%d/%m/%Y %H:%M:%S')
        elif(self.type == 'unicode'):
            return unicode(self.value)

    def set(self, value):
        t = type(value).__name__
        if t not in ['str', 'unicode', 'int', 'float', 'datetime', 'bool', 'NoneType']:
            raise Exception("Type not supported by dynsettings")
        self.type = t
        if (self.type == "datetime"):
            self.value = value.strftime('%d/%m/%Y %H:%M:%S')
        else:
            self.value = str(value)
        self.save()


class _Config:
    def __setitem__(self, key, value):
        s = DynSettings.objects.get_or_create(name=key)
        s[0].set(value)

    def __getitem__(self, key):
        s = DynSettings.objects.get_or_create(name=key)
        return s[0].get()


config = _Config()

#if ('DYNSETTINGS_CONFIGS' in dir(settings)):
#    d = settings.DYNSETTINGS_CONFIGS
#    for v, k in d.items():
#        config[k] = v
