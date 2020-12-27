from test_appium.po.page.address_list_page import AddresssListPage
from test_appium.po.page.app import App
from test_appium.po.page.main_page import MainPage


def test_add_member():

    app = App()
    app.start()
    result = app.goto_main().goto_address().click_addmember().add_member_manual().add_contact()
    assert result