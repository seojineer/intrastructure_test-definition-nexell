import time
from common import ApkTestRunner
from com.dtmilano.android.viewclient import ViewNotFoundException


class ApkRunnerImpl(ApkTestRunner):
    def __init__(self, config):
        self.config = config
        self.config['apk_file_name'] = 'A1_SD_v2.6.1.apk'
        self.config['apk_package'] = 'com.a1dev.sdbench'
        self.config['activity'] = 'com.a1dev.sdbench/.A1SDBenchStart'
        super(ApkRunnerImpl, self).__init__(self.config)

    def execute(self):
        time.sleep(5)
        self.dump_always()

        #btn_internal_memory = self.vc.findViewWithTextOrRaise(u'Internal memory')
        #btn_internal_memory.touch()
        #time.sleep(250)
        
        btn_ram = self.vc.findViewWithText(u'RAM')
        if not btn_ram:
            print("[SEOJI] no button named RAM")
            self.vc.swipe(800, 500, 800, 300)
            self.dump_always()
            btn_ram = self.vc.findViewWithText(u'RAM')

        btn_ram.touch()
        time.sleep(15)
        print("[SEOJI] sleep done")

        finished = False
        while not finished:
            try:
                #time.sleep()
                #self.logger.debug("[SEOJI] dump and find view by text.")
                print("[SEOJI] dump and find view by text.")
                self.dump_always()
                #self.a1sd_results = self.vc.findViewWithText(u'RAM copy')
                #self.a1sd_results = self.vc.findViewById("com.a1dev.sdbench:id/thirdLine")
                self.a1sd_results = self.vc.findViewWithText(u'RAM copy')
                print("[SEOJI] getText(): " + str(self.a1sd_results.getText()))
                
                #self.a1sd_results = self.vc.findViewById("com.a1dev.sdbench:id/thirdLine")
                #print("[SEOJI] getText(): " + str(self.a1sd_results.getText()))

                # check result
                if self.a1sd_results.getText().find("copy") > 0:
                    print("[SEOJI] getText includes 'copy'")
                    finished = True
                    self.logger.debug("[SEOJI] benchmark finished")
                    time.sleep(10)

            except ValueError:
                print("[SEOJI] ValueError")
        '''
        btn_java_bench = self.vc.findViewWithTextOrRaise(u'Java bench')
        btn_java_bench.touch()

        finished = False
        while not finished:
            try:
                time.sleep(60)
                self.dump_always()
                self.sci_results = self.vc.findViewByIdOrRaise("net.danielroggen.scimark:id/textViewResult")
                if self.sci_results.getText().find("Done") > 0:
                    finished = True
                    self.logger.info("benchmark finished")
            except ViewNotFoundException:
                pass
            except RuntimeError:
                pass
            except ValueError:
                pass
        '''

    def parseResult(self):
        pass
        '''
        keys = ["FFT (1024)", "SOR (100x100)", "Monte Carlo",
                "Sparse matmult (N=1000, nz=5000)", "LU (100x100)", "Composite Score"]

        for line in self.sci_results.getText().replace(": \n", ":").split("\n"):
            line = str(line.strip())
            key_val = line.split(":")
            if len(key_val) == 2:
                if key_val[0].strip() in keys:
                    key = key_val[0].strip().replace(' ', '-').replace('(', '').replace(')', '').replace(',', '')
                    self.report_result("scimark-" + key, 'pass', key_val[1].strip(), 'Mflops')
        '''
