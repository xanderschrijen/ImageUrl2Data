import sublime
import sublime_plugin
import urllib.parse, urllib.request, base64

CONTENT_TYPE = "Content-Type"

class EncodeImgUrlCommand(sublime_plugin.TextCommand):

	def image_url_to_data_url(self, url):
		response = urllib.request.urlopen(url)
		if CONTENT_TYPE not in response.info():
			return "<unknown image type |"+url+"|>"
		content_type = response.info()[CONTENT_TYPE]
		data = response.read()
		data_str = base64.b64encode(data).decode()
		return "data:{0};base64,{1}".format(content_type, data_str)

	def run(self, edit):
		select = self.view.sel()
		for region in list(select):
			text = self.view.substr(region)
			new_text = self.image_url_to_data_url(text)
			self.view.replace(edit, region, new_text)
