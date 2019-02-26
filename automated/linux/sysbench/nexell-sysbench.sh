#!/bin/sh -e

. ../../lib/sh-test-lib

general_parser() {
    ms=$(grep -m 1 "total time" "${logfile}" | awk '{print substr($NF,1,length($NF)-1)}')
    add_metric "cpu-total-time" "pass" "${ms}" "s"
}

OUTPUT="$(pwd)/output"
RESULT_FILE="${OUTPUT}/result.txt"
export RESULT_FILE
logfile="/tmp/sysbench_log.txt"

create_out_dir "${OUTPUT}"
cd "${OUTPUT}"

# TEST
/usr/bin/sysbench --test=cpu --cpu-max-prime=10000 --num-threads=2 run | tee ${logfile}
general_parser

