class Claim:
	
	def __init__(self):
		self.source=""
		self.claim=""
		self.body=""
		self.conclusion=""
		self.refered_links=""
		self.title=""
		self.date=""
		self.url=""

		
	def setSource(self, str_):
		self.source = str_
		return self
	
	def setClaim(self, str_):
		self.claim = str_
		return self
		
	def setBody(self, str_):
		self.body = str_
		return self

	def setConclusion(self, str_):
		self.conclusion = str_
		return self

	def setRefered_links(self, str_):
		self.refered_links = str_
		return self

	def setTitle(self, str_):
		self.title = str_
		return self

	def setDate(self, str_):
		self.date = str_
		return self

	def setUrl(self, str_):
		self.url = str_
		return self

	def getDict(self):
		dict_={}
		dict_['source']=self.source
		dict_['claim']=self.claim
		dict_['body']=self.body
		dict_['conclusion']=self.conclusion
		dict_['refered_links']=self.refered_links
		dict_['title']=self.title
		dict_['date']=self.date
		dict_['url']=self.url
		return dict_
