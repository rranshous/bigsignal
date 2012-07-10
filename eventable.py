import logging

# TODO: use queue's so that events happen in the order
# they are fired

class Eventable(object):
    """
    base class for object you want to handle events
    uses a simple event tracking system
    """
    def __init__(self):
        self.__handlers = {}

    def on(self,event,handler):
        """
        add a listener
        """
        logging.debug('adding handler: %s' % event)
        self.__handlers.setdefault(event,[]).append(handler)
        return self

    def un(self,event,handler):
        """
        remove a listener
        """
        if event in self.__handlers:
            try:
                self.__handlers[event].remove(handler)
            except ValueError:
                pass # nothing to remove
        return self

    def fire(self,event,*args,**kwargs):
        """
        fire the event. aka call the handlers
        and pass them the args, kwargs
        """
        logging.debug('firing %s' % event)
        for handler in self.__handlers.get(event,[]):
            logging.debug('firing handler')
            handler(*args,**kwargs)
        return self

