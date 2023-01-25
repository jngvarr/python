from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view
import os

path = os.path.dirname(os.path.abspath(__file__))

def create(device = 1):
    # path = os.path.dirname(os.path.abspath(__file__))
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device))
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += '  </body>\n</html>'
    
    with open(path+'\index.html', 'w') as page:
        page.write(html)

    return html



def new_create(data ,device = 1):
    # path = os.path.dirname(os.path.abspath(__file__))
    t, p, w = data
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, t)
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, w)
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '  </body>\n</html>'
    
    with open(path + '\new_index.html', 'a') as page:
        page.write(html)

    return data