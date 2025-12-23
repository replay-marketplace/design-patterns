from hello_world.hello import hello_world

def test_hello_world(capsys):
    """Test that hello_world prints the correct message."""
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == 'Hello, World!\n'

