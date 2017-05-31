import sciter


class Frame(sciter.Window):

    def __init__(self):
        super().__init__(ismain=True, uni_theme=True)

    def on_script_call(self, name, args):
        # script calls
        print(name, "called from script")
        return self.dispatch(name, args)

    def on_subscription(self, groups):
        # subscribing only for scripting calls and document events
        from sciter.event import EVENT_GROUPS
        return EVENT_GROUPS.HANDLE_BEHAVIOR_EVENT | EVENT_GROUPS.HANDLE_SCRIPTING_METHOD_CALL

    def GetNativeApi(self):

        def on_exit():
            print("exiting...")
            exit(1)

        api = {'exit': on_exit}

        return api


if __name__ == '__main__':
    import os
    htm = os.path.join(os.path.dirname(__file__), 'html', 'minimal.html')
    frame = Frame()
    frame.load_file(htm)
    frame.run_app()

