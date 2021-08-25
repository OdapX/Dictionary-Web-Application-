from django.shortcuts import render
import urllib
import json
# Create your views here.
def dictionary(request) :
  
    word = request.POST.get('word')
    if(request.method == 'POST') :
        data_from_api = urllib.request.urlopen('https://api.dictionaryapi.dev/api/v2/entries/en/'+word).read()
        image_from_api= urllib.request.urlopen('https://api.unsplash.com/search/photos/?client_id=Pj9k8NYupW64ieiy41VqFtLgr6dXqE4Fyj8zY7ql4V4&query='+word).read()
        image_url = json.loads(image_from_api) 
        data = json.loads(data_from_api) 
        if  image_url['results'] :
               url= image_url['results'][0]['urls']['raw']
        else :
               url = 'https://e7.pngegg.com/pngimages/829/733/png-clipart-logo-brand-product-trademark-font-not-found-logo-brand-thumbnail.png'              
      
        
        infos = {
           'word':data[0]['word'],
           'origin':data[0]['origin'],
           'definition' : data[0]['meanings'][0]['definitions'][0]['definition'],
           'phonetic':data[0]['phonetic'],
           'phonetics':data[0]['phonetics'][0]['audio'],
           'origin':data[0]['origin'],
           'synonyms' : data[0]['meanings'][0]['definitions'][0]['synonyms'],
           'antonyms' : data[0]['meanings'][0]['definitions'][0]['antonyms'],
           'partOfSpeech' : data[0]['meanings'][0]['partOfSpeech'],
           'example' : data[0]['meanings'][0]['definitions'][0]['example'],
           'image_url': url ,
           
               }
        
                       
    else :
          infos = { }   
       
    return render(request,'dictionaryapp/home.html',{'infos':infos})

def error_404_view(request,exception):
       return render(request,'dictionaryapp/404.html')


