"""Tests for the `hello` module."""

from cognitivefactory.interactive_clustering_gui import hello


def test_hello():
    """Test that the `hello.hello_world` method works."""
    assert hello.hello_world() == "Hello World !"
