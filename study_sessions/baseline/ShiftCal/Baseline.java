package de.nulide.shiftcal;

import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.Espresso.pressBack;
import static androidx.test.espresso.action.ViewActions.click;
import static androidx.test.espresso.action.ViewActions.longClick;
import static androidx.test.espresso.action.ViewActions.typeText;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static androidx.test.espresso.matcher.ViewMatchers.withText;
import static androidx.test.platform.app.InstrumentationRegistry.getInstrumentation;

import android.graphics.Point;

import androidx.test.ext.junit.rules.ActivityScenarioRule;
import androidx.test.uiautomator.By;
import androidx.test.uiautomator.UiDevice;
import androidx.test.uiautomator.Until;

import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
public class TestSuite {

    @Rule
    public ActivityScenarioRule<CalendarActivity> activityScenarioRule = new ActivityScenarioRule<>(CalendarActivity.class);

    /**
     * The application is a calendar for managing your employers and shifts.
     */

    UiDevice device = UiDevice.getInstance(getInstrumentation());

    @Test
    public void setShifts() {
        // 1. Click the menu icon in the top-right corner.
        onView(withId(R.id.btnPopup)).perform(click());
        // 2. Click "Employers".
        onView(withText("Employers")).perform(click());
        // 3. Click the + icon on the bottom-right corner.
        onView(withId(R.id.fabAddEmployer)).perform(click());
        // 4. Enter "Sheffield" in the Name field (then press enter on the keyboard).
        onView(withId(R.id.scEditTextName)).perform(typeText("Sheffield")).perform(ViewActions.pressKey(KeyEvent.KEYCODE_ENTER));
        // 5. Click the ✓ icon.
        onView(withId(R.id.fabDoneEmployer)).perform(click());
        // 6. Press back to return to the homepage.
        pressBack();
        // 7. Click the menu icon in the top-right corner.
        onView(withId(R.id.btnPopup)).perform(click());
        // 8. Click "Shifts".
        onView(withText("Shifts")).perform(click());
        // 9. Click the + icon on the bottom-right corner.
        onView(withId(R.id.fabAddShift)).perform(click());
        // 10. Enter "Weekday" in the Name field.
        onView(withId(R.id.scEditTextName)).perform(typeText("Weekday"));
        // 11. Enter "WD" in the Short Name field.
        onView(withId(R.id.scEditTextSName)).perform(typeText("WD"));
        // 12. Click the button of Start Time, click 9 then click OK.
        onView(withId(R.id.btnStartTime)).perform(click());
        device.findObject(By.desc("9")).click();
        device.wait(Until.findObject(By.desc("30")), 5000);
        device.findObject(By.text("OK")).click();
        device.wait(Until.findObject(By.res("de.nulide.shiftcal:id/btnEndTime")), 5000);
        // 13. Click the button of End Time, click 17 then click OK.
        onView(withId(R.id.btnEndTime)).perform(click());
        device.findObject(By.desc("17")).click();
        device.wait(Until.findObject(By.desc("30")), 5000);
        device.findObject(By.text("OK")).click();
        device.wait(Until.findObject(By.res("de.nulide.shiftcal:id/fabDoneShift")), 5000);
        // 14. Click the ✓ icon.
        onView(withId(R.id.fabDoneShift)).perform(click());
        // 15. Press back to return to the homepage.
        pressBack();
        // 16. Click the Edit icon in the bottom-right corner of the homepage.
        onView(withId(R.id.fabEdit)).perform(click());
        // 17. Click the S icon.
        onView(withId(R.id.fabShiftSelector)).perform(click());
        // 18. Click "Weekday".
        onView(withText("Weekday")).perform(click());
        // 19. Click date 30 of January 2023.
        device.findObject(By.desc("30")).click();
        // 20. Click the ✓ icon.
        onView(withId(R.id.fabEdit)).perform(click());
        // 21. Click the Edit icon in the bottom-right corner of the homepage.
        onView(withId(R.id.fabEdit)).perform(click());
        // 22. Click the WD icon.
        onView(withId(R.id.fabShiftSelector)).perform(click());
        // 23. Click "Delete".
        onView(withText("Delete")).perform(click());
        // 24. Click date 30 of January 2023.
        device.findObject(By.desc("30")).click();
        // 25. Click the ✓ icon.
        onView(withId(R.id.fabEdit)).perform(click());
        // 26. Click the menu icon in the top-right corner.
        onView(withId(R.id.btnPopup)).perform(click());
        // 27. Click "Shifts".
        onView(withText("Shifts")).perform(click());
        // 28. Long click "Weekday".
        onView(withId(R.id.textViewSName)).perform(longClick());
        // 29. Click "Delete".
        onView(withText("Delete")).perform(click());
        // 30. Press back to return to the homepage.
        pressBack();
        // 31. Click the menu icon in the top-right corner.
        onView(withId(R.id.btnPopup)).perform(click());
        // 32. Click "Employers".
        onView(withText("Employers")).perform(click());
        // 33. Long click "Sheffield".
        onView(withId(R.id.textViewName)).perform(longClick());
        // 34. Click "Delete".
        onView(withText("Delete")).perform(click());
        // 35. Press back to return to the homepage.
        pressBack();
    }
}
