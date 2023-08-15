package nl.asymmetrics.droidshows;

import static androidx.test.platform.app.InstrumentationRegistry.getInstrumentation;

import android.os.RemoteException;
import android.util.Log;

import androidx.test.ext.junit.rules.ActivityScenarioRule;
import androidx.test.uiautomator.By;
import androidx.test.uiautomator.UiDevice;
import androidx.test.uiautomator.Until;

import org.junit.After;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;


@RunWith(JUnit4.class)
public class Baseline_uiautomator {
    @Rule
    public ActivityScenarioRule<DroidShows> activityScenarioRule = new ActivityScenarioRule<>(DroidShows.class);

    /**
     * Before the development:
     * Please make sure the emulator is connected to the Internet.
     * Please login your Google account on the emulator to make sure you can access the Calendar app.
     */
    UiDevice device = UiDevice.getInstance(getInstrumentation());

    public long startTime;
    public long endTime;

    @Before
    public final void setUp() {
        startTime = System.currentTimeMillis();
        Log.i("Time Logging", "Start " + startTime);
    }

    @After
    public final void tearDown() {
        endTime = System.currentTimeMillis();
        Log.i("Time Logging", "End " + endTime);
        long runTime = endTime - startTime;
        Log.i("Time Logging", "Run time " + runTime);
    }

    @Test
    public void addShow() {
        // 1. Click the "ADD SHOW" button on the home page.
        device.findObject(By.res("nl.asymmetrics.droidshows:id/add_show")).click();
        device.wait(Until.findObject(By.res("android:id/search_src_text")), 5000);
        // 2. Enter "Yellowstone" in the "Show to add..." field and press enter key.
        device.findObject(By.res("android:id/search_src_text")).setText("Yellowstone");
        device.pressEnter();
        // 3. Click "Yellowstone (2018) (en)".
        device.wait(Until.findObject(By.res("nl.asymmetrics.droidshows:id/seriename")), 5000);
        device.findObject(By.text("Yellowstone (2018) (en)")).click();
        // 4. Click the "ADD SHOW" button in the dialog.
        device.wait(Until.findObject(By.text("ADD SHOW")), 5000);
        device.findObject(By.text("ADD SHOW")).click();
        // 5. Use "press back" to return to the home page.
        device.wait(Until.findObject(By.text("Yellowstone (2018) (en)")), 5000);
        device.pressBack();
        // 6. Click the "⋮" button of the added show.
        device.wait(Until.findObject(By.res("nl.asymmetrics.droidshows:id/seriecontext")), 5000);
        device.findObject(By.res("nl.asymmetrics.droidshows:id/seriecontext")).click();
        // 7. Click "Delete" in the popup menu.
        device.wait(Until.findObject(By.text("Delete")), 5000);
        device.findObject(By.text("Delete")).click();
        // 8. Click the "OK" button in the dialog.
        device.wait(Until.findObject(By.text("OK")), 5000);
        device.findObject(By.text("OK")).click();
    }

    @Test
    public void markEpisodeWatched() {
        // 1. Click the "ADD SHOW" button on the home page.
        device.findObject(By.res("nl.asymmetrics.droidshows:id/add_show")).click();
        device.wait(Until.findObject(By.res("android:id/search_src_text")), 5000);
        // 2. Enter "Yellowstone" in the "Show to add..." field and press enter key.
        device.findObject(By.res("android:id/search_src_text")).setText("Yellowstone");
        device.pressEnter();
        // 3. Click "Yellowstone (2018) (en)".
        device.wait(Until.findObject(By.res("nl.asymmetrics.droidshows:id/seriename")), 5000);
        device.findObject(By.text("Yellowstone (2018) (en)")).click();
        // 4. Click the "ADD SHOW" button in the dialog.
        device.wait(Until.findObject(By.text("ADD SHOW")), 5000);
        device.findObject(By.text("ADD SHOW")).click();
        // 5. Use "press back" to return to the home page.
        device.wait(Until.findObject(By.text("Yellowstone (2018) (en)")), 5000);
        device.pressBack();
        // 6. Click the added show on the home page.
        device.wait(Until.findObject(By.res("nl.asymmetrics.droidshows:id/serie")), 5000);
        device.findObject(By.res("nl.asymmetrics.droidshows:id/serie")).click();
        // 7. Click "Season 1".
        device.wait(Until.findObject(By.text("Season 1")), 5000);
        device.findObject(By.text("Season 1")).click();
        // 8. Click the checkbox of "Ep. 1. Daybreak".
        device.wait(Until.findObject(By.res("nl.asymmetrics.droidshows:id/seen")), 5000);
        device.findObject(By.res("nl.asymmetrics.droidshows:id/seen")).click();
        // 9. Use "press back" to return to the Seasons page of the show.
        device.wait(Until.findObject(By.checked(true)), 5000);
        device.pressBack();
        // 10. Use "press back" to return to the home page.
        device.wait(Until.findObject(By.text("Season 1")), 5000);
        device.pressBack();
        // 11. Click the "⋮" button of the added show.
        device.wait(Until.findObject(By.res("nl.asymmetrics.droidshows:id/seriecontext")), 5000);
        device.findObject(By.res("nl.asymmetrics.droidshows:id/seriecontext")).click();
        // 12. Click "Delete" in the popup menu.
        device.wait(Until.findObject(By.text("Delete")), 5000);
        device.findObject(By.text("Delete")).click();
        // 13. Click the "OK" button in the dialog.
        device.wait(Until.findObject(By.text("OK")), 5000);
        device.findObject(By.text("OK")).click();
    }

