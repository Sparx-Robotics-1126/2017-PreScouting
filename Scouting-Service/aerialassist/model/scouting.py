from google.appengine.ext import ndb

class ScoutingAuto(ndb.Model):
      portcullisPosition = ndb.IntegerProperty()
      chevalPosition = ndb.IntegerProperty()
      moatPosition = ndb.IntegerProperty()
      rampartsPosition = ndb.IntegerProperty()
      drawbridgePosition = ndb,IntegerProperty()
      sallyportPosition = ndb.IntegerProperty()
      rockwallPosition = ndb.IntegerProperty()
      roughterrainPosition = ndb.IntegerProperty()
      portcullisCrossed = ndb.BooleanProperty()
      chevalCrossed = ndb.BooleanProperty()
      moatCrossed = ndb.BooleanProperty()
      rampartsCrossed = ndb.BooleanProperty()
      drawbridgeCrossed = ndb.BooleanProperty()
      sallyportCrossed = ndb.BooleanProperty()
      rockwallCrossed = ndb.BooleanProperty()
      roughterrainCrossed = ndb.BooleanProperty()
      lowbarCrossed = ndb.BooleanProperty()
      boulderPickedUp = ndb.BooleanProperty()
      robotScoredHigh = ndb.BooleanProperty()
      robotScoredLow = ndb.BooleanProperty()
      endingPosition = ndb.StringProperty()
      reachAchieved = ndb.BooleanProperty()
      reachWasCrossAttempt = ndb.BooleanProperty()
      startedAsSpy = ndb.BooleanProperty()

class ScoutingTele(ndb.Model):
     highGoalAttempts = ndb.IntegerProperty() 
     highGoalsScored = ndb.IntegerProperty() 
     lowGoalAttempts = ndb.IntegerProperty() 
     lowGoalsScored = ndb.IntegerProperty() 
     portcullisCrosses = ndb.IntegerProperty() 
     chevalCrosses = ndb.IntegerProperty() 
     moatCrosses = ndb.IntegerProperty() 
     rampartsCrosses = ndb.IntegerProperty() 
     drawbridgeCrosses = ndb.IntegerProperty() 
     sallyportCrosses = ndb.IntegerProperty() 
     rockwallCrosses = ndb.IntegerProperty() 
     roughterrainCrosses = ndb.IntegerProperty() 
     lowbarCrosses = ndb.IntegerProperty() 
     playsDefense = ndb.BooleanProperty()
     bouldersPickedUp = ndb.IntegerProperty() 
     bouldersTakenToCourtyard = ndb.IntegerProperty() 
     bouldersReceivedFromBrattice = ndb.IntegerProperty() 
   
      
class ScoutingGeneral(ndb.Model): 
      numberOfPenalties = ndb.IntegerProperty()
      commentsOnPenalties = ndb.StringProperty()
      numberOfTechnicalFouls = ndb.IntegerProperty
      commentsOnTechnicalFouls = ndb.StringProperty()
      generalComments = ndb.StringProperty()


class Scouting(ndb.Model):
    nameOfScouter = ndb.StringProperty()
    teamKey = ndb.StringProperty()
    eventKey = ndb.StringProperty()
    matchKey = ndb.StringProperty()

    auto = ndb.StructuredProperty(ScoutingAuto, repeated=False)
    tele = ndb.StructuredProperty(ScoutingTele, repeated=False)
    general = ndb.StructuredProperty(ScoutingGeneral, repeated=False)
