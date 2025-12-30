from watch import parse

def test_valid_embed():
    html = '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    assert parse(html) == "https://youtu.be/xvFZjo5PgG0"

def test_valid_embed_http():
    html = '<iframe src="http://www.youtube.com/embed/abcd1234xyz"></iframe>'
    assert parse(html) == "https://youtu.be/abcd1234xyz"

def test_valid_embed_full_iframe():
    html = '''
    <iframe width="560" height="315" src="https://www.youtube.com/embed/xyz789"
    title="YouTube video player" frameborder="0"></iframe>
    '''
    assert parse(html) == "https://youtu.be/xyz789"

def test_no_youtube_embed():
    html = '<iframe src="https://cs50.harvard.edu/python"></iframe>'
    assert parse(html) is None

def test_empty_string():
    html = ''
    assert parse(html) is None
