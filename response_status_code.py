# import requests module
import requests

# Making a get request
response = requests.get('https://api.github.com/')

# print request object
print(response.url)

# print status code
print(response.status_code)



'''To illustrate use of response.status_code, let’s ping api.github.com. 
To run this script, you need to have Python and requests installed on your PC.

**Check that and 200 in the output which refer to HttpResponse and Status code respectively. '''