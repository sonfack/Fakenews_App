from googleapiclient.discovery import build
import json

"""
key google api : AIzaSyAHM2BO5oMzQ3QAnR_go6WxDMJ9TJGpJSE

pip install google-api-python-client

<script>
  (function() {
    var cx = '017411662308276300777:dhoerkg7vwi';
    var gcse = document.createElement('script');
    gcse.type = 'text/javascript';
    gcse.async = true;
    gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(gcse, s);
  })();
</script>
<gcse:search></gcse:search>


Identifiant du moteur de recherche 
017411662308276300777:dhoerkg7vwi


"""
my_api_key = 'AIzaSyAHM2BO5oMzQ3QAnR_go6WxDMJ9TJGpJSE'
my_cse_id = '017411662308276300777:dhoerkg7vwi'

def google_search(search_term, api_key = my_api_key, cse_id=my_cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res


def readUrlFromGoogleSearch(jsonFile):
    links = []
    jsonFileconvert = json.dumps(jsonFile, ensure_ascii=False)
    loaded_json = json.loads(jsonFileconvert)
    for pagemap in loaded_json['items']:
        links.append(pagemap['link'])
    return links


#result = google_search("Coffee", my_api_key, my_cse_id)

#list = readUrlFromGoogleSearch(result)

#print(list)