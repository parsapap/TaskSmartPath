import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TestAPIView(APIView):
    def post(self, request, number):
        # Get the 'id' from request headers
        header_id = request.headers.get('id')
        if not header_id:
            return Response({"message": "id not provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the 'id' is a valid UUID
        try:
            header_id = uuid.UUID(header_id)
        except ValueError:
            return Response({"message": "Invalid UUID"}, status=status.HTTP_400_BAD_REQUEST)

        # Get the body data from the request (JSON array)
        body_data = request.data
        matched_objects = []

        for obj in body_data:
            try:
                if str(obj['BodyId']) == str(header_id) and str(obj['BodyIdNumber']) == str(number):
                    matched_objects.append(obj)
            except KeyError:
                return Response({"message": "Invalid data structure"}, status=status.HTTP_400_BAD_REQUEST)

        if matched_objects:
            return Response(matched_objects, status=status.HTTP_200_OK)
        else:
            return Response({"message": "not found"}, status=status.HTTP_404_NOT_FOUND)
