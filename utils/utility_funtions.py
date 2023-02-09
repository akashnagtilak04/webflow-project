from rest_framework.response import Response

def custom_response(status,  data={}, error=True, message='', is_pagination=False):
    if not is_pagination:
        return Response({'status_code': status, "error": error, 'data': data, 'message': message}, status=status)
    return Response({'status_code': status, "error": error, **data, 'message': message}, status=status)
