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
	start_quote=page.find('"',start_link)
	end_quote=page.find('"',start_quote+1)
	url=page[start_quote+1:end_quote]
	page=page[end_quote:]
	return url

seed='https://www.wikipedia.org/'
page=get_page(seed)
print(get_a_link(page))