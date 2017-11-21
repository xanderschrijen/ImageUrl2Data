import sublime
import sublime_plugin
import urllib.parse, urllib.request, base64

def get_data(url):
	f = urllib.request.urlopen(url)
	data = f.read()
	data_str = base64.b64encode(data)
	return data_str.decode()

def image_url_to_data_url(url):
	template = "data:image/{0};base64,{1}"
	path = urllib.parse.urlparse(url).path.lower()
	if path.endswith(".jpg") or path.endswith(".jpeg"):
		return template.format("jpeg", get_data(url))
	elif path.endswith("png"):
		return template.format("png", get_data(url))
	else:
		return "<unknown image type: |"+url+"|>"


class EncodeImgUrlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		select = self.view.sel()
		for region in list(select):
			text = self.view.substr(region)
			new_text = image_url_to_data_url(text)
			self.view.replace(edit, region, new_text)

## Test Url
# https://cdn.shopify.com/s/files/1/1187/7354/products/vol_3_1024x1024.jpog