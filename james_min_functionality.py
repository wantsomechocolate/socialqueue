
from datetime import datetime
from datetime import timedelta
from random import randrange


## Information we need:


## Main source of contacts is google contacts (because a lot of people
## already have those

## Additional info about particular users will be stored somewhere as well
dct = {'user_ref':1, 'google_contact_ref':'whatever','contact_frequency':180,'location':'San Francisco', 'contact_blacklist':[], 'interest_tags':['chocolate','anime'] , 'last_contact_date':None , 'randomization':20, 'next_contact_date':None}


## We also need some info about the person using the app, but it's probably better to assume some defaults than force the user to give information
## When you prefer to contact people, the method you prefer to use, etc.


## Do we need to store a map of users to contacts? If they already have that information in their phone, I guess in the additional info source we'd need to know which of our users contacts it is, is that a security issue
## Should we have a different database table for each user? is that more secure?


##James min functionality is something that reminds the user that they haven't reached out to X in a while. a while defined by the app. (default 6 months) (can look at nearest holiday, birthday)

## In order to do this, I need the last time that the person was contacted, if there is no last time, use the frequency devided by 2 as the estimate of the next date
## Then adjust the date with a 20% adjustable variability


dct['next_contact_date'] = dct['last_contact_date'] + timedelta(days=dct['contact_frequency']*(1+(randrange(-1*dct['randomization'],dct['randomization'])/100))) if dct['last_contact_date'] else datetime.utcnow() + timedelta(days=(dct['contact_frequency']/2)*(1+(randrange(-1*dct['randomization'],dct['randomization'])/100)))
print(dct['next_contact_date'])
dct['last_contact_date'] = dct['next_contact_date']

dct['next_contact_date'] = dct['last_contact_date'] + timedelta(days=dct['contact_frequency']*(1+(randrange(-1*dct['randomization'],dct['randomization'])/100))) if dct['last_contact_date'] else datetime.utcnow() + timedelta(days=(dct['contact_frequency']/2)*(1+(randrange(-1*dct['randomization'],dct['randomization'])/100)))
print(dct['next_contact_date'])
