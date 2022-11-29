# Android Automated UI Testing - Demonstration

In this document, the implementation process of the test case *addItemAndDelete* will be detailed, including the reasons for choosing a testing framework to perform the step or not.

## Environment

Emulator Device: Pixel 6Emulator 

Android Version: API 26, Android 8.0

Application: *Personal Stuff* 

Solution: https://github.com/guruizhen/a-personal-stuff-solution 

## Test Steps

### 1. Click *"Add Item"* on the home page.

If you are going to use UIAutomator for this test case, you could start by creating an *UiDevice* object.

```java
UiDevice device = UiDevice.getInstance(getInstrumentation());
```

You can locate the *"Add Item"* button and perform the click action on it by both Espresso and UIAutomator.

**Please note:** it is possible that it takes some time when you launch an application. To avoid flakiness, you could add a waiting step by UIAutomator before all of your actions.

```java
device.wait(Until.findObject(By.res("m.co.rh.id.a_personal_stuff:id/button_add_item")), 5000);
```

#### Espresso

The Android ID of this view can be found in the resource file *res/layout/page_home.xml*.

```java
onView(withId(R.id.button_add_item)).perform(click());
```

#### UIAutomator

The resource ID of the element can be found by uiautomatorviewer.

```java
device.findObject(By.res("m.co.rh.id.a_personal_stuff:id/button_add_item")).click();
// You can also write it like this
UiObject2 add_item = device.findObject(By.res("m.co.rh.id.a_personal_stuff:id/button_add_item"));
add_item.click();
```

### 2. Enter "Cookie" in the *"Name"* field.

You can locate the *"Name"* field and enter text in it by both Espresso and UIAutomator.

#### Espresso

The Android ID of this view can be found in the resource file *res/layout/page_item_detail.xml*.

```java
onView(withId(R.id.input_text_name)).perform(typeText("Cookie"));
```

#### UIAutomator

**Please note:** it is recommended to add a waiting step between two actions from two different activities.

```java
device.wait(Until.findObject(By.res("m.co.rh.id.a_personal_stuff:id/input_text_name")), 5000);
device.findObject(By.res("m.co.rh.id.a_personal_stuff:id/input_text_name")).setText("Cookie");
```

### 3. Click *"+1"* next to the *"Amount"* field.

You can locate the *"+1"* button and click it by both Espresso and UIAutomator.

#### Espresso

The Android ID of this view can be found in the resource file *res/layout/page_item_detail.xml*.

```java
onView(withId(R.id.button_plus_1)).perform(click());
```

#### UIAutomator

```java
device.findObject(By.res("m.co.rh.id.a_personal_stuff:id/input_text_name")).setText("Cookie");
```

### 4. Enter "10" in the *"Price"* field.

You can locate the "Price" field and enter text in it by both Espresso and UIAutomator.

#### Espresso

The Android ID of this view can be found in the resource file *res/layout/page_item_detail.xml*.

```java
onView(withId(R.id.input_text_price)).perform(typeText("10"));
```

#### UIAutomator

```java
device.findObject(By.res("m.co.rh.id.a_personal_stuff:id/input_text_price")).setText("10");
```

### 5. Click *"Expired date time"* and select 31 January 2023 then click *"OK"*.

#### 5.1 Click *"Expired date time"* 

The *"Expired date time"* field can be located and clicked by both Espresso and UIAutomator.

##### Espresso

The Android ID of this view can be found in the resource file *res/layout/page_item_detail.xml*.

```java
onView(withId(R.id.input_text_expired_date_time)).perform(click());
```

##### UIAutomator

```java
device.findObject(By.res("m.co.rh.id.a_personal_stuff:id/input_text_expired_date_time")).click();
```

#### 5.2 Click *"next"* icon to navigate to January 2023

It can be found in *app/src/main/java/m/co/rh/id/a_personal_stuff/app/ui/page/ItemDetailPage.java* that the date picker dialog is a custom view. The custom view class is from a external library *com.github.rh-id.a-navigator:a-navigator-extension-dialog*, and the dependency can be found in *base/build.gradle*.

It is recommended to use UIAutomator to find a custom view, the resource ID of the *"next"* icon *"android:id/next"* can be found by uiautomatorviewer.

##### UIAutomator

**Please note:** it is recommended to add a waiting step when a new dialog is popped up.

```java
device.wait(Until.findObject(By.res("android:id/next")), 5000);
device.findObject(By.res("android:id/next")).click();
```

#### 5.3 Click *"31"* in the calendar

The calendar is also a part of the custom view, like the *"next"* icon, so UIAutomator is preferred.

The *"31"* element can be located by text.

##### UIAutomator

```java
device.findObject(By.text("31")).click();
```

#### 5.4 Click *"OK"* button

The *"OK"* button can be located and clicked by both Espresso and UIAutomator.

##### Espresso

The Android ID of this view can be found in the resource file *res/layout/page_item_select.xml*.

```java
onView(withId(R.id.button_ok)).perform(click());
```

##### UIAutomator

```java
device.findObject(By.res("m.co.rh.id.a_personal_stuff:id/button_ok")).click();
```

### 6. Click the *"save"* icon in the bottom right corner.

The *"save"* icon can be located and clicked by both Espresso and UIAutomator.

#### Espresso

The Android ID of this view can be found in the resource file *res/menu/page_item_detail.xml*.

```java
onView(withId(R.id.menu_save)).perform(click());
```

#### UIAutomator

**Please note**: it is recommended to add a waiting step when a dialog is disabled.

```java
device.wait(Until.findObject(By.res("m.co.rh.id.a_personal_stuff:id/menu_save")), 5000);
device.findObject(By.res("m.co.rh.id.a_personal_stuff:id/menu_save")).click();
```

### 7. Swipe from left to right on the home page to open the menu.

Espresso has the default swipe APIs *swipeLeft()*, *swipeRight()*, *swipeDown()* and *swipeUp()*.

You can specify the start and end points' coordinates and the speed of a swipe action by UIAutomator's *device.swipe()* API. 

### 8. Click *"Items"* on the menu.

### 9. Assert the name of the item as "Cookie".

### 10.  Assert the Amount of the item as "1".

### 11. Assert the Price of the item as "10".

### 12. Click the *"delete"* button at the bottom of the item's view then click *"OK"*.

### 13. Use a *"press back"* action to go back to the home page.
