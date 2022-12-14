"""Views for the recipe APIs."""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Quote
from quote.serializers import (
                        QuoteSerializer,
                        QuoteDetailSerializer
)


class QuoteViewSet(viewsets.ModelViewSet):
    """View for managing quote APIs."""
    serializer_class = QuoteDetailSerializer
    queryset = Quote.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return QuoteSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new quote. """
        serializer.save(user=self.request.user)
