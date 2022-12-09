#!/bin/bash
cd ../../../Experiment/DroidShows/
./gradlew combinedTestReportDebug
adb uninstall nl.asymmetrics.droidshows