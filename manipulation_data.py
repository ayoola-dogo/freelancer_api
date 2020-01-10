import json


# projects_by_price_keyword.write_json()
# with open('projects_file_ret.json', 'r') as r_file:
#     data = json.load(r_file)
# print(len(data))
# print('==========================================================================================================')
# for i in data:
#     print(i)
# print('==========================================================================================================')
# print('Items in result: =>')
# result = data['result']
# print(len(result))
# print(type(result))
# for k, v in result.items():
#     print(k, v)
# print('==========================================================================================================')
# print('Items in projects')
# projects = result['projects']
# print(type(projects))
# print(len(projects))

def read_json():
    with open('projects_file_ret.json', 'r') as r_file:
        data = json.load(r_file)

    result = data['result']
    projects = result['projects']
    return projects


def number_projects(projects):
    if projects:
        return len(projects)


# print('==========================================================================================================')


def output(projects):
    project_contents = list()
    n = 0
    for project in projects:
        n += 1
        project_contents.append('Preview  {} : {}'.format(n, project['preview_description']))
        project_contents.append('Country: {}'.format(project['currency']['country']))
        project_contents.append(project['status'])
        project_contents.append('Project Id: {}'.format(project['id']))
        project_contents.append('Title: {}'.format(project['title']))
        project_contents.append(project['description'])
        project_contents.append('Owner Id: {}'.format(project['owner_id']))
        project_contents.append('Currency: {}'.format(project['currency']['name']))
        project_contents.append(project['budget'])
        project_contents.append(project['bid_stats'])
    return project_contents
