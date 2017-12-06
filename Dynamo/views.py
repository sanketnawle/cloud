from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dynamo
import boto3


class ItemCreate(CreateView):
    model = Dynamo
    fields = ['text']
    template_name = 'dynamo/index.html'


class NewItem:

    def create_item(self, item):

        print("Entered create_item")
        print("Item is: %".format(item))

        dynamodb = boto3.resource('dynamodb', region_name='us-east-2',
                                  endpoint_url='http://dynamodb.us-east-2.amazonaws.com')

        table = dynamodb.Table('Movies')

        response = table.put_item(
            Item={
                "item": item
            }
        )


def request_page(request):
  if(request.GET.get('addbtn')):
    NewItem.create_item( request.GET.get('item_name'))