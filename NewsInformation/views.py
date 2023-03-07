from django.shortcuts import render, redirect
from NewsApp.models import News

# Create your views here.

def INDEX(request):
    news = News.objects.all()

    context = {
        'news': news,
    }
    return render(request, 'index.html',context)


def ADD(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        news_details = request.POST.get('news_details')
        cover_image = request.POST.get('cover_image')


        news = News(
            title = title,
            news_details = news_details,
            cover_image = cover_image,
        )
        news.save()
        return redirect('home')
    
    return render(request, 'index.html')


def Edit(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return redirect(request,'index.html',context)


# def Update(request, id):
#     if request.method == "POST":
#         title = request.POST.get('title')
#         news_details = request.POST.get('news_details')

#         news = News(
#             id = id,
#             title = title,
#             news_details = news_details
#         )
#         news.save()
#         return redirect('home')
#     return redirect(request,'index.html')

def Update(request,id):
    if request.method == "POST":
        title=request.POST.get('title')
        
        news_details=request.POST.get('news_details')
        cover_image = request.POST.get('cover_image')
       
        news = News(
            id=id,
            title = title,
            news_details=news_details
           
    )
        news.save()
        return redirect('home')
    return redirect(request,'index.html')


def Delete(request,id):
    news = News.objects.filter(id =id)
    news.delete()

    context = {
        'news': news,
    }

    return redirect('home')

