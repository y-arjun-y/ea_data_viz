import time

most_recent_refresh = None


def refresh_data():
    global most_recent_refresh
    if most_recent_refresh and time.time() - most_recent_refresh < 60 * 60:
        return
    most_recent_refresh = time.time()
