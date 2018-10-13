def caught_speeding(speed, is_birthday):
  if is_birthday==True:
    if speed <66:
      return 0
    elif speed<86:
      return 1
    else :
     return 2
  else : 
    if speed <61:
      return 0
    elif speed<81:
      return 1
    else :
     return 2
