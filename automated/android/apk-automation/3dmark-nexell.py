import time
from common import ApkTestRunner
from com.dtmilano.android.viewclient import ViewNotFoundException


class ApkRunnerImpl(ApkTestRunner):
    def __init__(self, config):
        self.config = config
        self.config['apk_file_name'] = "3DMark_v2.0.4574.apk"
        self.config['apk_package'] = "com.futuremark.dmandroid.application"
        self.config['activity'] = "com.futuremark.dmandroid.application/.SplashPageActivity"
        super(ApkRunnerImpl, self).__init__(self.config)

    def execute(self):
        '''
        time.sleep(5)
        self.dump_always()
        
        btn_ok = self.vc.findViewWithText(u'OK')
        if btn_ok:
            btn_ok.touch()
        time.sleep(2)

        self.dump_always()
        btn_allow = self.vc.findViewWithText(u'ALLOW')
        if btn_allow:
            btn_allow.touch()
        time.sleep(2)

        self.dump_always()
        btn_skip = self.vc.findViewWithText(u'SKIP')
        if btn_skip:
            btn_skip.touch()
        time.sleep(2)

        self.dump_always()
        btn_download = self.vc.findViewById("com.futuremark.dmandroid.application:id/flm_fab_benchmark")
        if btn_download:
            btn_download.touch()
        time.sleep(60)

        download_done = False
        while not download_done:
            try:
                self.logger.info("[SEOJI] check downlad is done")
                time.sleep(10)
                self.dump_always()
                down_done = self.vc.findViewById("com.futuremark.dmandroid.application:id/flm_fab_benchmark")
                if down_done:
                    download_done = True
                    down_done.touch()
                    self.logger.info("[SEOJI] download action done. Start test")
            except ViewNotFoundException:
                pass
            except RuntimeError:
                pass
            except ValueError:
                pass

        time.sleep(60)

        finished = False
        while not finished:
            try:
                self.logger.info("[SEOJI] check if test is done")
                time.sleep(20)
                self.dump_always()
                self.overall_score_exist = self.vc.findViewWithText(u'Overral score')
                if self.overall_score_exist:
                    finished = True
                    self.overall_score = self.vc.findViewById("com.futuremark.dmandroid.application:id/flm_item_score_value").getText()
                    self.logger.info("[SEOJI] 3dmark benchmark finished")
            except ViewNotFoundException:
                pass
            except RuntimeError:
                pass
            except ValueError:
                pass
        '''

    def parseResult(self):
        self.dump_always()
        self.overall_score = self.vc.findViewById("com.futuremark.dmandroid.application:id/flm_item_score_value")
        self.logger.info("[SEOJI] self.overall_score: " + str(self.overall_score.getText()))
        if int(self.overall_score.getText().replace(" ", "")) > 1500:
            self.report_result("3dmark", 'pass', self.overall_score.getText().replace(" ", ""), 'score')
        else:
            self.report_result("3dmark", 'fail')
