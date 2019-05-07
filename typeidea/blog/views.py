from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def post_list(request, category_id=None, tag_id=None):
    return render(request, 'blog/list.html', context = {'name': 'post_list'})
    content = 'post_list category_id={category_id}, tag_id={tag_id}'.format(
        category_id = category_id,
        tag_id = tag_id,
    )
    return HttpResponse(content)

def post_detail(request, post_id):
    return render(request, 'blog/detail.html', context = {'name': 'post_detail'})
    return HttpResponse('detail')
