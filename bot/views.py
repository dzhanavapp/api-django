from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from bot.bot import chatbot_response


class BotAPIView(APIView):

    def get(self, request, *args, **kwargs):
        if request.query_params.get('msg'):
            msg = chatbot_response(request.query_params.get('msg'))
            return Response(msg)
        return Response(status=status.HTTP_400_BAD_REQUEST)