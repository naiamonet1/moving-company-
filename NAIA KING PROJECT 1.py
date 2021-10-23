return_to_warehouse = 0
total_storage = [ ]
AT_WAREHOUSE = 0
STORAGE_SPACE = 1600



while return_to_warehouse <=3 and AT_WAREHOUSE == 0:

  pickup_location = float(input("Where is the next pickup? "))
  print()

  pickup_size = float(input("How large is the next pickup? "))
  print()

  next_pickup_request_max = pickup_location + 2

  next_pickup_request_min = pickup_location - 2
  #I'm having trouble with making a variable where the next pickup location is within 2 miles of the current location

  miles_from_warehouse = pickup_location + 5 or pickup_location -5
  #I'm having trouble with making a variable where the pickup location is within 5 miles of the warehouse

  miles_from_warehousee = 5


  if (-10 <= pickup_location <= 10) and (0 <= pickup_size <= 1600) and (sum(total_storage) < 1600):

    print("Pickup at:", pickup_location,",", "Size", pickup_size, "cubic feet")
    
    total_storage.append(pickup_size)
    
    print(sum(total_storage))
    
    space_left = STORAGE_SPACE - pickup_size


  elif (pickup_size > 1600) or (pickup_location > next_pickup_request_max) or (pickup_location < next_pickup_request_min):
  #code won't decline orders > 10 miles away as well as orders <-10 miles away
    
    print("Declined.")
    
    print("Drop off size:", sum(total_storage), "cubic feet")
    
    return_to_warehouse += 1
  

  elif (pickup_location < -10) or (pickup_location > 10) or (sum(total_storage) == 1600):
   
    print("Declined.")
  
    print("Drop off size:", sum(total_storage), "cubic feet")
    
    return_to_warehouse += 1


  if return_to_warehouse == 3:
    
    print("All done. Total storage amount:", sum(total_storage), "cubic feet")
    break




  