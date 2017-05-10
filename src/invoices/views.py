from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Invoice, InvoiceEntry
from .serializers import InvoiceSerializer, InvoiceEntrySerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'invoices': reverse('invoice-list', request=request, format=format),
    })


class InvoiceList(generics.ListCreateAPIView):
    """
    List all the invoices (GET) or create a new one (POST)
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a invoice instance.
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceEntryList(generics.ListCreateAPIView):
    """
    List all the invoices (GET) or create a new one (POST)
    """

    queryset = InvoiceEntry.objects.all()
    serializer_class = InvoiceEntrySerializer


class InvoiceEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an entry for an invoice.
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceEntrySerializer
