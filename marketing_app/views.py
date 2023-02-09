from rest_framework.generics import GenericAPIView
from rest_framework import status
from .models import *
from .serializer import *
from utils.utility_funtions import *
from utils.messages import *
import requests
from django.http import HttpResponse
import json

# Create your views here.
class CheckAccessCodeAPI(GenericAPIView):
    """
        API for Access code checking
    """

    # model = MarketingAccessCode
    # serializer_class = MarketingAccessCodeSerializer
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        """
            URL : POST api/check-access-code/

            Sample Request :
            {
                "access_code":"RN6ZIE"
            }

            Sample Response : 
            {
                "status_code": 200,
                "error": false,
                "data": {
                    "uuid": "2162fb44-32c6-4ec3-9f79-2e1b555bf8e1",
                    "access_code": "RN6ZIE"
                },
                "message": "valid access code"
            }
        """
        data = request.data
        endpoint = 'http://ec2-3-22-222-168.us-east-2.compute.amazonaws.com/api/check-access-code/'
        payload = {'otp': data.get('otp')}
        response = requests.post(endpoint, json=payload)
        if response.status_code == 200:
            data = response.json()
        else:
            response.headers["content-type"].strip().startswith("application/json")
            data = response.json()
        
        return HttpResponse(json.dumps(data), content_type='application/json')
        # data = request.data

        # try:
        #     access_code = self.model.objects.get(
        #         access_code__exact=data.get('otp'))
        # except Exception:
        #     return custom_response(status.HTTP_200_OK, error=False, message=MarketingAccessCodeMessages.ERROR_PLEASE_ENTER_VALID_ACCESS_CODE)
        # access_code_serializer = self.serializer_class(access_code)
        # return custom_response(status.HTTP_200_OK, access_code_serializer.data, error=False, message=MarketingAccessCodeMessages.SUCCESS_VALID_ACCESS_CODE)


class AddMarketingEmailAPI(GenericAPIView):
    """
        API for add email marketing.
    """
    # model = EmailMarketing
    # serializer_class = EmailMarketingSerializer
    # serializer_class_get = EmailMarketingGETSerializer
    # This need in future. Please keep this.
    # permission_classes = (partial(GuestPrivacyTokenPermission), ['POST'])
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        data = request.data
        endpoint = 'http://ec2-3-22-222-168.us-east-2.compute.amazonaws.com/api/add-marketing-email/'
        payload = {'email': data.get('email')}
        response = requests.post(endpoint, json=payload)
        print(response)
        if response.status_code == 200:
            data = response.json()
        else:
            response.headers["content-type"].strip().startswith("application/json")

            data = response.json()
        
        return HttpResponse(json.dumps(data), content_type='application/json')
        # data = request.data
        # email_category = data.get(EMAIL_MARKETING_FIELD_EMAIL_CATEGORY, None)

        # if email_category:
        #     email_category, _ = EmailCategory.objects.get_or_create(
        #         category_name=email_category)
        #     data[EMAIL_MARKETING_FIELD_EMAIL_CATEGORY] = email_category.email_category_id

        # email_category_serializer = self.serializer_class(data=data)
        # if email_category_serializer.is_valid(raise_exception=True):
        #     email_category_serializer.save()
        #     return custom_response(status.HTTP_200_OK, email_category_serializer.data, error=False, message=EmailMarketingMessages.SUCCESS_EMAIL_CREATED)


