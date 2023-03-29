from django.http import JsonResponse
from django.db import transaction
from django.forms import Form, CharField

from .models import Post, Thread

# def validate_post_data(post_data):
#     #проверка на то чтобы поля были заполнены
#     if 'username' not in post_data:
#         return False
#     #на валидность юзернейма
#     if not post_data['username'].isalnum() or len(post_data['username']) < 5:
#         return False
#     #сюда еще можно всяких проверок напихать 
    


#     return True
#     #если все заебца возвращаем тру
# def validate_thread_data(thread_data):
#     #я хз какие проверки 
#     return True



# def save_post(request):
#     if request.method == 'POST':
#         if validate_post_data(request):
#             post = Post(
#                 thread_id=request.POST['thread_id'],
#                 subject=request.POST['subject'],
#                 text=request.POST['text'],
#                 number=request.POST['number']
#             )
#             post.save()
#             return JsonResponse({'status':'KEFTEME'})
#         else:
#             return JsonResponse({'status': 'NE KEFTEME'},
#                                 {'message': 'Data ne valid'})
#     else:
#         return JsonResponse({'status': 'NE KEFTEME'},
#                             {'message': 'request ne POST'})


# def save_thread(request):
#     if request.method == 'POST':
#         if validate_thread_data(request.POST):
            
#             thread = Thread(
#                 board_id=request.POST['board_id'],
#                 tag_id=request.POST.get('tag_id'),
#                 is_pinned=request.POST.get('is_pinned', False),
#                 is_locked=request.POST.get('is_locked', False)
#             )
#             thread.save()

#             return JsonResponse({'status':'KEFTEME'})
#         else:
#             return JsonResponse({'status': 'NE KEFTEME'},
#                                 {'message': 'Data ne valid'})
#     else:
#         return JsonResponse({'status': 'NE KEFTEME'},
#                             {'message': 'request ne POST'})



class PostForm(forms.Form):
    thread_id = forms.CharField()
    subject = forms.CharField()
    text = forms.CharField()
    number = forms.CharField()

class ThreadForm(forms.Form):
    board_id = forms.CharField()
    tag_id = forms.CharField(required=False)
    is_pinned = forms.BooleanField(required=False)
    is_locked = forms.BooleanField(required=False)

@transaction.atomic
def save_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(
                thread_id=form.cleaned_data['thread_id'],
                subject=form.cleaned_data['subject'],
                text=form.cleaned_data['text'],
                number=form.cleaned_data['number']
            )
            return JsonResponse({'status': 'KEFTEME'})
        else:
            return JsonResponse({'status': 'NE KEFTEME', 'message': 'Data ne valid'}, status=400)
    else:
        return JsonResponse({'status': 'NE KEFTEME', 'message': 'request ne POST'}, status=400)

@transaction.atomic
def save_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = Thread.objects.create(
                board_id=form.cleaned_data['board_id'],
                tag_id=form.cleaned_data.get('tag_id'),
                is_pinned=form.cleaned_data.get('is_pinned', False),
                is_locked=form.cleaned_data.get('is_locked', False)
            )
            return JsonResponse({'status': 'KEFTEME'})
        else:
            return JsonResponse({'status': 'NE KEFTEME', 'message': 'Data ne valid'}, status=400)
    else:
        return JsonResponse({'status': 'NE KEFTEME', 'message': 'request ne POST'}, status=400)