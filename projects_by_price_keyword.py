from urllib.request import urlopen, Request
import json


# Function for writing api result to json file

def write_json(arg):
    api_url = 'https://www.freelancer.com/api/projects/0.1/projects/active/?compact=&languages=en&full_description=true' \
               'max_avg_price=5000%3D&min_avg_price=20&query={}&job_details=true'
    api_url = api_url.format(arg)
    request = Request(api_url)
    request.add_header('freelancer-oauth-v1', '<oauth_access_token>')
    with urlopen(request) as response:
        source = response.read()
    # print(source)

    # Decoding the source object (byte object)
    decode_source = source.decode('utf-8', 'strict')
    # print(decode_source)

    data = json.loads(decode_source)
    # print(data)

    with open('projects_file_ret.json', 'w') as w_file:
        json.dump(data, w_file, indent=4)
