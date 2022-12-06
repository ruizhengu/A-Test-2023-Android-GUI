package de.nulide.shiftcal;

import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.Espresso.pressBack;
import static androidx.test.espresso.action.ViewActions.click;
import static androidx.test.espresso.action.ViewActions.longClick;
import static androidx.test.espresso.action.ViewActions.typeText;
import static androidx.test.espresso.matcher.ViewMatchers.withClassName;
import static androidx.test.espresso.matcher.ViewMatchers.withContentDescription;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static androidx.test.espresso.matcher.ViewMatchers.withText;
import static androidx.test.platform.app.InstrumentationRegistry.getInstrumentation;

import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.containsString;
import static org.junit.Assert.assertEquals;

import android.os.RemoteException;
import android.widget.CheckedTextView;

import androidx.test.ext.junit.rules.ActivityScenarioRule;
import androidx.test.uiautomator.By;
import androidx.test.uiautomator.UiDevice;
import androidx.test.uiautomator.UiObject;
import androidx.test.uiautomator.UiObject2;
import androidx.test.uiautomator.Until;

import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)

public class Baseline {
    @Rule
    public ActivityScenarioRule<CalendarActivity> activityScenarioRule = new ActivityScenarioRule<>(CalendarActivity.class);

    /**
     * Before the development:
     * Please make sure the emulator is connected to the Internet.
     * Please login your Google account on the emulator to make sure you can access the Calendar app.
     * Turn on the "Sync" functionality in Settings:
     * 1. Click the "menu" icon in the top right corner of the home page.
     * 2. Click "Settings".
     * 3. Click "Sync".
     * 4. Turn on the switch to enable sync functionality.
     */

    UiDevice device = UiDevice.getInstance(getInstrumentation());

    public void createEmployerSheffield() {
        onView(withId(R.id.btnPopup)).perform(click());
        onView(withText("Employers")).perform(click());
        onView(withId(R.id.fabAddEmployer)).perform(click());
        onView(withId(R.id.scEditTextName)).perform(typeText("Sheffield"));
        device.pressEnter();
        onView(withId(R.id.fabDoneEmployer)).perform(click());
    }

    public void deleteEmployerSheffield() {
        onView(withId(R.id.textViewName)).perform(longClick());
        onView(withText("Delete")).perform(click());
        pressBack();
    }

    public void createShiftWeekday() {
        onView(withId(R.id.btnPopup)).perform(click());
        onView(withText("Shifts")).perform(click());
        onView(withId(R.id.fabAddShift)).perform(click());
        onView(withId(R.id.scEditTextName)).perform(typeText("Weekday"));
        onView(withId(R.id.scEditTextSName)).perform(typeText("WD"));
        onView(withId(R.id.btnStartTime)).perform(click());
        device.wait(Until.findObject(By.res("android:id/time_header")), 5000);
        device.findObject(By.desc("9")).click();
        device.wait(Until.findObject(By.desc("30")), 5000);
        device.findObject(By.text("OK")).click();
        onView(withId(R.id.btnEndTime)).perform(click());
        device.wait(Until.findObject(By.res("android:id/time_header")), 5000);
        device.findObject(By.desc("17")).click();
        device.wait(Until.findObject(By.desc("30")), 5000);
        device.findObject(By.text("OK")).click();
        onView(withId(R.id.fabDoneShift)).perform(click());
    }

    public void deleteShiftWeekday() {
        onView(withId(R.id.textViewSName)).perform(longClick());
        onView(withText("Delete")).perform(click());
        pressBack();
    }

    @Test
    public void createEmployer() {
        // 1. Click the "menu" icon in the top right corner of the home page.
        // 2. Click "Employers".
        // 3. Click the "add" icon in the bottom right corner.
        // 4. Enter "Sheffield" in the "Name" field.
        // 5. Click the "✓" icon in the bottom right corner.
        createEmployerSheffield();
        // 6. Assert the created employer's name to "Sheffield".
        device.wait(Until.findObject(By.res("de.nulide.shiftcal:id/textViewName")), 5000);
        assertEquals(device.findObject(By.res("de.nulide.shiftcal:id/textViewName")).getText(), "Sheffield");
        // 7. Long click "Sheffield" on the "Employers" page.
        // 8. Click "Delete" in the popup window.
        // 9. Use "press back" to return to the home page.
        deleteEmployerSheffield();
    }

    @Test
    public void createShifts() {
        // 1. Click the "menu" icon in the top right corner of the home page.
        // 2. Click "Employers".
        // 3. Click the "add" icon in the bottom right corner.
        // 4. Enter "Sheffield" in the "Name" field.
        // 5. Click the "✓" icon in the bottom right corner.
        createEmployerSheffield();
        // 6. Use "press back" to return to the home page.
        pressBack();
        // 7. Click the "menu" icon in the top right corner of the home page.
        // 8. Click "Shifts".
        // 9. Click the "add" icon in the bottom right corner.
        // 10. Enter "Weekday" in the "Name" field.
        // 11. Enter "WD" in the "Short Name" field.
        // 12. Click the "Start Time" button, click "9" on the dial then click "OK".
        // 13. Click the "End Time" button, click "17" on the dial then click "OK".
        // 14. Click the "✓" icon in the bottom right corner.
        createShiftWeekday();
        // 15. Assert the created shift's name to "Weekday".
        device.wait(Until.findObject(By.res("de.nulide.shiftcal:id/textViewName")), 5000);
        assertEquals(device.findObject(By.res("de.nulide.shiftcal:id/textViewName")).getText(), "Weekday");
        // 16. Long click "Weekday" on the "Shifts" page.
        // 17. Click the "Delete" in the popup window.
        // 18. Use "press back" to return to the home page.
        deleteShiftWeekday();
        // 19. Click the "menu" icon in the top right corner of the home page.
        onView(withId(R.id.btnPopup)).perform(click());
        // 20. Click "Employers".
        onView(withText("Employers")).perform(click());
        // 21. Long click "Sheffield" on the "Employers" page.
        // 22. Click "Delete" in the popup window.
        // 23. Use "press back" to return to the home page.
        deleteEmployerSheffield();
    }

