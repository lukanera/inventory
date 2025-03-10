from rest_framework import serializers
from .models import Item, Category
from datetime import date

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    @staticmethod
    def check_symbols(value):
        symbols = ('!@#$%^&*')
        for s in symbols:
            if s in value:
                raise serializers.ValidationError(f"{value} can't have symbols in it")
        return value

    def validate_name(self, value):
        if len(value) < 5 : raise serializers.ValidationError('name must be at least 5 letters long')
        self.check_symbols(value)
        return value

    def validate_description(self, value):
        split_value = value.split()
        if len(split_value) <2: raise serializers.ValidationError('description must have at least 2 words')
        self.check_symbols(value)
        return value


    def validate(self, data):
        for i in ('width', 'height', 'length', 'weight'):
            if data[i] and data[i] < 0 : raise serializers.ValidationError(f'{i} can not be negative or zero')

        category = data['category'].name
        print(category)
        if 'food' in category.lower() or 'drink' in category.lower():
            if not data['expiration_date']:
                raise serializers.ValidationError('food and drink categories must have expiration date')
        if data['expiration_date'] and data['expiration_date'] < date.today(): raise serializers.ValidationError('expiration date can not be past date')

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