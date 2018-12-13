from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core.events import AllSlotsReset, Restarted
from weather import Weather, Unit

class showRestaurants(Action):


    def name(self):

      return "action_show_restaurants"

    def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

      dispatcher.utter_message("searching restaurants.... ")

      # recent_message = (tracker.latest_message)['text']

      # if tracker.get_slot('project'):

      #     util.getQuery(recent_message, dispatcher, tracker.current_slot_values())

      #     # dispatcher.utter_message("project info being uttered ..")

      # else:
          
      #     dispatcher.utter_message("no project slot is filled inside action give project information action")

      return []


class tellWeather(Action):


    def name(self):

      return "action_tell_weather"

    def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

      dispatcher.utter_message("action tell weather")

      weather = Weather(unit=Unit.CELSIUS)
      
      # print ("tracker.get_slot('location') ", tracker.get_slot('location')[bool(tracker.get_slot('location'))])

      gpe = (tracker.get_slot('location'))

      result = weather.lookup_by_location(gpe)

      dispatcher.utter_message("result ")

      try:
        if result:

            condition = result.condition
            city = result.location.city
            country = result.location.country
            dispatcher.utter_message('It\'s ' + condition.text + ' and ' + condition.temp + '°C in ' +
                                     city + ', ' + country + '.')
        else:
            dispatcher.utter_message('We did not find any weather information for ' + gpe + '. Search by a city name.')

      except:

        dispatcher.utter_message("We did not find any weather information for" + gpe)
      return

'''
This class resets the slots
reset all the slots except project  
because this slot is not being used for other intents
'''

class ActionReset(Action):

    def name(self):
      return 'action_reset'


    def run(self, dispatcher, tracker, domain):

      return_slots = []

      for slot in tracker.slots:
        if slot != 'project':
          return_slots.append(SlotSet(slot, None))

      return return_slots