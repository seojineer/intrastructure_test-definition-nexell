#!/bin/sh -e

. ../../lib/sh-test-lib

parse_ltp_output() {
	result=`grep -E -m 1 ERROR "${OUTPUT}/$1_log.txt" \
		| awk '{print $4}'`

	echo $RESULT_FILE

	if [ "$result" = "ERROR" ]; then
		echo "$1 fail" >> "${RESULT_FILE}"
	else
		echo "$1 pass" >> "${RESULT_FILE}"
	fi
}

OUTPUT="$(pwd)/output"
RESULT_FILE="${OUTPUT}/result.txt"
export RESULT_FILE

create_out_dir "${OUTPUT}"
cd "${OUTPUT}"

# TEST
testname="ltp_selftest"
logfile="${OUTPUT}/${testname}_log.txt"
/home/nexell/autotest/client/autotest-local --verbose run selftest | tee ${logfile}
cp /home/nexell/autotest/client/results/default/job_report.html ${OUTPUT}/${testname}_job_report.html
parse_ltp_output $testname 

testname="ltp_profiler_test"
logfile="${OUTPUT}/${testname}_log.txt"
/home/nexell/autotest/client/autotest-local --verbose run profiler_test | tee ${logfile}
cp /home/nexell/autotest/client/results/default/job_report.html ${OUTPUT}/${testname}_job_report.html
parse_ltp_output $testname 

testname="ltp_selftest"
logfile="${OUTPUT}/${testname}_log.txt"
/home/nexell/autotest/client/autotest-local --verbose run disktest | tee ${logfile}
cp /home/nexell/autotest/client/results/default/job_report.html ${OUTPUT}/${testname}_job_report.html
parse_ltp_output $testname 

testname="ltp_stress"
logfile="${OUTPUT}/${testname}_log.txt"
/home/nexell/autotest/client/autotest-local --verbose run stress | tee ${logfile}
cp /home/nexell/autotest/client/results/default/job_report.html ${OUTPUT}/${testname}_job_report.html
parse_ltp_output $testname 

testname="ltp_sleeptest"
logfile="${OUTPUT}/${testname}_log.txt"
/home/nexell/autotest/client/autotest-local --verbose run sleeptest | tee ${logfile}
cp /home/nexell/autotest/client/results/default/job_report.html ${OUTPUT}/${testname}_job_report.html
parse_ltp_output $testname 
