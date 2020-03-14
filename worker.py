from email_to_json import *
from google_call import *


def main():
    body_html = eml_to_html()
    res_dict = body_to_lists(body_html)

    for key, val in res_dict.items():
        event_creator(key, val[0], val[1], val[2])

    return


if __name__ == '__main__':
    main()