import requests
import datetime

USERNAME = "tommyycpanpan"
TOKEN = "fe21e12jof19gds0adi02if19fe0dw0dwgi0201"

# user_param = {
#     "token":"fe21e12jof19gds0adi02if19fe0dw0dwgi0201",
#     "username":"tommyycpanpan",
#     "agreeTermsOfService":"yes",
#     "notMinor": "yes",
# }

header_token = {
    "X-USER-TOKEN":TOKEN,
}
graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "times",
    "type": "int",
    "color":"sora",
}

graph_endpoint = "https://pixe.la/v1/users/tommyycpanpan/graphs"

now = datetime.datetime.today()
date = now.strftime("%Y%m%d")


post_graph_endpoint = f"{graph_endpoint}/graph1"


post_graph_config = {
    "date": "20230915",
    "quantity":"20"
}

# post_graph_request = requests.post(url=post_graph_endpoint, json=post_graph_config, headers=header_token)
# print(post_graph_request.text)

update_graph_endpoint = f"{graph_endpoint}/graph1/20230915"
update_graph_config = {
    "quantity":"10",
}
# update_graph_request = requests.put(url=update_graph_endpoint, json=update_graph_config, headers=header_token)
# print(update_graph_request.text)

delete_graph_request = requests.delete(url=update_graph_endpoint, headers=header_token)
print(delete_graph_request.text)