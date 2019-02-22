import sys
import os


sysbenchLog = "/tmp/sysbench_log.txt"
TOTAL_TIME_STR = "total time:"
BOARD_REFS_ALLOW_MAX_TIME = {"s5p4418-navi-ref" : 50,
                             "s5p6818-avn-ref" : 110}
SYSTEM_QUIT_CMD = "reboot"
SEND_LAVA_CMD = "../../utils/send-to-lava.sh ./result.txt"


def usage() :
    print("========================================================")
    print(" Usage : python sysbenchcheck.py <board name>")
    print("      python sysbenchcheck.py s5p4418-navi-ref")
    print("      python sysbenchcheck.py s5p6818-anv-ref")
    print("========================================================")
    print("")
    print("Try Again !")
    print("")


def sysbenchGetTotalTime() :
    total_time = ""
    total_time_int = 0
    with open(sysbenchLog, 'r') as f :
        for line in f :
            if TOTAL_TIME_STR in line :
                total_time = line.split(" ")[-1].rstrip().rstrip("s")
                total_time_int = int(float(str(total_time)))
                # print(total_time_int)

    return total_time_int


def checkPassFail(boardType, totaltime) :
    # print(BOARD_REFS_ALLOW_MAX_TIME["s5p4418-navi-ref"])
    if BOARD_REFS_ALLOW_MAX_TIME[boardType] < totaltime :
        print("****************************")
        print("sysbench time is strange, too slow")
        print("FAIL")
        print("****************************")

        print("nexell-sysbench fail %d s" % totaltime)

        f = open("result.txt", 'w')
        f.write("nexell-sysbench fail %d s\n" % totaltime)
        f.close()
        return False
    else :
        print("****************************")
        print("sysbench time is good, PASS")
        print("****************************")

        print("nexell-sysbench pass %d s" % totaltime)
        f = open("result.txt", 'w')
        f.write("nexell-sysbench pass %d s\n" % totaltime)
        f.close()
        return True


def systemQuit() :
    os.system(SYSTEM_QUIT_CMD)

def send_to_lava() :
    os.system(SEND_LAVA_CMD)

def main(boardType):
    print(boardType)
    if boardType not in BOARD_REFS_ALLOW_MAX_TIME :
        print("Does not exist Board Type")
        return "FAIL"

    totaltime = sysbenchGetTotalTime()
    ret = checkPassFail(boardType, totaltime)
    if ret :
        send_to_lava()
        #pass
    else :
        # LAVA TEST ABORT
        send_to_lava()
        systemQuit()


if __name__ == "__main__":
    try :
        main(sys.argv[1])
    except IndexError :
        usage()

    finally :
        pass
