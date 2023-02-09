from rest_framework import serializers
from marketing_app.models import MarketingAccessCode, EmailMarketing, EmailCategory

# MarketingAccessCode

MARKETING_ACCESS_CODE_FIELD_UUID = 'uuid'
MARKETING_ACCESS_CODE_FIELD_ACCESS_CODE_ID = 'access_code_id'
MARKETING_ACCESS_CODE_FIELD_ACCESS_CODE = 'access_code'
MARKETING_ACCESS_CODE_FIELD_IS_ACTIVE = 'is_active'

# EmailMarketing
EMAIL_MARKETING_FIELD_UUID = 'uuid'
EMAIL_MARKETING_FIELD_EMAIL = 'email'
EMAIL_MARKETING_FIELD_EMAIL_CATEGORY = 'email_category'

# EmailCategory
EMAIL_CATEGORY_FIELD_UUID = 'uuid'
EMAIL_CATEGORY_FIELD_CATEGORY_NAME = 'category_name'



class MarketingAccessCodeSerializer(serializers.ModelSerializer):
    """
        Serializer for marketing access code.
    """
    class Meta:
        model = MarketingAccessCode
        fields = [MARKETING_ACCESS_CODE_FIELD_UUID,
                  MARKETING_ACCESS_CODE_FIELD_ACCESS_CODE]


class EmailMarketingSerializer(serializers.ModelSerializer):
    """
        Serializer for email marketing.
    """
    class Meta:
        model = EmailMarketing
        fields = '__all__'


class EmailMarketingGETSerializer(serializers.ModelSerializer):
    """
        Serializer for email marketing.
    """
    class Meta:
        model = EmailMarketing
        fields = (EMAIL_MARKETING_FIELD_EMAIL, EMAIL_MARKETING_FIELD_UUID)


class EmailCategorySerializer(serializers.ModelSerializer):
    """
        Serializer for email category
    """
    class Meta:
        model = EmailCategory
        fields = (EMAIL_CATEGORY_FIELD_UUID,
                  EMAIL_CATEGORY_FIELD_CATEGORY_NAME)
