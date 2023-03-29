from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Board, Thread, Post
from django.db.models.functions import Coalesce
from django.db.models import Max

def index(request):
    return render(request, 'index.html')
# Create your views here.

def boards(request):
    return JsonResponse({'boards':list(Board.objects.all().values())})

def board(request, board_prefix):
    curr_board = Board.object.get(prefix = board_prefix)#.prefetch_related('threads')
    page_threads = curr_board.threads.annotate(last_bump = Max('posts__date')).order_by('-last_bump')[:20]
    
    data_from_boards = {
        'board' : curr_board.name,
        'threads' : []
    }   

    for thread in page_threads:
        data_from_boards['threads'].append(
            {'subject':thread.subject},
            {'posts':list(thread.posts.values('content', 'created_at'))}
        )
    return JsonResponse(data_from_boards) 
 


