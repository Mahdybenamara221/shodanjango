from django.shortcuts import render,redirect
from shodanjangoapp.models import information,address
from shodanjangoapp.forms import form,form2
import shodan
# Create your views here.

def insert(request):
    info=address.objects.all()
    if request.method=="POST":
        Form=form2(request.POST)
        Form2=form(request.POST)
        if Form.is_valid():
            try:
                Form.save()
                return redirect("/")
            except:
                pass
    else:
        Form=form()
    return render(request,'index.html',{'form':Form,'info':info})

    
def show(request, id):
    info =address.objects.get(id=id)
    key='lcufS8RJCj0UIlWptTXlJsoctxWJTDIT'
    api=shodan.Shodan(key)
    host=api.host(info.ip)
    org=host.get("org","n/a")
    os=host.get("OS","n/a")
    country=host["country_name"]
    city=host["city"]
    return render(request,'show.html',{'info':info,'org':org,'os':os,'country':country,'city':city})




def hostinfo(api={},host=''):
	host=api.host(host)
	print(f'[-] IP: {host.get("ip_str","n/a")}')
	print(f'[-] Org: {host.get("org","n/a")}')
	print(f'[-] OS: {host.get("OS","n/a")}')
	print("[-] Latitude: %s"%host["latitude"])
	print("[-] Longitude: %s"%host["longitude"])
	print("[-] Country: %s"%host['country_name'])
	print("[-] City: %s"%host["city"])



def main():
	key='lcufS8RJCj0UIlWptTXlJsoctxWJTDIT'
	api=shodan.Shodan(key)
	ip=str(input('IP @	:	'))
	hostinfo(api,ip)
#'174.127.119.236'
