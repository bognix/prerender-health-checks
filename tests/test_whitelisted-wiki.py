import requests


def test_rogerbot_UA():
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; rogerbot/2.1)'}
    r = requests.get('http://sandbox-dedicated.assassinscreed.wikia.com/wiki/Armor', headers=headers)

    assert 'ember-view' in r.content


def test_googlebot_UA_no_escaped_fragment():
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; googlebot/2.1; +http://www.google.com/bot.html)'}
    r = requests.get('http://sandbox-dedicated.assassinscreed.wikia.com/wiki/Lucy_Stillman', headers=headers)

    assert 'ember-view' not in r.content


def test_googlebot_UA_escaped_fragment():
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; googlebot/2.1; +http://www.google.com/bot.html)'}
    r = requests.get('http://sandbox-dedicated.assassinscreed.wikia.com/wiki/Guardian?_escaped_fragment_',
                     headers=headers)

    assert 'ember-view' in r.content


def test_UA():
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4'}
    r = requests.get('http://sandbox-dedicated.assassinscreed.wikia.com/wiki/Where_There_is_Smoke', headers=headers)

    assert 'ember-view' not in r.content
