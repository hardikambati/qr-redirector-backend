from django.db.models import Q
from rest_framework import (
    views,
    response,
    status,
    permissions,
)

# custom
from websockets.utility import send_message_to_channel


class RedirectWebhookAPIView(views.APIView):
    """
    Accepts external requests in form of webhook
    Sends a redirect message to websocket that was already opened
    """

    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        data = request.data
        token = data.get('token')
        if not token:
            return response.Response({'detail': 'Token not passed in request body'}, status=status.HTTP_400_BAD_REQUEST)
        
        send_message_to_channel(
            token=token,
            message={
                'status': 'redirect'
            }
        )
        return response.Response({'detail': 'success'}, status=status.HTTP_200_OK)
        