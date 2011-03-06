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
        self.__handlers[event].setdefault(event,[]).append(handler)
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

    def fire(self,event,args,**kwargs):
        """
        fire the event. aka call the handlers
        and pass them the args, kwargs
        """
        for handler in self.__handlers.get(event,[]):
            handler(args,**kwargs)
        return self
