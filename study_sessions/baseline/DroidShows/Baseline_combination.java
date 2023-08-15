package nl.asymmetrics.droidshows;

import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.Espresso.pressBack;
import static androidx.test.espresso.action.ViewActions.click;
import static androidx.test.espresso.matcher.ViewMatchers.hasSibling;
import static androidx.test.espresso.matcher.ViewMatchers.withChild;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static androidx.test.espresso.matcher.ViewMatchers.withText;
import static androidx.test.platform.app.InstrumentationRegistry.getInstrumentation;

import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.containsString;

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
public class Baseline_combination {
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
        onView(withId(R.id.add_show)).perform(click());
        // 2. Enter "Yellowstone" in the "Show to add..." field and press enter key.
        device.findObject(By.res("android:id/search_src_text")).setText("Yellowstone");
        device.pressEnter();
        // 3. Click "Yellowstone (2018) (en)".
        device.wait(Until.findObject(By.res("nl.asymmetrics.droidshows:id/seriename")), 5000);
        onView(withText("Yellowstone (2018) (en)")).perform(click());
        // 4. Click the "ADD SHOW" button in the dialog.
        onView(withText("ADD SHOW")).perform(click());
        // 5. Use "press back" to return to the home page.
        pressBack();
        // 6. Click the "⋮" button of the added show.
        onView(withId(R.id.seriecontext)).perform(click());
        // 7. Click "Delete" in the popup menu.
        onView(withText("Delete")).perform(click());
        // 8. Click the "OK" button in the dialog.
        onView(withText("OK")).perform(click());
    }

    @Test
    public void markEpisodeWatched() {
        // 1. Click the "ADD SHOW" button on the home page.
        onView(withId(R.id.add_show)).perform(click());
        // 2. Enter "Yellowstone" in the "Show to add..." field and press enter key.
        device.findObject(By.res("android:id/search_src_text")).setText("Yellowstone");
        device.pressEnter();
        // 3. Click "Yellowstone (2018) (en)".
        device.wait(Until.findObject(By.res("nl.asymmetrics.droidshows:id/seriename")), 5000);
        onView(withText("Yellowstone (2018) (en)")).perform(click());
        // 4. Click the "ADD SHOW" button in the dialog.
        onView(withText("ADD SHOW")).perform(click());
        // 5. Use "press back" to return to the home page.
        pressBack();
        // 6. Click the added show on the home page.
        onView(withId(R.id.serie)).perform(click());
        // 7. Click "Season 1".
        onView(withText("Season 1")).perform(click());
        // 8. Click the checkbox of "Ep. 1. Daybreak".
        onView(allOf(withId(R.id.seen), hasSibling(withChild(withText("Ep. 1. Daybreak"))))).perform(click());
        // 9. Use "press back" to return to the Seasons page of the show.
        pressBack();
        // 10. Use "press back" to return to the home page.
        pressBack();
        // 11. Click the "⋮" button of the added show.
        onView(withId(R.id.seriecontext)).perform(click());
        // 12. Click "Delete" in the popup menu.
        onView(withText("Delete")).perform(click());
        // 13. Click the "OK" button in the dialog.
        onView(withText("OK")).perform(click());
    }

    @Test
    public void addAiredDateToCalendar() throws RemoteException {
        // 1. Click the "ADD SHOW" button on the home page.
        onView(withId(R.id.add_show)).perform(click());
        // 2. Enter "Yellowstone" in the "Show to add..." field and press enter key.
        device.findObject(By.res("android:id/search_src_text")).setText("Yellowstone");
        device.pressEnter();
        // 3. Click "Yellowstone (2018) (en)".
        device.wait(Until.findObject(By.res("nl.asymmetrics.droidshows:id/seriename")), 5000);
        onView(withText("Yellowstone (2018) (en)")).perform(click());
        // 4. Click the "ADD SHOW" button in the dialog.
        onView(withText("ADD SHOW")).perform(click());
        // 5. Use "press back" to return to the home page.
        pressBack();
        // 6. Click the added show on the home page.
        onView(withId(R.id.serie)).perform(click());
        // 7. Click "Season 5".
        onView(withText("Season 5")).perform(click());
        // 8. Click "Ep. 6. Cigarettes, Whiskey, a Meadow and Fog".
        onView(withText(containsString("Ep. 6."))).perform(click());
        // 9. Click the aired date "Dec 11, 2022".
        onView(withId(R.id.firstAired)).perform(click());
        // 10. Launch the "DroidShows" app.
        device.pressRecentApps();
        device.wait(Until.findObject(By.res("com.android.systemui:id/task_view_bar")), 5000);
        device.findObject(By.text("DroidShows")).click();
        // 11. Use "press back" to return to the Episodes page of Season 5.
        pressBack();
        // 12. Use "press back" to return to the Seasons page of the show.
        pressBack();
        // 13. Use "press back" to return to the home page.
        pressBack();
        // 14. Click the "⋮" button of the added show.
        onView(withId(R.id.seriecontext)).perform(click());
        // 15. Click "Delete" in the popup menu.
        onView(withText("Delete")).perform(click());
        // 16. Click the "OK" button in the dialog.
        onView(withText("OK")).perform(click());
    }
}
