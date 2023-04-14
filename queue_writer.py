import urllib.request
from bs4 import BeautifulSoup
import requests
def submit_response(form_url,entry,verbose=False):
    res = urllib.request.urlopen(form_url)
    soup = BeautifulSoup(res.read(), 'html.parser')
    html = soup.decode("utf-8")
    if not "Ответы больше не принимаются." in html:
        submit_url = form_url.replace('/viewform', '/formResponse')
        form_data = {'draftResponse':[],
                    'pageHistory':0}
        form_data[entry] = "awd"
        user_agent = {'Referer':form_url,
                    'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
        global t
        t = True
        return requests.post(submit_url, data=form_data, headers=user_agent)
urlbd = "https://docs.google.com/forms/d/17yKOnNs0rCKk8cZQWHeOAxuCF5nrjUmVqcNV1sFGenI/formResponse"
urlprog = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfiYFjZkPDmIiXNgpKPNxvY2l00CanxoeT3tmxLUxKTAfPLYA/formResponse"
urlopd = "https://docs.google.com/forms/d/1UiIDe0qF5VYkcDQVxwNHnmpVUXXFwIty8W_T1yUz6jk/formResponse"
bd = "entry.1543865908"
prog = "entry.988308360"
opd = ""
global t
t = False
while not t:
    print(submit_response(urlopd,opd))