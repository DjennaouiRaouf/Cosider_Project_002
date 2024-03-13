from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_gc.filters import *
from api_gc.serializers import *


# Create your views here.


#--------------------------------------- user
class SignupFields(APIView):
    def get(self, request):

        serializer = UserSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            obj = {
                    'name': field_name,
                        'type': str(field_instance.__class__.__name__),
                        'required': field_instance.required,
                        'label': field_instance.label or field_name,
                }

            field_info.append(obj)
            if (field_name == "password"):
                field_info.append({
                    'name': 'confirme' + field_name,
                    'type': str(field_instance.__class__.__name__),
                    'required':True,
                    'label': 'Confirmer le mot de passe',
                })
        return Response({'fields': field_info},
                        status=status.HTTP_200_OK)

class SignupFieldsDS(APIView):
    def get(self, request):
        serializer = UserSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            default_value = ''
            field_info.append({
                field_name:default_value ,

            })
            state = {}

            for d in field_info:
                state.update(d)
        return Response({'state': state}, status=status.HTTP_200_OK)



#--------------------------------------- contrat

class ContratFieldsList(APIView):
    def get(self, request):
        serializer = ContratSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            obj = {
                    'field': field_name,
                    'headerName': field_instance.label or field_name,


            }
            if(field_name in ['montant_ht','montant_ttc','rg','tva','rabais']):
                obj['cellRenderer'] = 'InfoRenderer'

            field_info.append(obj)
        return Response({'fields': field_info},
                        status=status.HTTP_200_OK)





class ContratFilterForm(APIView):
    def get(self,request):
        field_info = []

        for field_name, field_instance  in ContratFilter.base_filters.items():
            if(field_name  not in ['deleted','deleted_by_cascade']):

                obj = {
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),
                    'label': field_instance.label or field_name,

                }
                if str(field_instance.__class__.__name__) == 'ModelChoiceFilter':
                    anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                    serialized_data = anySerilizer(field_instance.queryset, many=True).data
                    filtered_data = []
                    for item in serialized_data:
                        filtered_item = {
                            'value': item['id'],
                            'label': item['libelle']
                        }
                        filtered_data.append(filtered_item)

                    obj['queryset'] = filtered_data

                field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)
class ContratFieldsAddUpdate(APIView):
    def get(self, request):
        serializer = ContratSerializer()
        fields = serializer.get_fields()
        field_info = []
        field_state = []
        state = {}

        for field_name, field_instance in fields.items():
            if(field_name not in ['utilisateur','montant_ht','montant_ttc','validite']):
                obj = {
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),
                    'required': field_instance.required,
                    'label': field_instance.label or field_name,
                }
                if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                    anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                    serialized_data = anySerilizer(field_instance.queryset, many=True).data
                    filtered_data = []
                    for item in serialized_data:
                        filtered_item = {
                            'value': item['id'],
                            'label': item['libelle']
                        }
                        filtered_data.append(filtered_item)

                    obj['queryset'] = filtered_data

                field_info.append(obj)

                default_value = ''
                if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                    default_value=[]
                if str(field_instance.__class__.__name__) == 'BooleanField':
                    default_value = False
                if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField', 'DecimalField',
                                                              'PositiveIntegerField',
                                                              'IntegerField', ]:
                    default_value = 0
                field_state.append({
                    field_name: default_value,
                })
                for d in field_state:
                    state.update(d)

        return Response({'fields': field_info,'state':state},
                        status=status.HTTP_200_OK)






#--------------------------------------- client

class ClientFieldsList(APIView):
    def get(self, request):
        serializer = ClientSerilizer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            obj = {
                    'field': field_name,
                    'headerName': field_instance.label or field_name,


            }


            field_info.append(obj)
        return Response({'fields': field_info},
                        status=status.HTTP_200_OK)

