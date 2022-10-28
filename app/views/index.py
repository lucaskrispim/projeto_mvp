from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
import threading

def main():
    print('Hello ...')
    time.sleep(10)
    print('... World!')

# Create your views here.

def index_view(request):
    return render(request, 'index.html')


class Index(APIView):
    def get(self, request, format=None):
        return Response(
            {
                "msg": "Ok estamos no ar",
            },
            status=status.HTTP_200_OK)

    def post(self, request, format=None):

        #main()
        th = threading.Thread(target=main)
        th.start()
        
        print(request.user.id)

        return Response(
            {
                "msg": "Ok estamos no arrrr",
            },
            status=status.HTTP_200_OK)
