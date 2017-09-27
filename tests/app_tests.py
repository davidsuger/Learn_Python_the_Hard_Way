from nose.tools import assert_equal, assert_in
from app import app

app.config['TESTING'] = True
web = app.test_client()


def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)


def test_hello():
    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b'Fill Out This Form', rv.data)

    data = {'name': 'David', 'greet': 'Hola'}
    rv = web.post('hello', follow_redirects=True, data=data)
    assert_in(b'David', rv.data)
    assert_in(b'Hola', rv.data)


def test_game():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b'Central Corridor', rv.data)

    data = {'action': 'shoot!'}
    rv = web.post('game', follow_redirects=True, data=data)
    assert_in(b'You died.', rv.data)

    rv = web.get('/', follow_redirects=True)
    data = {'action': 'tell a joke'}
    rv = web.post('game', follow_redirects=True, data=data)
    assert_in(b'Laser Weapon Armory', rv.data)

    rv = web.get('/', follow_redirects=True)
    data = {'action': 'tell a joke'}
    rv = web.post('game', follow_redirects=True, data=data)
    data = {'action': '0132'}
    rv = web.post('game', follow_redirects=True, data=data)
    assert_in(b'The Bridge', rv.data)

    rv = web.get('/', follow_redirects=True)
    data = {'action': 'tell a joke'}
    rv = web.post('game', follow_redirects=True, data=data)
    data = {'action': '0132'}
    rv = web.post('game', follow_redirects=True, data=data)
    data = {'action': 'slowly place the bomb'}
    rv = web.post('game', follow_redirects=True, data=data)
    assert_in(b'Escape Pod', rv.data)

    rv = web.get('/', follow_redirects=True)
    data = {'action': 'tell a joke'}
    rv = web.post('game', follow_redirects=True, data=data)
    data = {'action': '0132'}
    rv = web.post('game', follow_redirects=True, data=data)
    data = {'action': 'slowly place the bomb'}
    rv = web.post('game', follow_redirects=True, data=data)
    data = {'action': '2'}
    rv = web.post('game', follow_redirects=True, data=data)
    assert_in(b'You won!', rv.data)