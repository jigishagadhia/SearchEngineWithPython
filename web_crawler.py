import urllib.request
def get_page(url):
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
        return html
    except:
        return ""

def get_a_link(page):
	page=str(page)
	start_link=page.find("<a href=")
	if start_link==-1:
		return None,0
	start_quote=page.find('"',start_link)
	end_quote=page.find('"',start_quote+1)
	url=page[start_quote+1:end_quote]
	return url,end_quote

def get_all_links(page):
	all_links=[]
	while True:
		link,endpos=get_a_link(page)
		if link:
			all_links.append(link)
			page=page[endpos+1:]
		else:
			break
	return all_links

seed='https://www.wikipedia.org/'
page=get_page(seed)
print(get_all_links(page))