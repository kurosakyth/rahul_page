from re import search
from pages.objectitos import rahul_radios

def test_radiobutton(browser, phrase='testingoo'):
    objectado = rahul_radios(browser)

    objectado.load()
    objectado.search(phrase)
    assert phrase == 'testingoo'


