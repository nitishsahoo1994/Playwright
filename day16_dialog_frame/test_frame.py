import pytest
from playwright.sync_api import sync_playwright, expect,Page


@pytest.mark.skip
def test_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames=page.frames
    print("Number of frames on a page:", len(frames))  # 7

    #frame1=page.frame_locator("")
    frame2=page.frame(url="https://ui.vision/demo/webtest/frames/frame_2")

    input_box=frame2.locator("input[name='mytext2']")
    input_box.fill("Nitish")

    expect(input_box).to_have_value("Nitish")


    page.wait_for_timeout(2000)
    page.close()



def test_inner_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    page.wait_for_timeout(2000)
    # frame 3
    frame3 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3")  # grap teh frame 3

    inputbox=frame3.locator("input[name='mytext3']")
    # get the inputbox from frame 3 and provide teh text

    inputbox.fill("Welcome")

    child_frames=frame3.child_frames
    print("Number of child frames inside teh frame 3: ", len(child_frames))

    innerframe=child_frames[0]

    radio=innerframe.locator("span:has-text('Form Autofilling')")
    radio.click()



    page.wait_for_timeout(5000)



