from rest_framework import serializers
from .models import FortuneCookie, Poem, Author, Theme

class FortuneCookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FortuneCookie
        fields = '__all__'

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'
