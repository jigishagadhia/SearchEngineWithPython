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
			page=page[endpos:]			#update the current content of the page - start from the end_quote till the end of page
		else:						#If there is no link on the page, break the loop 
			break
	return all_links				#retrun the list of links on the given page

def union(tocrawl,all_links):
	for url in all_links:
		if url not in tocrawl:
			tocrawl.append(url)

def add_to_index(index,keyword,url):
	if keyword not in index:
		index[keyword]=[url]
	else:
		index[keyword].append(url)

def add_content_to_index(index,content,url):
	keywords_list=content.split()
	for keyword in keywords_list:
		add_to_index(index,keyword,url)

def lookup(keyword,index):
	if keyword in index:
		return index[keyword]
	else:
		return None

def crawl_web(seed):
	tocrawl=[seed]
	crawled=[]
	index={}
	while tocrawl:
		link=tocrawl.pop()
		if link not in crawled:
			content=get_page(link)
			add_content_to_index(index,content,link)
			all_links=get_all_links(content)
			union(tocrawl,all_links)
			crawled.append(link)
	return crawled

seed='https://xkcd.com/353/'			
print(crawl_web(seed))					