import requests

r = requests.get('https://xkcd.com/353/')
# See all the attributes and methods we can access within this response objects
# print(dir(r))

# Give details explanation of this object
# print(help(r))

# Give the source of the page
# print(r.text)

# Download Images
r = requests.get("https://imgs.xkcd.com/comics/python.png")
	# Print the content
# print(r.content)

	# wb stands for write byte mode
# with open('comic.png', 'wb') as f:
# 	f.write(r.content)
# Print out the status code
	# 200: Normal Server
	# 300: Redirect
	# 400: Client error (permission denied)
	# 500: Server error (server crash)
print(r.status_code)

# Print out the status that the server is OK or not for anything less than 400 response
print(r.ok)

# Print all the header
# print(r.headers)

# Make specific request 
payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)

# Print out the request results
# print(r.text)

# Get the requested URL
print(r.url)
payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)


# Print out the requested results
# print(r.text)

# Get the JSON response
# print(r.json())


# Capture Python reponse in a dictionary
r_dict = r.json()
print(r_dict['form'])

# Pass credentials to ger response
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))

print(r.text)

# Pass wrong credentials
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('coreyms', 'testing'))
print(r)

# It's a good idea to set a timeout so your requests don't last forever

r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'), timeout=3)
print(r)

# Delay for 1 second in the URL
r = requests.get('https://httpbin.org/delay/1', timeout=3)
print(r)

# If it gets 6 seconds to get the response, it will get an error if you timeout is less than 6 seconds
r = requests.get('https://httpbin.org/delay/6', timeout=3)
print(r)