from rest_framework import serializers

from product.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','pk')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
        #TODO: Poner los campos que correspondan

    def get_description(self, value):
        if value.description is None:
             return "No tiene descripcion"
        return value.description

    # Vamos a pisar el metodo UPDATE que tiene Django Rest
    def update(self, instance, validated_data):
        category_data = validated_data.pop(
            'category', None
        )
        category, created = Category.objects.get_or_create(
            **category_data
        )
        instance.category = category

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        # instance.active = validated_data.get('active', instance.active)
        instance.stock = validated_data.get('stock', instance.stock)
        #TODO: Hacer el campo "active"

        instance.save()

        return instance
    
    
    # validated_data es el formulario que viene del front
    # def create(self, validated_data):

    #     category_data = validated_data.pop(
    #         'category', None
    #     )

    #     category, created = Category.objects.get_or_create(
    #         category_data
    #     )

    #     product = Product.objects.create(
    #         # **validated_data   ---> 
    #         name=validated_data['name'],
    #         name=validated_data['price'],
    #         name=validated_data['stock'],
    #         category=category,
    #     )
    #     return product
        