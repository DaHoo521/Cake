import pathlib
from bs4 import BeautifulSoup


def test_h1_contains_welcome_message():
    html_file = pathlib.Path(__file__).resolve().parents[1] / "index.html"
    with open(html_file, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html5lib")
    h1 = soup.find("h1")
    assert h1 is not None, "<h1> element not found"
    assert "Welcome to Cups N Cakes" in h1.get_text(strip=True)
