from rest_framework.views import APIView, Response
from projeto.models import Profissional, Job
from projeto.serializer import ProfissionalSerializer, CadastrarJobSerializer, JobSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

class ProfissionalAPI(APIView):
    def get(self, request, format=None):
        profissionais = Profissional.objects.all()
        serializer = ProfissionalSerializer(profissionais, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
class CadastrarJobAPI(APIView):
    def post(self, request, id, format=None):
        profissional = get_object_or_404(Profissional, id=id)
        serializer = CadastrarJobSerializer(data=request.data)
        if serializer.is_valid():
            job = Job(
                nome = serializer.validated_data.get('nome'),
                email = serializer.validated_data.get('email'),
                profissional = profissional
            )
            job.save()
            job_serializer = JobSerializer(job, many=False)
            return Response(
                job_serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=HTTP_400_BAD_REQUEST
        )