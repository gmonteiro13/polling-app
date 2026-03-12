from rest_framework import serializers
from .models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    # Definimos o id como opcional para que não dê erro ao criar novas escolhas
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']

class QuestionSerializer(serializers.ModelSerializer):
    # Retiramos o 'read_only=True' para permitir enviar dados
    choice_set = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choice_set']

    def create(self, validated_data):
        # Removemos os dados das escolhas do dicionário principal
        choices_data = validated_data.pop('choice_set')
        
        # Criamos a Questão
        question = Question.objects.create(**validated_data)
        
        # Criamos cada uma das Choices vinculadas a essa Questão
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
            
        return question