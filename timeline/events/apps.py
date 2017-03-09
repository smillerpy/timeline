from django.apps import AppConfig

class EventsConfig(AppConfig):
    name = 'timeline.events'
    verbose_name = "Events"

    def ready(self):
        """Override this to put in:
            Events system checks
            Events signal registration
        """
        pass
