import urllib.request
def get_page(url):				#For a given url(link - eg: 'https://google.com')
    try:						#returns the html content on that page.
        with urllib.request.urlopen(url) as response:			#Requests for the content of the page
            html = response.read()			#Stores content in variable 'html'
        return html				#Returns the content as a string
    except:													
        return ""			#If not able to retrieve content, returns an empty string

def get_a_link(page):				#for a given link,returns the first link present on the page
	page=str(page)					#converts the input from 'bytes'(huge data) to 'string'
	start_link=page.find("<a href=")			#finds the indext of 1st occurence of "<a href="(HTML notation for link)
	if start_link==-1:					#<string>.find(<substring>) returns -1 if no occurence found
		return None,0					# if "<a href=" is not present in the page, return None
	start_quote=page.find('"',start_link)				#find the first ' " ' occurence after "<a href=" =>start_quote
	end_quote=page.find('"',start_quote+1)				#find the next ' " ' occurence after start_quote =>end_quote
	url=page[start_quote+1:end_quote]					#Our URL in between start_quote and end_quote
	return url,end_quote							#return the url and the position of end quote

def get_all_links(page):				#for a given link, returns all the urls present on the page
	all_links=[]						#creating an empty list to store all the links on a page
	while True:
		link,endpos=get_a_link(page)				#calling get_a_link(page) and storing the output of the function
		if link:							#if the function returns a valid url:
			all_links.append(link)					#add the url to the existing list of urls
			page=page[endpos+1:]			#update the current content of the page - start from the end_quote till the end of page
		else:						#If there is no link on the page, break the loop 
			break
	return get_all_links				#retru nthe list of links on the given page

seed='https://www.wikipedia.org/'			#initializing a string of url
page=get_page(seed)						#calling get_page(seed) to get the content of the page 
print(get_all_links(page))					#printing the output of the function get_all_links(page)