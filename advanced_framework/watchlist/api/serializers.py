from rest_framework import serializers
from ..models import WatchList, StreamPlatform


# Model Serializer
class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):
    # This return the everythin
    # watchlist = WatchListSerializer(many=True, read_only=True)

    # This utilises the watchlist model __str__ function which in  this case returns name
    # watchlist = serializers.StringRelatedField(many=True)

    # This returns the primary Key
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # This allows you to return the id of the watchlist as url
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watchlist_details')

    # This allows you to choose the field of the watchlist you want to return
    watchlist = serializers.SlugRelatedField(many=True, read_only=True, slug_field='storyline')

    class Meta:
        model = StreamPlatform
        fields = '__all__'
