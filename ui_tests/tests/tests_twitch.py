import logging

import pytest

from ui_tests.pages.home_page import HomePage

logger = logging.getLogger(__name__)


class TestTwitch:
    @pytest.mark.smoke_test_twitch
    def test_home_page_header(self, mobile_page):
        logger.info("Starting Test")

        home = HomePage(mobile_page)
        home.goto()

        browse = home.find_element_on_page_by_text("Browse")
        browse.wait_for(timeout=5000)
        browse.click()

        search_box = home.find_element_on_page_by_placeholder("Search")
        search_box.wait_for(timeout=5000)
        search_box.fill("StarCraft II")

        game = home.find_game_result("StarCraft II")
        game.wait_for(timeout=8000)
        game.click()

        home.scroll()
        home.scroll()

        first_stream = mobile_page.locator("button article h4[title]").first
        first_stream.wait_for(state="visible", timeout=8000)

        stream_card_click_target = first_stream.locator("xpath=ancestor::button")
        stream_card_click_target.click(force=True)

        player = mobile_page.locator("video")
        player.wait_for(state="visible", timeout=15000)
        mobile_page.screenshot(path="twitch_test_result.png", full_page=True)
        assert player.is_visible(), "Stream doesn't work"