class ClientFieldsAddUpdate(APIView):
    def get(self, request):
        serializer = ClientSerilizer()
        fields = serializer.get_fields()
        field_info = []
        field_state = []
        state = {}

        for field_name, field_instance in fields.items():
            if(field_name not in ['utilisateur']):
                obj = {
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),
                    'required': field_instance.required,
                    'label': field_instance.label or field_name,
                }
                if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                    anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                    serialized_data = anySerilizer(field_instance.queryset, many=True).data
                    filtered_data = []
                    for item in serialized_data:
                        filtered_item = {
                            'value': item['id'],
                            'label': item['libelle']
                        }
                        filtered_data.append(filtered_item)

                    obj['queryset'] = filtered_data

                field_info.append(obj)

                default_value = ''
                if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                    default_value=[]
                if str(field_instance.__class__.__name__) == 'BooleanField':
                    default_value = False
                if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField', 'DecimalField',
                                                              'PositiveIntegerField',
                                                              'IntegerField', ]:
                    default_value = 0
                field_state.append({
                    field_name: default_value,
                })
                for d in field_state:
                    state.update(d)

        return Response({'fields': field_info,'state':state},
                        status=status.HTTP_200_OK)



class ClientFilterForm(APIView):
    def get(self,request):


        field_info = []
        for field_name, field_instance  in ClientsFilter().base_filters.items():

            if(field_name  not in ['deleted','deleted_by_cascade']):

                obj = {
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),
                    'label': field_instance.label or field_name,

                }
                if str(field_instance.__class__.__name__) == 'ModelChoiceFilter':
                    anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                    serialized_data = anySerilizer(field_instance.queryset, many=True).data
                    filtered_data = []
                    for item in serialized_data:
                        filtered_item = {
                            'value': item['id'],
                            'label': item['libelle']
                        }
                        filtered_data.append(filtered_item)

                    obj['queryset'] = filtered_data

                field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)


#-------------------------------------------------------- DQE


class PrixProdFieldsList(APIView):
    def get(self, request):
        serializer = PrixProduitSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            if(field_name not in ['',]):
                obj = {
                        'field': field_name,
                        'headerName': field_instance.label or field_name,


                }
                if(field_name in ['prix_unitaire']):
                    obj['cellRenderer'] = 'InfoRenderer'

                field_info.append(obj)
        return Response({'fields': field_info},
                        status=status.HTTP_200_OK)






class DQEFieldsList(APIView):
    def get(self, request):
        serializer = DQESerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            if(field_name not in ['prixProduit',]):
                obj = {
                        'field': field_name,
                        'headerName': field_instance.label or field_name,


                }
                if(field_name in ['montant_qte','prix_unitaire']):
                    obj['cellRenderer'] = 'InfoRenderer'

                field_info.append(obj)
        return Response({'fields': field_info},
                        status=status.HTTP_200_OK)





class DQEFilterForm(APIView):
    def get(self,request):
        field_info = []

        for field_name, field_instance  in DQEFilter.base_filters.items():
            if(field_name  not in ['deleted','deleted_by_cascade']):

                obj = {
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),
                    'label': field_instance.label or field_name,

                }
                if str(field_instance.__class__.__name__) == 'ModelChoiceFilter':
                    anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                    serialized_data = anySerilizer(field_instance.queryset, many=True).data
                    filtered_data = []
                    for item in serialized_data:
                        filtered_item = {
                            'value': item['id'],
                            'label': item['libelle']
                        }
                        filtered_data.append(filtered_item)

                    obj['queryset'] = filtered_data

                field_info.append(obj)

        return Response({'fields': field_info},status=status.HTTP_200_OK)
