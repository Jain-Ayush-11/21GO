# 21GO
To help with the issue of tracking days going without the addictive habit, an app called "21GO" allowing people to track these habits.
# About the app
> A Timer Representing the time spent without that certain habit is available on the home screen with different streak based wallpapers which are updated as the streak progresses and reset if the streak is reset.
> The app has a relapse button to record a relapse and restart the journey.
> Along with wallpapers, the user can also:
    - Record certain habits, Workout, Reading and Meditation.
    - View his Journey in a calendar based representation and check the days he relapsed and day which were a success.
    - Upload and read text posts on a community channel/forum open to all.
# Tech Used
> Kotlin (Android) for Frontend.
> Django Rest Framework for Backend.
> Designed using Figma/Adobe Suite.
# Algorithms and Methods Used
> A CRUD application built using the Django Rest Framework.
> Usage of Generic views provided in the DRF.
# Problems Faced (Backend and Design)
> Building the calender and stats and recording the relapse while updating the best and number of attempts simultaneously - Implemented using simple save method and updating values in the views.
> Sending only a single random wallpaper for a certain Day - Implemented using a simple forloop and generating a random integer in the range of the count of queryset.
> Designing the application with a suitable color combination with the dark theme - Implemented by refering to multiple applications and implementation of fitness and lifestyle apps and color pallets.
# Problems Faced (Frontend)
> Implementation of the countdown timer with any external services - Implemented using system time.
> Implementation of the download feature of the wallpapers - Implemented using download manager.
> Implementation of Achievements and Calender in stats - Implemented Achievements using Local Storage and Calender using API and a dependency.
