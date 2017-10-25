from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import loader


from . models import Album,Song

# Create your views here.
def index(request):
	all_albums = Album.objects.all()
	# template = loader.get_template('music/index.html') combined with render
	context = {
		'all_albums' : all_albums,
	}
	# html = ''
	# for album in all_albums:
	# 	url = '/music/'+str(album.id)
	# 	html += '<a href = "'+url+'">'+album.album_title+'</a><br>'
	# return HttpResponse(template.render(context,request))
	return render(request,'music/index.html',context)

def detail(request,album_id):
	#try:
	# 	album = Album.objects.get(pk = album_id)
	# 	return render(request,'music/detail.html',{'album' : album})
	# except Album.DoesNotExist:
	# 	raise Http404("Album doesn not exists")
	album =  get_object_or_404(Album, pk = album_id)
	return render(request,'music/detail.html',{'album' : album})

def favorite(request,album_id):
	album =  get_object_or_404(Album, pk = album_id)

	try:
		selected_song = album.song_set.get(pk = request.POST['song'])
		print(selected_song)
	except(KeyError,SongDoesNotExists):
		return render(request,'music/detail.html',{
			'album':album,
			'error_message' : 'You did not select valid song',
			})
	else:
		selected_song.is_favorite = True
		selected_song.save()	
		return render(request,'music/detail.html',{'album' : album})


	