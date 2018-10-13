def cigar_party(cigars, is_weekend):
  if is_weekend ==True and cigars>39:
    return True
  elif   is_weekend ==False and (cigars>39 and cigars<61):
    return True
  else :
   return False
