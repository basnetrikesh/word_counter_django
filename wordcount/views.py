from django.http import HttpResponse
from django.shortcuts import render #this is to return the html file instead of in the form of string
def go_home(request):
    return render(request,"home.html")
def go_riker(request):
    return HttpResponse("<h1>I am riker</h1>") #writing all the html code inside this tiny space is not practicle so we use something called templates
def go_count(request):
    fulltext=request.GET["fulltext"] #getting all the text which is entered into the textarea
    word_list=fulltext.split()
    word_dictonary={}
    for word in word_list:
        if word in word_dictonary:
            word_dictonary[word]+=1
        else:
            word_dictonary[word]=1
        
    
    return render(request,"count.html",{"fulltext":fulltext,"word_count":len(word_list),"word_dictonary_list":word_dictonary.items()}) #passing the text entered in the form of dictionary
def go_about(request):
    return render(request,"about.html")