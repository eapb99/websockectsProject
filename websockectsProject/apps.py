from notify import signals


def ready(self):
    signals.announce_new_user()