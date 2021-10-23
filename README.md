# moving-company-
You’ve recently founded your own moving and storage company, and bought a moving truck as well. The service you offer is picking up items from customers’ homes and storing them in your warehouse. The unique part of your service is that it’s on-demand — customers can request a pickup at any time, and those requests will enter a queue within your system. 


When a customer enters a request, you see how far they live west or east of your warehouse, and how many cubic feet their belongings take up. Your teammate helps you out by sending you the next request on the list, whenever you ask for it. 

If you’re at the warehouse, you’re willing to travel up to 5 miles from the warehouse to accept a new job. Similarly, before you leave someone’s house, you check if the next request is within 2 miles from the current spot or on the
way back to the warehouse: if so, you’ll attempt to complete the next job before storing it all; if not, that request is forever declined. 

You do not, however, take any jobs greater than 10 miles from the warehouse. And be careful to not take any jobs that will overflow your truck! You do as many pickups per day as possible, but only finish your workday after returning to the warehouse 3 times.

PROJECT DETAILS:

• Your moving truck is quite large, and has 1,600.0 cubic feet of storage
space.

• Only when you ask for the two inputs should your teammate give you the
following:

  1. One response that says the location of the pickup as a negative or positive float, meaning how far west or east (respectively) the pickup location is from the warehouse

  2. One response that says the total size of the pickup as a positive float (in cubic feet)

• Once you are done for the day, print that your workday is over and how much stuff you stored in the warehouse that day.

