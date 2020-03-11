from email_to_json import *
from google_call import *


def main():
    print('pulling html from email')
    body_html = eml_to_html()
    print('organizing date details')
    res_dict = body_to_lists(body_html)

    for key, val in res_dict.items():
        day_list = res_dict[key]
        event_creator(key, day_list[0], day_list[1], day_list[2])

    return


if __name__ == '__main__':
    main()