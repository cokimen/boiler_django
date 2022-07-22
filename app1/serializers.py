from asyncore import read
from attr import fields
from rest_framework import serializers
from django.db import transaction

# import models
from .models import (Game, GameDetail)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class GameDetailSerializer(serializers.ModelSerializer):
    game = GameSerializer(many=False)

    class Meta:
        model = GameDetail
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        game = Game()
        game.model_name = validated_data.get('game').get('model_name')
        game.model_desc = validated_data.get('game').get('model_desc')
        game.save()

        gamedetail = GameDetail()
        gamedetail.game = game
        game.save()
        return validated_data

    def to_representation(self, instance):
        return instance
