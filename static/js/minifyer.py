from jsmin import jsmin
with open('opencv2.js') as js_file:
    minified = jsmin(js_file.read())
    with open('opencv2_out.js', 'w') as f:
    	f.write(minified)
    print(minified)
