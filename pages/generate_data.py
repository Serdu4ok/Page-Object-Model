import pytest


class GenerateData():
    @staticmethod
    def generate_link_for_product(number_of_page, *array_of_xfail):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
        link_array = []
        for number_of_step in range(number_of_page):
            if number_of_step in array_of_xfail:
                link_array.append(pytest.param(link + str(number_of_step), marks=pytest.mark.xfail))
            else:
                link_array.append(link + str(number_of_step))
        return link_array
