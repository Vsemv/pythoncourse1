from bs4 import BeautifulSoup



html_string = """

<!DOCTYPE html>
<html>
<head>
	<title>Web Development Page</title>
	<style type="text/css">
		
		h1{
			color: white;
			background: red;
		}

		li{
			color: red;
		}

		#css-li{
			color: blue;
		}

		.green{
			color: green;
		}

	</style>
</head>
<body>
	<h1>Web Development</h1>
	<h1 class="green">Web</h1>
	<h3>Programming Languages</h3>

	<ol>
		<li>HTML</li>
		<li id="css-li">CSS</li>
		<li class="green bold">JavaScript</li>
		<li class="green" id="python-li">Python</li>
	</ol>

</body>
</html>

"""


parsed_html = BeautifulSoup(html_string, 'html.parser')
# print(parsed_html)
# print(type(parsed_html))

# print(parsed_html.body.ol.li)
# print(parsed_html.find('li'))
# print(type(parsed_html.find('li')))
# print(parsed_html.find_all('li'))
# print(parsed_html.find(id="css-li"))
# print(parsed_html.select('#css-li'))
# print(parsed_html.select('.green')[1])
# print(parsed_html.find_all(class_="green"))
# print(parsed_html.select('li')[3])


# html_elem = parsed_html.select('li')[0]
# print(html_elem.get_text())


# html_elem_list = parsed_html.select('li')

# for html_elem in html_elem_list:
#     print(html_elem.get_text())


green_class_html_elem_list = parsed_html.select('li')

# for html_elem in green_class_html_elem_list:
#     print(html_elem.get_text())

for html_elem in green_class_html_elem_list:
    print(html_elem.attrs)
    
html_elem_list = parsed_html.select('li')[3]
# print(html_elem_list.attrs['id'])
print(html_elem_list['id'])
print(html_elem_list['class'])