import time
from playwright.sync_api import sync_playwright

base_url = 'https://maps.google.com'
search_query = 'bakery, chicago, IL'

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(java_script_enabled=True)
page = context.new_page()
page.goto(base_url, wait_until='load')

# find the search box
input_box = page.locator('//input[@name="q"]')
input_box.fill(search_query)
input_box.press('Enter')

# wait for search results container
xpath_search_result_element = '//div[@role="feed"]'
page.wait_for_selector(xpath_search_result_element)

# scroll results into view
results_container = page.query_selector(xpath_search_result_element)
results_container.scroll_into_view_if_needed()

keep_scrolling = True
while keep_scrolling:
    results_container.press('Space')
    time.sleep(2.5)

    if results_container.query_selector('//span[text()="You\'ve reached the end of the list."]'):
        results_container.press('Space')
        keep_scrolling = False

with open('maps.html', 'w', encoding='utf-8') as f:
    f.write(results_container.inner_html())

context.close()
browser.close()
playwright.stop()