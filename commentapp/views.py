from django.shortcuts import render,redirect
from .models import Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user_comment = form.save(commit= False)
            user_comment.user = request.user
            user_comment.save()
            return redirect('index')

        else:
            return render(request,'index.html',{'form':form})
    comment = Comment.objects.all()
    comment_reverse = reversed(comment)


    form = CommentForm()
    context = {
        'yorum':comment_reverse,
        'form':form
    }

    return render(request,'index.html',context)

def detay(request):
    return render(request,'detay.html')


def sil(request):
    if request.method=='POST':
        id = request.POST['sil']
        comment = Comment.objects.filter( id = id)
        comment.delete()
        return redirect('index')