import time
from common import ApkTestRunner
from com.dtmilano.android.viewclient import ViewNotFoundException


class ApkRunnerImpl(ApkTestRunner):
    def __init__(self, config):
        self.config = config
        self.config['apk_file_name'] = "antutu-video-tester.apk"
        self.config['apk_package'] = "com.antutu.videobench"
        self.config['activity'] = "com.antutu.videobench/.activity.VideoMainActivity"
        super(ApkRunnerImpl, self).__init__(self.config)

    def execute(self):
        time.sleep(5)
        self.dump_always()
        
        btn_video_test = self.vc.findViewWithText(u'Video Test')
        if btn_video_test:
            btn_video_test.touch()
        time.sleep(2)

        self.dump_always()
        btn_ok = self.vc.findViewWithText(u'OK')
        if btn_ok:
            btn_ok.touch()
        time.sleep(2)

        finished = False
        while not finished:
            try:
                self.logger.info("[SEOJI] check if test is done")
                time.sleep(20)
                self.dump_always()
                self.result_ok = self.vc.findViewById("com.antutu.videobench:id/okvideo_size_tv")
                if self.result_ok:
                    finished = True
                    self.result_partial = self.vc.findViewById("com.antutu.videobench:id/peervideo_size_tv")
                    self.result_not_support = self.vc.findViewById("com.antutu.videobench:id/failedvideo_size_tv")
                    self.logger.info("antutu video benchmark finished")
            except ViewNotFoundException:
                pass
            except RuntimeError:
                pass
            except ValueError:
                pass

    def parseResult(self):
        self.logger.info("[SEOJI] self.result_ok: " + str(self.result_ok.getText()))
        if int(self.result_ok.getText()) > 5:
            self.report_result("antutu-video_ok", 'pass', self.result_ok.getText(), 'items')
            self.report_result("antutu-video_partially_support", 'pass', self.result_partial.getText(), 'items')
            self.report_result("antutu-video_not_support", 'fail', self.result_not_support.getText(), 'items')
        else:
            self.report_result("antutu-video", 'fail')
