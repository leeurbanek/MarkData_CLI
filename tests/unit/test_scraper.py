import os
import unittest
from unittest.mock import MagicMock, patch

from bs4 import BeautifulSoup
# from requests_file import FileAdapter
from requests_html import HTMLSession


session = HTMLSession()
# session.mount('file://', FileAdapter())


def get_local(html):
    path = os.path.sep.join((os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), html))
    url = f'file://{path}'
    return session.get(url)

def get_img_src(html):
    pass


@unittest.skip('TODO: get_img_src()')
class GetSaveChartImageTests(unittest.TestCase):

    def setUp(self) -> None:
        self.html = 'stockcharts.html'
        self.src = '//stockcharts.com/c-sc/sc?s=IWM&p=D&b=5&g=0&i=0&r=1673043325495'
        self.url = 'file:///Users/000041473/my_docs/dev/cli/md_cli/tests/stockcharts.html'

    def test_get_img_src(self):
        html = """
        <div class="ChartNotesContainer">
            <table height="100%" style="border-collapse: collapse">
                <tr bgcolor="#FFFFFF">
                    <td valign="top">
                        <div id="ChartNotesMenu"></div>
                    </td>
                    <td valign="top">
                        <img alt="Chart" class="chartimg" crossorigin="use-credentials" id="chartImg" src="//stockcharts.com/c-sc/sc?s=IWM&amp;p=D&amp;b=5&amp;g=0&amp;i=0&amp;r=1673139638243"/>
                        <div id="debug" style="display:none"></div>
                    </td>
                </tr>
            </table>
        </div>
        """
        src =get_img_src(html)
        self.assertEqual(self.src, src)


# type(session)=<class 'requests_html.HTMLSession'>
# type(r)=<class 'requests_html.HTMLResponse'>
# type(soup)=<class 'bs4.BeautifulSoup'>

if __name__ == '__main__':
    unittest.main()

# print(f"\n======= url =======\n{url}")
