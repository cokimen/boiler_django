from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from django.db.models import QuerySet
from .serializers import AnonSerializer
from rest_framework.response import Response
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


class AnonViewSet(viewsets.ModelViewSet):

    queryset = [QuerySet()]
    serializer_class = AnonSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def reverse_action(self, url_name, *args, **kwargs):
        return super().reverse_action(url_name, *args, **kwargs)

    @action(methods=['GET'], detail=False)
    def trial_template(self, request, *args, **kwargs):
        di = "dimski marbroto"
        content = "<html>{dien}</html>".format(dien=di)
        buffer = io.BytesIO()

        p = canvas.Canvas(buffer)
        p.drawString(100, 100, content)

        p.showPage()
        p.save()
        buffer.seek(0)

        return FileResponse(buffer, as_attachment=False, filename='hello.pdf')

    @action(methods=['GET'], detail=False)
    def coki(self, request, *args, **kwargs):

        template = get_template("file1.html")
        html = template.render({"a": "a"})
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None
    # return Response({"a": content})