    @Test
    public void setShifts() throws RemoteException {
        // 1. Click the "menu" icon in the top right corner of the home page.
        // 2. Click "Employers".
        // 3. Click the "add" icon in the bottom right corner.
        // 4. Enter "Sheffield" in the "Name" field.
        // 5. Click the "✓" icon in the bottom right corner.
        createEmployerSheffield();
        // 6. Use "press back" to return to the home page.
        pressBack();
        // 7. Click the "menu" icon in the top right corner of the home page.
        // 8. Click "Shifts".
        // 9. Click the "add" icon in the bottom right corner.
        // 10. Enter "Weekday" in the "Name" field.
        // 11. Enter "WD" in the "Short Name" field.
        // 12. Click the "Start Time" button, click "9" on the dial then click "OK".
        // 13. Click the "End Time" button, click "17" on the dial then click "OK".
        // 14. Click the "✓" icon in the bottom right corner.
        createShiftWeekday();
        // 15. Use "press back" to return to the home page.
        pressBack();
        // 16. Click the "edit" icon on the bottom right corner.
        onView(withId(R.id.fabEdit)).perform(click());
        // 17. Click the "S" icon above the "edit" icon.
        onView(withId(R.id.fabShiftSelector)).perform(click());
        // 18. Click "Weekday".
        onView(withText("Weekday")).perform(click());
        // 19. Click date "10" in the calendar.
        device.findObject(By.desc("10")).click();
        // 20. Click the "✓" icon in the bottom right corner.
        onView(withId(R.id.fabEdit)).perform(click());
//        // 21. Launch the "Calendar" application.
//        device.pressHome();
//        device.wait(Until.findObject(By.res("com.google.android.apps.nexuslauncher:id/all_apps_handle")), 5000);
//        device.findObject(By.res("com.google.android.apps.nexuslauncher:id/all_apps_handle")).click();
//        device.wait(Until.findObject(By.res("com.google.android.apps.nexuslauncher:id/search_box_input")), 5000);
//        device.findObject(By.text("Calendar")).click();
//        // 22. Click the "WD - Weekday" Calendar event.
//        device.wait(Until.findObject(By.desc("9:00 AM – 5:00 PM: WD - Weekday")), 5000);
//        device.findObject(By.desc("9:00 AM – 5:00 PM: WD - Weekday")).click();
//        // 23. Assert the event name to "WD - Weekday".
//        device.wait(Until.findObject(By.res("com.google.android.calendar:id/title")), 5000);
//        assertEquals(device.findObject(By.res("com.google.android.calendar:id/title")).getText(), "WD - Weekday");
//        // 24. Assert the event date to "Saturday, December 10".
//        // 25. Click the "⋮" button in the top right corner of the Calendar event.
//        device.findObject(By.desc("More options")).click();
//        // 26. Click "Delete" in the popup menu.
//        device.wait(Until.findObject(By.text("Delete")), 5000);
//        device.findObject(By.text("Delete")).click();
//        // 27. Click "DELETE" in the dialog.
//        device.wait(Until.findObject(By.text("DELETE")), 5000);
//        device.findObject(By.text("DELETE")).click();
//        // 28. Launch the "ShiftCal" application.
//        device.pressRecentApps();
//        device.wait(Until.findObject(By.res("com.android.systemui:id/task_view_bar")), 5000);
//        device.findObject(By.text("ShiftCal")).click();
        // 29. Click the "edit" icon on the bottom right corner.
        onView(withId(R.id.fabEdit)).perform(click());
        // 30. Click the "S" icon above the "edit" icon.
        onView(withId(R.id.fabShiftSelector)).perform(click());
        // 31. Click "Delete".
        onView(withText("Delete")).perform(click());
        // 32. Click date "10" in the calendar.
//        onView(allOf(withText(containsString("10")), withText(containsString("WD")))).perform(click());
        device.findObject(By.descContains("10")).click();
//        device.wait(Until.findObject(By.desc("10\nWD")), 5000);
//        device.findObject(By.desc("10\nWD")).click();
        // 33. Click the "✓" icon in the bottom right corner.
        onView(withId(R.id.fabEdit)).perform(click());
        // 34. Click the "menu" icon in the top right corner of the home page.
        onView(withId(R.id.btnPopup)).perform(click());
        // 35. Click "Shifts".
        onView(withText("Shifts")).perform(click());
        // 36. Long click "Weekday" on the "Shifts" page.
        // 37. Click the "Delete" in the popup window.
        // 38. Use "press back" to return to the home page.
        deleteShiftWeekday();
        // 39. Click the "menu" icon in the top right corner of the home page.
        onView(withId(R.id.btnPopup)).perform(click());
        // 40. Click "Employers".
        onView(withText("Employers")).perform(click());
        // 41. Long click "Sheffield" on the "Employers" page.
        // 42. Click "Delete" in the popup window.
        // 43. Use "press back" to return to the home page.
        deleteEmployerSheffield();
    }
}
