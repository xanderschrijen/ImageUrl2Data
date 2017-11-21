import sublime
import sublime_plugin
import urllib.parse, urllib.request, base64

IMG_TYPES = {"gif": "gif", "png": "png", "jpg": "jpeg", "jpeg": "jpeg"}
TEMPLATE = "data:image/{0};base64,{1}"

class EncodeImgUrlCommand(sublime_plugin.TextCommand):

	def image_url_to_data_url(self, url):
		path = urllib.parse.urlparse(url).path
		ext = path.lower().split(".")[-1]
		if ext in IMG_TYPES:
			return TEMPLATE.format(IMG_TYPES[ext], self.get_data(url))
		else:
			return "<unknown image type |"+url+"|>"

	def get_data(self, url):
		f = urllib.request.urlopen(url)
		data = f.read()
		data_str = base64.b64encode(data)
		return data_str.decode()

	def run(self, edit):
		select = self.view.sel()
		for region in list(select):
			text = self.view.substr(region)
			new_text = image_url_to_data_url(text)
			self.view.replace(edit, region, new_text)
