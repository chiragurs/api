from rest_framework.views import APIView
#response will be given from Response function
from rest_framework.response import Response

# Create your views here.
class SampleApiView(APIView):
    """The get method is responsible for handling the get requests"""
    def get(self,request,format=None):
        #always resposne should be in the form of dictionary
        return Response({'name':"SampleAPIview",'message':"Hello world"})

    def post(self,request,format=None):
        print(request.data)
        return Response({'message':request.data,"request_method":"post"})

    def put(self,request,format=None):
       return Response({'message':request.data,"request_method":"put"})

    def patch(self,request,format=None):
       return Response({'message':request.data,"request_method":"patch"})

    def delete(self,request,format=None):
       return Response({"request_method":"delete"})