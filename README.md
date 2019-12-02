# HoosRiding -- A ride share application for UVA students

The purpose of this web application is to provide connections between UVA students who are looking to carpool between
their homes and Charlottesville. Users can host rides as well as request a seat as a passenger from another driver.

## Usage

This web application is hosted using Heroku. To access this app, please visit this link: `https://project-103-jawgz.herokuapp.com/`.

## Features

The HoosRiding application has many features that will make this product useful, secure, and efficient.

### Login

Our team implemented Google's social authentication as a means to login and store user data.
To enhance security, only users with an @virginia.edu email address will be able to log in. This ensures that this
application is only used by members of the UVA community.
Using Google social authentication is also efficient for the user because it connects this new account to a previously
existing account, and will automatically sign in if a valid email address is recognized and active in that browser.

### Find A Ride Page

The main page of this website is the "Find a Ride" page. Here, all of the currently active rides are displayed, automatically
sorted by the date of the ride.
On the sidebar, the user is able to both sort and search through the different rides to facilitate the search process.
The user is able to sort by Posting Date, Riding Date, and Price. If the user clicks on the filter multiple times,
they are able to change the direction of the sort (i.e. highest prices first will change to lowest prices first).
Users are also able to search for a ride based on their starting location, end location, and the date of the ride.

Users may request to join any ride that has available seats, as any rides with no seats available will not be displayed
on this page. When a user requests to join a ride, the request is sent to the driver, who is then able to accept or
decline that rider. This information on both the passenger and driver side is displayed on the "My Rides" page.

Each ride will display relevant profile information for the driver and the riders. In the details section, users will
find information on other riders as well as a generated route using the Google Maps API.

### Post A Ride

A driver is able to post their ride information on this page. The Google Places API was implemented to auto-complete
and verify the starting and ending locations for the drive.
There is form validation. You are unable to submit the form if required fields are not filled out, and you are unable to
post a ride from a date in the past.
When the driver submits the form, they are redirected to the "Find a Ride" page, where their new ride will be displayed.

### My Rides

The "My Rides" page of HoosRiding has many features including an editable profile, passenger information, and driver
information and actions.

#### Edit your profile

When you log on, the name and email are obtained from the Google Social Authentication process. Users have the option
to add other information (cell number, car make/model, and license plate) to their profile that will be displayed on any
rides they host.
Users can also upload a profile picture. These images are stored in an AWS S3 bucket.
The user rating is generated based on all of the rides the user has previously hosted.

#### Passenger view

On Passenger view, a user is able to view both their past and future rides. Users are able to see their status on the
ride (pending, accepted, or declined) based on the response from the driver. A rider is also able to remove themselves
from a certain ride if they choose. Users can only remove themselves from a ride if it has not happened yet.
If you were accepted on a certain ride, and it has already happened, a rider is able to rate their ride. This rating
will then update the profile of the driver. A rider can only rate a ride one time.

#### Driver View

In Driver view, a user is also able to see both past and future rides. In Future Rides, drivers see all incoming rider
requests. They are able to either accept or decline riders. As they accept riders, the number of available seats on the
ride adjust accordingly. Drivers are also able to delete active rides, but not rides from the past.
