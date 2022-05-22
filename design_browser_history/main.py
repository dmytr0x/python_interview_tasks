"""
Source: https://leetcode.com/problems/design-browser-history/
"""

from typing import Iterable

HOME_PAGE = 'https://intelliarts.com'

URLS = [f'https://resource_{i:02d}' for i in range(1, 10 + 1)]


class BrowserHistory:
    """
    You have a browser of one tab where you start on the homepage and
    you can visit another url, get back in the history number of steps or
    move forward in the history number of steps.

    Implement the BrowserHistory class:
        __init__(homepage: str) -> None
            Initializes the object with the homepage of the browser.

        visit(url: str) -> None
            Visits url from the current page.
            It clears up all the forward history.

        back(steps: int) -> str
            Move steps back in history. If you can only return x steps in the
            history and steps > x, you will return only x steps.
            Return the current url after moving back in history at most steps.

        forward(steps: int) -> str
            Move steps forward in history.
            If you can only forward x steps in the history and steps > x,
            you will forward only x steps.
            Return the current url after forwarding in history at most steps.
    """
    pass


if __name__ == '__main__':
    bh = BrowserHistory(HOME_PAGE)
    assert bh.cur_idx == 0, "History index is not 0"
    assert isinstance(bh.hist, Iterable), "History is not iterable"
    assert len(bh.hist) == 1, "Initial history should have 1 element"
    assert HOME_PAGE in bh.hist, "Initial history should contain homepage"

    # visit some resources
    for idx in range(5):
        bh.visit(URLS[idx])
    assert bh.cur_idx == 5
    assert len(bh.hist) == 6
    for idx in range(1, 5 + 1):
        assert bh.hist[idx] == URLS[idx - 1]

    # back in history
    url = bh.back(1)
    assert url == 'https://resource_04'
    assert bh.cur_idx == 4
    assert len(bh.hist) == 6
    url = bh.back(2)
    assert url == 'https://resource_02'
    assert bh.cur_idx == 2
    assert len(bh.hist) == 6
    assert HOME_PAGE == bh.hist[0]
    for idx in range(1, 5 + 1):
        assert bh.hist[idx] == URLS[idx - 1]

    # forward in history
    url = bh.forward(1)
    assert url == 'https://resource_03'
    assert bh.cur_idx == 3
    assert len(bh.hist) == 6
    assert HOME_PAGE == bh.hist[0]
    for idx in range(1, 5 + 1):
        assert bh.hist[idx] == URLS[idx - 1]
    url = bh.forward(2)
    assert url == 'https://resource_05'
    assert bh.cur_idx == 5
    assert len(bh.hist) == 6
    assert HOME_PAGE == bh.hist[0]
    for idx in range(1, 5 + 1):
        assert bh.hist[idx] == URLS[idx - 1]

    # back & visit new resources
    url = bh.back(3)
    assert url == 'https://resource_02'
    bh.visit('https://resource_06')
    bh.visit('https://resource_07')
    assert bh.cur_idx == 4
    assert len(bh.hist) == 5
    assert HOME_PAGE == bh.hist[0]
    assert bh.hist[0] == 'https://intelliarts.com'
    assert bh.hist[1] == 'https://resource_01'
    assert bh.hist[2] == 'https://resource_02'
    assert bh.hist[3] == 'https://resource_06'
    assert bh.hist[4] == 'https://resource_07'

    # back more than history size
    url = bh.back(1)
    assert url == 'https://resource_06'
    url = bh.back(1)
    assert url == 'https://resource_02'
    url = bh.back(1)
    assert url == 'https://resource_01'
    url = bh.back(1)
    assert url == HOME_PAGE
    url = bh.back(1)
    assert url == HOME_PAGE

    # forward more than history size
    url = bh.forward(4)
    assert url == 'https://resource_07'
    url = bh.forward(10)
    assert url == 'https://resource_07'

    print('All tests passed!')