    @Test
    public void addAiredDateToCalendar() throws RemoteException {
        // 1. Click the "ADD SHOW" button on the home page.
        device.findObject(By.res("nl.asymmetrics.droidshows:id/add_show")).click();
        device.wait(Until.findObject(By.res("android:id/search_src_text")), 5000);
        // 2. Enter "Yellowstone" in the "Show to add..." field and press enter key.
        device.findObject(By.res("android:id/search_src_text")).setText("Yellowstone");
        device.pressEnter();
        // 3. Click "Yellowstone (2018) (en)".
        device.wait(Until.findObject(By.res("nl.asymmetrics.droidshows:id/seriename")), 5000);
        device.findObject(By.text("Yellowstone (2018) (en)")).click();
        // 4. Click the "ADD SHOW" button in the dialog.
        device.wait(Until.findObject(By.text("ADD SHOW")), 5000);
        device.findObject(By.text("ADD SHOW")).click();
        // 5. Use "press back" to return to the home page.
        device.wait(Until.findObject(By.text("Yellowstone (2018) (en)")), 5000);
        device.pressBack();
        // 6. Click the added show on the home page.
        device.wait(Until.findObject(By.res("nl.asymmetrics.droidshows:id/serie")), 5000);
        device.findObject(By.res("nl.asymmetrics.droidshows:id/serie")).click();
        // 7. Click "Season 5".
        device.wait(Until.findObject(By.text("Season 5")), 5000);
        device.findObject(By.text("Season 5")).click();
        // 8. Click "Ep. 6. Cigarettes, Whiskey, a Meadow and Fog".
        device.wait(Until.findObject(By.textContains("Ep. 8.")), 5000);
        device.findObject(By.textContains("Ep. 8.")).click();
        // 9. Click the aired date "Dec 11, 2022".
        device.wait(Until.findObject(By.text("Jan 1, 2023")), 5000);
        device.findObject(By.text("Jan 1, 2023")).click();
        // 10. Launch the "DroidShows" app.
        device.wait(Until.findObject(By.res("com.google.android.calendar:id/input")), 5000);
        device.pressRecentApps();
        device.wait(Until.findObject(By.res("com.android.systemui:id/task_view_bar")), 5000);
        device.findObject(By.text("DroidShows")).click();
        // 11. Use "press back" to return to the Episodes page of Season 5.
        device.wait(Until.findObject(By.text("Dec 11, 2022")), 5000);
        device.pressBack();
        // 12. Use "press back" to return to the Seasons page of the show.
        device.wait(Until.findObject(By.textContains("Ep. 6.")), 5000);
        device.pressBack();
        // 13. Use "press back" to return to the home page.
        device.wait(Until.findObject(By.text("Season 1")), 5000);
        device.pressBack();
        // 14. Click the "⋮" button of the added show.
        device.wait(Until.findObject(By.res("nl.asymmetrics.droidshows:id/seriecontext")), 5000);
        device.findObject(By.res("nl.asymmetrics.droidshows:id/seriecontext")).click();
        // 15. Click "Delete" in the popup menu.
        device.wait(Until.findObject(By.text("Delete")), 5000);
        device.findObject(By.text("Delete")).click();
        // 16. Click the "OK" button in the dialog.
        device.wait(Until.findObject(By.text("OK")), 5000);
        device.findObject(By.text("OK")).click();
    }
}
