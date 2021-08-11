from .models import Game, Review
from rest_framework import serializers



class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.HyperlinkedRelatedField(
        view_name='game_detail', read_only=True
        )
    game_name = serializers.SlugRelatedField(
        queryset=Game.objects.all(), slug_field='title', source='game'
        )
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'game', 'game_name', 'title', 'body', 'created', 'owner',)

class GameSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True,
        view_name='review_list'
    )

    game_url = serializers.ModelSerializer.serializer_url_field(
        view_name='game_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Game
        fields = ('id', 'title', 'genre', 'release_date', 'rating', 'preview_url', 'owner', 'reviews', 'game_url')
    