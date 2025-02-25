from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(["GET"])
@renderer_classes([JSONRenderer])
def healthcheck_view(request: Request) -> Response:
    return Response(data=dict(status="ok"), status=status.HTTP_200_OK)
