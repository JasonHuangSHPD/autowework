import time
import allure
import logging
logging.basicConfig(Level=logging.INFO)


def black_wrapper(fun):
    def run(*args, **kwargs):
        basepage = args[0]
        try:
            logging.info("start find :\nargs: "+str(args)+" kwargs: " + str(kwargs))
            return fun(*args, **kwargs)
            # 捕获元素没找到异常
        except Exception as e:
            # 找不到元素时截图，并且加入到allure报告中
            path = "../tmp/tmp%d.png" % int(time.time())
            basepage.screenshot(path)
            with open(path, 'rb') as f:
                picture_data = f.read()
            allure.attach(picture_data, attachment_type=allure.attachment_type.PNG)
            # 遍历黑名单中的元素，进行处理
            for black in basepage.black_list:
                eles = basepage.finds(*black)
                if len(eles) > 0:
                    # 对黑名单进行点击，可以扩展
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e
    return run

