from playwright.sync_api import Page
from ui_tests.helpers.config import BASE_URL


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.header = "text=Example Domain"

    def goto(self):
        self.page.goto(BASE_URL, wait_until="networkidle")

    def get_header_text(self):
        return self.page.locator(self.header).inner_text()

    def find_element_on_page_by_text(self, text: str):
        return self.page.get_by_text(text, exact=False)

    def find_element_on_page_by_placeholder(self, name: str):
        return self.page.get_by_placeholder(name)

    def find_game_result(self, name: str):
        locator = self.page.get_by_role("link", name=name)

        try:
            if locator.first.is_visible(timeout=3000):
                return locator.first
        except:
            pass

        # fallback exact match
        return self.page.get_by_role("link", name=name, exact=True)

    def scroll(self):
        self.page.evaluate("window.scrollBy(0, window.innerHeight)")

    def click_on_stream(self):
        # Twitch mobile UI – stabilan selektor za live stream preview
        stream_card = self.page.locator("a[data-a-target='preview-card-image-link']").first

        try:
            stream_card.wait_for(state="visible", timeout=10000)
        except:
            raise AssertionError("Nema dostupnih live streamova za ovu igru!")

        stream_card.click(force=True)


