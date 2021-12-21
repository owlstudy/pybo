import logging

from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

def index(request):
  # logger.info("INFO 레벨로 출력")
  context = {}
  return render(request, 'pybo/question_list.html', context)