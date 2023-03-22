import time

import pytest


class TestLeave:
    @pytest.mark.dependency(name='load')
    def test_load_wait_num1(self, launch):
        list_href = list()
        launch.goto('https://globus-china.com/')
        try:
            launch.wait_for_load_state(state='networkidle', timeout=5000)
        except:
            launch.screenshot(path='load_fail.png')
        links = launch.query_selector_all('a')
        for link in links:
            href = link.get_attribute('href')
            if href.startswith('http'):
                list_href.append(href)
        # 移除这2个链接，是因为这2个链接有问题，无法直接跳转
        list_href.remove('https://api.whatsapp.com/send?phone=8618675762020&text=Hello%21%20I%20would%20like%20to%20learn%20more%20about%20online%20shopping%20from%20China%20%28website%29.')
        list_href.remove('https://t.me/globus_furniture')
        for url in list_href:
            launch.goto(url)
            try:
                launch.wait_for_load_state(state='networkidle', timeout=5000)
            except:
                launch.screenshot(path='load_fail-' + url + '.png')

    @pytest.mark.dependency(name='leave', depends=['load'])
    def test_leave_num2(self, launch):
        launch.goto('https://globus-china.com/')
        time.sleep(3)
        launch.get_by_role('button', name='Leave a request').click()
        time.sleep(3)
        launch.get_by_label('I agree to the processing of personal data').check()
        launch.get_by_role('button', name='Leave a request').nth(1).click()
        time.sleep(3)
        launch.screenshot(path='leaverequest.png')

    @pytest.mark.dependency(name='scroll', depends=['leave'])
    def test_scroll_num3(self, launch):
        launch.goto('https://globus-china.com/')
        time.sleep(3)
        for i in range(0, 14):
            launch.mouse.wheel(0, 1000)
            time.sleep(2)
            launch.screenshot(path='scroll' + str(i) + '.png')

    @pytest.mark.dependency(name='pc', depends=['scroll'])
    def test_view_pc_num4(self, view_pc):
        view_pc.goto('https://globus-china.com/')
        time.sleep(3)
        wid = view_pc.get_by_role('link', name='To online shop').bounding_box()['width']
        print(wid)
        view_pc.get_by_role('link', name='To online shop').screenshot(path='PC.png')

    @pytest.mark.dependency(name='mobile', depends=['pc'])
    def test_view_mobile_num4(self, view_mobile):
        view_mobile.goto('https://globus-china.com/')
        time.sleep(3)
        wid = view_mobile.get_by_role('link', name='To online shop').bounding_box()['width']
        print(wid)
        view_mobile.get_by_role('link', name='To online shop').screenshot(path='mobile.png')