from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def count(request):
    data=request.GET["counttextarea"]
    word_list=data.split()
    word_count=len(word_list)

    my_dict={}

    for word in word_list:
        if word in my_dict:
            my_dict[word] +=1
        else:
            my_dict[word] = 1

    sorted_list=sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{"fulltext":data,"wordcount":word_count,"sortlist":sorted_list})
