#!/bin/bash
OUTPUT="$(pwd)/output"
RESULT_FILE="${OUTPUT}/result.txt"

mkdir -p "${OUTPUT}"

echo "Camera Test[0] Start"
dp_cam_test -m 0 -w 720 -h 480 -p 0 -f 0 -F 1 -t 0  -d 1 -c 100
if [ $? -eq 0 ]; then
	echo "camera-test-0 pass" >> ${RESULT_FILE}
else
	echo "camera-test-0 fail" >> ${RESULT_FILE}
	exit 0
fi

echo "Camera Test[1] Start"
dp_cam_test -m 1 -w 704 -h 480 -p 0 -f 0 -F 1 -t 2  -d 1 -c 100
if [ $? -eq 0 ]; then
	echo "camera-test-1 pass" >> ${RESULT_FILE}
else
	echo "camera-test-1 fail" >> ${RESULT_FILE}
fi

