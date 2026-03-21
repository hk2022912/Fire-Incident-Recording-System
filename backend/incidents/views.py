from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Personnel, Incident
from .serializers import PersonnelSerializer, IncidentSerializer


@api_view(['GET'])
def personnel_list(request):
    return Response(PersonnelSerializer(Personnel.objects.all(), many=True).data)


@api_view(['PATCH'])
def personnel_detail(request, slot):
    try:
        person = Personnel.objects.get(slot=slot)
    except Personnel.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=404)
    s = PersonnelSerializer(person, data=request.data, partial=True)
    if s.is_valid():
        s.save()
        return Response(s.data)
    return Response(s.errors, status=400)


@api_view(['GET', 'POST'])
def incident_list(request):
    if request.method == 'GET':
        return Response(IncidentSerializer(Incident.objects.all(), many=True).data)
    s = IncidentSerializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data, status=201)
    return Response(s.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def incident_detail(request, pk):
    try:
        incident = Incident.objects.get(pk=pk)
    except Incident.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=404)
    if request.method == 'GET':
        return Response(IncidentSerializer(incident).data)
    if request.method == 'PUT':
        s = IncidentSerializer(incident, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=400)
    incident.delete()
    return Response(status=204)


@api_view(['POST'])
def incident_bulk(request):
    rows = request.data
    if not isinstance(rows, list) or len(rows) == 0:
        return Response({'detail': 'Send a non-empty JSON array.'}, status=400)
    created, errors = [], []
    for i, row in enumerate(rows):
        s = IncidentSerializer(data=row)
        if s.is_valid():
            obj = s.save()
            created.append(IncidentSerializer(obj).data)
        else:
            errors.append({'row': i + 1, 'errors': s.errors})
    return Response({'created': created, 'errors': errors}, status=201 if created else 400)