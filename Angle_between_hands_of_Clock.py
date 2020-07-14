def angleClock(self, hour: int, minutes: int) -> float:
  minHand = 6 * minutes. # minute hand moves 6˚ in one minute
  hourHand = 0.5*( (60 * hour) + minutes) # hour hand moves 0.5˚ per minute
  diff =  max(minHand,hourHand)-min(minHand, hourHand)
  return min(360-diff,diff)
