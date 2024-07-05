import pytest

@pytest.fixture(scope='function')
def set_cookies_and_load_page(context):
    context.add_cookies([{
        "name": "CookieScriptConsent",
        "value": "{\"googleconsentmap\":{\"ad_storage\":\"targeting\",\"analytics_storage\":\"performance\",\"ad_personalization\":\"targeting\",\"ad_user_data\":\"targeting\",\"functionality_storage\":\"functionality\",\"personalization_storage\":\"functionality\",\"security_storage\":\"functionality\"},\"bannershown\":1,\"action\":\"accept\",\"categories\":\"[\\\"functionality\\\",\\\"unclassified\\\",\\\"performance\\\",\\\"targeting\\\"]\",\"key\":\"7711c314-a010-4b8f-9007-9b0c237e6756\"}",
        "domain": "engeto.cz",
        "path": "/"
    }])
    page = context.new_page()
    page.goto('https://engeto.cz/')
    yield page
    page.close()


def test_button(set_cookies_and_load_page):
    page = set_cookies_and_load_page
    print("find button 'PŘEHLED IT KURZŮ' and click")
    button_prehled_it_kurzu = page.locator('a[href="/prehled-kurzu/"]:has-text("Přehled IT kurzů")')
    button_prehled_it_kurzu.click()

    print("check if the URL address changed and check if there is just one h1, it's text and if it is visible")
    assert page.url == "https://engeto.cz/prehled-kurzu/"
    h1 = page.wait_for_selector('h1:has-text("Kurzy programování")')
    assert h1.is_visible()


def test_hover_kurzy(set_cookies_and_load_page):
    page = set_cookies_and_load_page

    print('hover over top navbar -> "Kurzy"')
    kurzy_link = page.locator('a:has-text("Kurzy")').nth(0)
    kurzy_link.hover()

    print("wait for menu to load after hovering")
    sub_menu_selector = 'ul.sub-menu'
    page.wait_for_selector(sub_menu_selector)

    print("find Testing Akademie and click on it, then check if url changed")
    testing_akademie = page.locator('span.menu-item-title:has-text("Testing Akademie")')
    assert testing_akademie.is_visible()
    testing_akademie.click()
    assert page.url == "https://engeto.cz/testovani-softwaru/"


def test_kurz_Tester_s_Pythonem(set_cookies_and_load_page):
    page = set_cookies_and_load_page

    print("Find course Tester s Pythonem and check if the text in the card is correct. Then click on it.")
    card_link = page.locator('a.card:has-text("Tester s Pythonem")')
    assert card_link.inner_text() == "Tester s Pythonem\nDíky téhle kombinaci můžeš mířit k pozicím jako vývojář, tester nebo manažer kvality."
    card_link.click()

    print("Check if URL changed")
    assert page.url == 'https://engeto.cz/tester-s-pythonem/'

    print("Wait for h1 to load and check it' s visibility after that")
    h1 = page.wait_for_selector('h1.title:has-text("Tester s Pythonem")')
    h1.is_visible()

    print("Check the text of h3 if it is correct and it´s visibility.")
    h3 = page.locator('h3:has-text("Termíny: Kurz Tester s Pythonem")')
    h3.is_visible()

    print("Check current price of the nearest date of courses.")
    li_locator = page.locator("li.prices").nth(0)
    price_span_locator = li_locator.locator('span.price.is_bold > span.woocommerce-Price-amount.amount > bdi:has-text("36 990")')
    assert price_span_locator.is_visible()