class DQEFieldsAddUpdate(APIView):
    def get(self, request):
        serializer = DQESerializer()
        fields = serializer.get_fields()
        field_info = []
        field_state = []
        state = {}

        for field_name, field_instance in fields.items():
            if(field_name not in ['utilisateur','montant_qte','produit','unite','prix_unitaire','contrat','id']):
                obj = {
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),
                    'required': field_instance.required,
                    'label': field_instance.label or field_name,
                }
                if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField" and field_name in [
                    'prixProduit']):

                    serialized_data = PrixProduitSerializer(field_instance.queryset, many=True).data
                    filtered_data = []
                    for item in serialized_data:
                        filtered_item = {
                            'value': item['id'],
                            'label': item['unite']+"-"+item['libelle_prod']+"-"+item['prix_unitaire']

                        }
                        filtered_data.append(filtered_item)

                    obj['queryset'] = filtered_data

                field_info.append(obj)

                default_value = ''
                if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                    default_value=[]
                if str(field_instance.__class__.__name__) == 'BooleanField':
                    default_value = False
                if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField', 'DecimalField',
                                                              'PositiveIntegerField',
                                                              'IntegerField', ]:
                    default_value = 0
                field_state.append({
                    field_name: default_value,
                })
                for d in field_state:
                    state.update(d)

        return Response({'fields': field_info,'state':state},
                        status=status.HTTP_200_OK)



#----------------------------------------------------- Bon de livraison




class BLFieldsList(APIView):
    def get(self, request):
        serializer = BonLivraisonSerializer()
        fields = serializer.get_fields()
        field_info = []
        for field_name, field_instance in fields.items():
            if(field_name not in ['contrat',]):
                obj = {
                        'field': field_name,
                        'headerName': field_instance.label or field_name,


                }
                field_info.append(obj)
        return Response({'fields': field_info},
                        status=status.HTTP_200_OK)



class BLFieldsAddUpdate(APIView):
    def get(self, request):
        serializer = BonLivraisonSerializer()
        fields = serializer.get_fields()
        field_info = []
        field_state = []
        state = {}

        for field_name, field_instance in fields.items():
            if(field_name not in ['contrat','id','date']):
                obj = {
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),
                    'required': field_instance.required,
                    'label': field_instance.label or field_name,
                }
                if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField" and field_name in [
                    'camion']):

                    anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                    serialized_data = anySerilizer(field_instance.queryset, many=True).data

                    filtered_data = []
                    for item in serialized_data:
                        filtered_item = {
                            'value': item['matricule'],
                            'label': item['matricule']

                        }
                        filtered_data.append(filtered_item)

                    obj['queryset'] = filtered_data

                field_info.append(obj)

                default_value = ''
                if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                    default_value=[]
                if str(field_instance.__class__.__name__) == 'BooleanField':
                    default_value = False
                if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField', 'DecimalField',
                                                              'PositiveIntegerField',
                                                              'IntegerField', ]:
                    default_value = 0
                field_state.append({
                    field_name: default_value,
                })
                for d in field_state:
                    state.update(d)

        return Response({'fields': field_info,'state':state},
                        status=status.HTTP_200_OK)








class ItemBLFieldsAddUpdat(APIView):
    def get(self, request):
        serializer = DetailBonLivraisonSerializer()
        fields = serializer.get_fields()
        field_info = []
        field_state = []
        state = {}

        for field_name, field_instance in fields.items():
            if(field_name not in ['contrat','id','date']):
                obj = {
                    'name': field_name,
                    'type': str(field_instance.__class__.__name__),
                    'required': field_instance.required,
                    'label': field_instance.label or field_name,
                }
                if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField" and field_name in [
                    'camion']):

                    anySerilizer = create_dynamic_serializer(field_instance.queryset.model)
                    serialized_data = anySerilizer(field_instance.queryset, many=True).data

                    filtered_data = []
                    for item in serialized_data:
                        filtered_item = {
                            'value': item['matricule'],
                            'label': item['matricule']

                        }
                        filtered_data.append(filtered_item)

                    obj['queryset'] = filtered_data

                field_info.append(obj)

                default_value = ''
                if (str(field_instance.__class__.__name__) == "PrimaryKeyRelatedField"):
                    default_value=[]
                if str(field_instance.__class__.__name__) == 'BooleanField':
                    default_value = False
                if str(field_instance.__class__.__name__) in ['PositiveSmallIntegerField', 'DecimalField',
                                                              'PositiveIntegerField',
                                                              'IntegerField', ]:
                    default_value = 0
                field_state.append({
                    field_name: default_value,
                })
                for d in field_state:
                    state.update(d)

        return Response({'fields': field_info,'state':state},
                        status=status.HTTP_200_OK)
