#!/bin/bash
adb root
cd ../../../Experiment/ShiftCal/
./gradlew combinedTestReportDebug
adb uninstall de.nulide.shiftcal
