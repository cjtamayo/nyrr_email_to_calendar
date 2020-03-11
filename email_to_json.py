import datetime
import eml_parser
from bs4 import BeautifulSoup


def eml_to_html():
    """
    Grabs .eml file (hard coded name from BASH script) and pulls the HTML body
    :return: HTML string
    """
    with open('email_loc/nyrr_email.eml', 'rb') as fhdl:
        raw_email = fhdl.read()

    parsed_eml = eml_parser.eml_parser.decode_email_b(raw_email, include_raw_body=True)

    body_html = parsed_eml["body"][0]["content"]

    return body_html


def dict_builder(day_list, workout_list, descrip_list):
    """
    Takes the lists and creates a dictionary of {day: [workout, distance/pace, description]}
    :param day_list:
    :param workout_list:
    :param descrip_list:
    :return:
    """
    response_dict = dict()
    for num, day in enumerate(day_list):
        response_dict[day] = [workout_list[num], descrip_list[num][0], descrip_list[num][1]]

    return response_dict


def body_to_lists(html):
    """
    Takes HTML string, parses it, and gets the data we want, the way we want it
    :param html:
    :return:
    """

    soup = BeautifulSoup(html, 'html.parser')

    days = list()
    day_titles = list()
    descrip = list()

    for row in soup.find_all('div',attrs={"class" : "training_date_day"}):
        days.append(row.text)

    for row in soup.find_all('h1'):
        day_titles.append(row.text)


    for row in soup.find_all('p'):
        descrip.append(row.text)

    new_descrip = list()
    spot = 0
    for title in day_titles:
        if title == 'Day Off':
            new_descrip.append(['place_hold', descrip[spot]])
            spot += 1
        else:
            new_descrip.append([descrip[spot], descrip[spot+1]])
            spot += 2

    results_dict = dict_builder(days, day_titles, new_descrip)

    return results_dict
