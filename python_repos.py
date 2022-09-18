import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)

response = r.json()
response_items = response['items']

names, plot_dicts = [], []

for item in response_items:
    names.append(item['name'])
    description = item['description']
    if not description:
        description = "N description provided"
    plot_dict = {
        'value':item['stargazers_count'], 
        'label':description,
        'xlink':item['html_url'],
        }
    plot_dicts.append(plot_dict)


my_style = LS('#333366', base_style = LCS)
my_style.major_label_font_size = 14
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.truncate_label = 15
my_config.show_legend = False

chart = pygal.Bar(my_config, style = my_style)
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_in_browser()
