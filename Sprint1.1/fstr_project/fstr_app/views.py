from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .data_handler import DataHandler

class SubmitDataView(APIView):
    def post(self, request):
        data = request.data

        # Проверка наличия необходимых полей
        required_fields = ['beauty_title', 'title', 'coords', 'user', 'level', 'images']
        for field in required_fields:
            if field not in data:
                return Response({
                    "status": 400,
                    "message": f"Поле {field} отсутствует.",
                    "id": None
                }, status=status.HTTP_400_BAD_REQUEST)

        try:
            pereval_id = DataHandler.submit_data(data)
            return Response({
                "status": 200,
                "message": None,
                "id": pereval_id
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": 500,
                "message": str(e),
                "id": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

