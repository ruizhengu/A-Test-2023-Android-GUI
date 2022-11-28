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

**Please note:** it is possible that it takes some time when you launch an application. To avoid flakiness, you could add a waiting step by UIAutomator before all of your actions.

```java
device.wait(Until.findObject(By.res("m.co.rh.id.a_personal_stuff:id/button_add_item")), 5000);
```

### 2. Enter "Cookie" in the *"Name"* field.

You can locate the *"Name"* field and enter text in it by both Espresso and UIAutomator.

#### Espresso

The Android ID of this view can be found in the resource file *res/layout/page_item_detail.xml*.

```java
onView(withId(R.id.input_text_name)).perform(typeText("Cookie"));
```

#### UIAutomator

The resource ID of the element can be found by uiautomatorviewer.

```java
device.findObject(By.res("m.co.rh.id.a_personal_stuff:id/input_text_name")).setText("Cookie");
```

**Please note:** it is recommended to add a waiting step by UIAutomator between two actions from two different activities.

```java
device.wait(Until.findObject(By.res("m.co.rh.id.a_personal_stuff:id/input_text_name")), 5000);
```

### 3. Click *"+1"* next to the *"Amount"* field.

You can locate the *"+1"* button and click it by both Espresso and UIAutomator.

#### Espresso

The Android ID of this view can be found in the resource file *res/layout/page_item_detail.xml*.

```java
onView(withId(R.id.button_plus_1)).perform(click());
```

#### UIAutomator

The resource ID of the element can be found by uiautomatorviewer.

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

The resource ID of the element can be found by uiautomatorviewer.

```java
device.findObject(By.res("m.co.rh.id.a_personal_stuff:id/input_text_price")).setText("10");
```

### 5. Click *"Expired date time"* and select 31 January 2023 then click *"OK"*.

The "Expired date time" field can be located and clicked by both Espresso and UIAutomator.

#### Espresso

The Android ID of this view can be found in the resource file *res/layout/page_item_detail.xml*.

```java
onView(withId(R.id.input_text_expired_date_time)).perform(click());
```

#### UIAutomator

The resource ID of the element can be found by uiautomatorviewer.

```java
device.findObject(By.res("m.co.rh.id.a_personal_stuff:id/input_text_expired_date_time")).click();
```



### 6. Click the *"save"* icon in the bottom right corner.

### 7. Swipe from left to right on the home page to open the menu.

### 8. Click *"Items"* on the menu.

### 9. Assert the name of the item as "Cookie".

### 10.  Assert the Amount of the item as "1".

### 11. Assert the Price of the item as "10".

### 12. Click the *"delete"* button at the bottom of the item's view then click *"OK"*.

### 13. Use a *"press back"* action to go back to the home page.
