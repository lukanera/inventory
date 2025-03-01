from rest_framework import serializers
from .models import Item, Category

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def validate_name(self, value):
        symbols = ['!@#$%^&*']
        if len(value) < 5: raise serializers.ValidationError('name must be at least 5 letters long')
        for i in symbols:
            if i in value['name']: raise serializers.ValidationError("name can't have symbols in it")
        return value

    def validate_description(self, value):
        split_value = value['description'].split()
        symbols = ['!@#$%^&*']
        if len(split_value) <2: raise serializers.ValidationError('description must have at least 2 words')
        for i in symbols:
            if i in value['name']: raise serializers.ValidationError("name can't have symbols in it")
        return value

    def validate_lengths(self, value):
        if value['width'] or value['lenth'] or value['weight'] or value['height'] <=0: raise serializers.ValidationError('width, length and weight can not be negative')
        return value

    def validate(self, data):
        print(data)
        return data
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Item
        fields = '__all__'