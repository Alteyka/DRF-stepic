from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests


@api_view(http_method_names=['GET'])
def recipient_list(request):
    result_list = []
    result_dict = {}
    try:
        response = requests.get('https://stepik.org/media/attachments/course/73594/recipients.json', timeout=40)
        recipients = response.json()
    except requests.exceptions.Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
    if response:
        for recipient in recipients:
            result_dict.update(recipient['info'])
            result_dict.update(recipient['contacts'])
            result_list.append(result_dict)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(result_list)


@api_view(http_method_names=['GET'])
def recipient_id(request, pk):
    result_dict = {}
    try:
        response = requests.get('https://stepik.org/media/attachments/course/73594/recipients.json', timeout=40)
        recipients = response.json()
    except requests.exceptions.Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)

    for recipient in recipients:
        if recipients.index(recipient) == pk:
            response = recipient
            result_dict.update(recipient['info'])
            result_dict.update(recipient['contacts'])
    if len(result_dict) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if response:
        return Response(result_dict)


@api_view(http_method_names=['GET'])
def box_list(request):
    result_list = []
    result_dict = {}
    try:
        response = requests.get(
            'https://stepik.org/media/attachments/course/73594/presentsboxes.json',
            timeout=40,)
        boxes = response.json()
    except requests.exceptions.Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
    if response:
        for box in boxes:
            for item in list(box):
                if item == "name" or item == "about" or item == "price" or item == "weight_grams":
                    final_item = {item: box[item]}
                    result_dict.update(final_item)
            result_list.append(result_dict)
            result_dict = {}
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(result_list)


@api_view(http_method_names=['GET'])
def box_detail(request, pk):
    result_dict = {}
    try:
        response = requests.get(
            'https://stepik.org/media/attachments/course/73594/presentsboxes.json',
            timeout=40,)
        boxes = response.json()
    except requests.exceptions.Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
    if response:
        for box in boxes:
            if box["inner_id"] == pk:
                for item in list(box):
                    if item == "name" or item == "about" or item == "price" or item == "weight_grams":
                        final_item = {item: box[item]}
                        result_dict.update(final_item)
        if len(result_dict) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(result_dict)


@api_view(http_method_names=['GET'])
def box_min_price(request):
    result_list = []
    try:
        response = requests.get('https://stepik.org/media/attachments/course/73594/presentsboxes.json', timeout=40)
        boxes = response.json()
    except requests.exceptions.Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
    min_price = request.query_params.get('price')
    for box in boxes:
        if box["price"] >= int(min_price):
            result_list.append(box)
    if response:
        return Response(result_list)
