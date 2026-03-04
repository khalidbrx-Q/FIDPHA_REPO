from django.contrib import admin

from .legacy_models import Sells
# Register your models here.

from .models import Client,Product,Contract,ContractProduct

# Register your models here.



admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Contract)
admin.site.register(ContractProduct)
admin.site.register(Sells)