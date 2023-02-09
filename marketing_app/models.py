
from django.db import models
# Create your models here.
import uuid
FILES_LOCATION_EMAIL_MEDIA = 'email_category/'



class BaseModelMixin(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    modification_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def change_uuid(self):
        self.uuid = uuid.uuid4()
        return self.uuid

    class Meta:
        abstract = True


class MarketingAccessCode(BaseModelMixin):
    """ 
        Model for marketing access code.
    """
    access_code_id = models.AutoField(primary_key=True, null=False)
    access_code = models.CharField(max_length=6, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Marketing Code UUID : {self.uuid} -> Access Code : {self.access_code} -> Status : {self.is_active}"


class EmailCategory(BaseModelMixin):
    """
        Model for email category
    """
    email_category_id = models.AutoField(primary_key=True, null=False)
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(
        upload_to=FILES_LOCATION_EMAIL_MEDIA, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Email Category UUID : {self.uuid} -> Category Name : {self.category_name}"


class EmailMarketing(BaseModelMixin):
    """
        Model for email marketing.
    """
    email_marketing_id = models.AutoField(primary_key=True, null=False)
    email_category = models.ForeignKey(
        EmailCategory, on_delete=models.DO_NOTHING, blank=True, null=True)
    email = models.EmailField(
        max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return f"Email UUID : {self.uuid} -> Email: {self.email} -> Category : {self.email_category}"
