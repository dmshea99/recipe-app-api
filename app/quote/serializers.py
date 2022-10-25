from rest_framework import serializers

from core.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Quote
        fields = ['id', 'author', 'text', 'tag1']
        read_only_fields = ['id']


class QuoteDetailSerializer(QuoteSerializer):
    """Serialzier for quote detail view."""
    class Meta(QuoteSerializer.Meta):
        fields = QuoteSerializer.Meta.fields + ['description',
                                                'link', 'tag2']
