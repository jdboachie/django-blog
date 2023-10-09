from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'author': 'Jude Boachie',
#         'title': 'ChristWorld Incorporated: The Vision and Mission',
#         'content': 'Vision:\nBuilding A Nation Where Christ Is All And In All And To Make Christ The Centre Of The World By Dispensing Christ With Love, The Holy Ghost As Our Means.\nMission:Building Christ Into All Men Through The Revelation [Galatians 1:16], Formation [Galatians 4:19],  Magnification [Philippians 1:20], And Glorification [2 Thessalonians 1:12] Of Christ In All Men, Until All Men, Conform To The Image Of His Son [Romans 8:29], Using Christ As The Building Material.',
#         'date_posted': 'October 10, 2023'
#     },
#     {
#         'author': 'Freda Yamorti Gbande',
#         'title': 'Love Economy Church: The Founder',
#         'content': 'Bishop Isaac Oti Boateng is the president and founder of Love Economy (aka Christworld Inc.), a dynamic, multifaceted global ministry currently numbering over 1000 people in 4 continents. He is an alumni of the Kwame Nkrumah University of Science and Technology (KNUST) and has a Masters in Business Administration and offers management consultancy. His love for entrepreneurship has lead him to start and help numerous businesses and startups achieve maximum efficiency through his business management consultancy. However, his greatest source of joy and pride is seeing God’s people discover the inherent power of God in them.',
#         'date_posted': 'October 9, 2023'
#     },
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
