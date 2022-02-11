from unicodedata import category
from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from . models import *
from django.urls import path
from . forms import *
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import View
from django.utils import render_to_pdf
from xhtml2pdf import pisa
# Register your models here.
""" def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None """
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'locality', 'city', 'state')
    list_filter = ('city', 'state')
    list_per_page = 10
    search_fields = ('locality', 'city', 'state')
    save_on_top = True
    class Meta:
        verbose_name_plural = "Address"
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','category_image','updated_at')
    #list_editable = ('slug', )
    list_filter = ('title',)
    list_per_page = 10
    search_fields = ('title', 'description')
    save_on_top = True
    #prepopulated_fields = {"slug": ("title", )}
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):
        #try:

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
                
            if not csv_file.name.endswith('.csv'):
                 messages.warning(request, 'The wrong file type was uploaded')
                 return HttpResponseRedirect(request.path_info)
                
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Category.objects.create(
                title=fields[0],
                description=fields[1],
                category_image=fields[2],

                        )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
            
        return render(request, "admin/csv_upload.html", data)
        """ except:
            return render(request, "admin/csv_upload.html", data) """

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'product_image','price', 'updated_at')#,'is_active','is_featured'
    list_editable = ('category', )
    list_filter = ('category',)
    list_per_page = 10
    search_fields = ('title', 'category', 'short_description')
    save_on_top = True
    #prepopulated_fields = {"slug": ("title", )}
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Product.objects.update_or_create(
                    title=fields[0],
                    sku=fields[1],
                    short_description=fields[2],
                    detail_description=fields[3],
                    product_image=fields[4],
                    price=fields[5],
                    #is_active=fields[7],
                    #is_featured=fields[8],
                    category=Category.objects.get(pk=(fields[6]))
                    #is_active=fields[5],
                    #category=fields[6],
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'ordered_date')
    list_editable = ('quantity', 'status')
    list_filter = ('status', 'ordered_date')
    list_per_page = 20
    search_fields = ('user', 'product')
    save_on_top = True

class AttributesAdmin(admin.ModelAdmin):
    list_display=('Product','Color','Size')
    list_filter=('Product','Color','Size')
    list_per_page = 20
    search_fields = ('Product','Color','Size')
    save_on_top = True

class salesAdmin(admin.ModelAdmin):
    list_display=('campaign_name','startdate','enddate')
    list_filter=('campaign_name','startdate','enddate')
    list_per_page = 20
    search_fields = ('campaign_name','startdate','enddate')
    save_on_top = True

admin.site.register(Order,OrderAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Attributes,AttributesAdmin)
admin.site.register(sales,salesAdmin)