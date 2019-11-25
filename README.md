# HoosRiding -- A ride share application for UVA students

Talk about purpose of the app here.

## Usage

Here is how to do it on local host. `link here`
Here is how to use it on Heroku. `link here`

## Features

We got lots of features

### Login

Google social auth, limited to UVA email addresses, will recognize if you are already signed link

### Find A Ride Page

"Home page" of the app, sorting (automatic sort), searching
Request to join a ride

### Post A Ride

Fill out the form, there is form validation
Can't post from a date in the past
use Google Places API to verify cities
Submit --> takes you back to find a ride page
*what does this do*

### Profile

you can do lots on your profile page

#### Edit your profile

Update your car and contact information
Rating is generated based on all of the rides you have hosted in the past.
Profile picture is stored in AWS S3 bucket

#### Passenger view

You can see future and past rides
You see your status on those rides --> accepted, declined or pending
Rate your ride --> if you were accepted on a ride, and the date has already passed, you are able to rate your driver.
This rating will update the profile of the driver.

#### DriverView

You can see future and past rides
you can see incoming requests for riders and either accept or decline them
you can delete them?
