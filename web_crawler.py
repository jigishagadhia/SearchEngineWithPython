import urllib.request
def get_page(url):				#For a given url(link - eg: 'https://google.com')
    try:						#returns the html content on that page.
        with urllib.request.urlopen(url) as response:			#Requests for the content of the page
            html = response.read()			#Stores content in variable 'html'
        return html				#Returns the content as a string
    except:													
        return ""			#If not able to retrieve content, returns an empty string

def get_a_link(page):				#for a given link,returns the first link present on the page
	page=str(page)						#converts the input from 'bytes'(huge data) to 'string'
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

def union(tocrawl,crawled,all_links):
	for url in all_links:
		if url and url not in tocrawl and url not in crawled:
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
	return None

def crawl_web(seed):
	tocrawl=[seed]
	crawled=[]
	index={}
	graph={}
	while tocrawl:
		link=tocrawl.pop()
		print(len(tocrawl),link)
		if link and link not in crawled:
			crawled.append(link)
			content=get_page(link)
			add_content_to_index(index,content,link)
			outlinks=get_all_links(content)
			if outlinks:
				graph[link]=outlinks 
			union(tocrawl,crawled,outlinks)
	return index, graph

def computing_ranks(graph):
	d=0.8
	no_of_pages=len(graph)
	ranks={}
	for url in graph:
		ranks[url]=1/no_of_pages
	for i in range(0,10):
		newranks={}
		for url in graph:
			newrank=(1-d)/no_of_pages
			for node in graph:
				if url in graph[node]:
					newrank+=d*(rank[node]/len(graph[node]))
			newranks[url]=newrank
		ranks=newranks
	return ranks

seed='https://en.wikipedia.org/wiki/Friends'			
page=get_page(seed)
print(get_all_links(page))
index,graph=crawl_web(seed)
#print(computing_ranks(graph))