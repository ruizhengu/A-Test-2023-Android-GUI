#!/bin/bash
adb root
cd ../../../Experiment/DroidShows/
./gradlew combinedTestReportDebug
adb uninstall nl.asymmetrics.droidshows
