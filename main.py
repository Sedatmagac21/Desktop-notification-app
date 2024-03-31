import time
import notify2
from topnews import topStories

# Specify the file path of the notification window icon
ICON_PATH = "full_path_to_icon_image.png"

# Fetch news items
news_items = topStories()

# Initialize the d-bus connection
notify2.init("News Notifier")

# Create a Notification object
notification = notify2.Notification(None, icon=ICON_PATH)

# Set urgency level
notification.set_urgency(notify2.URGENCY_NORMAL)

# Set the duration for the notification on screen
notification.set_timeout(10000)

for news_item in news_items:
    # Update notification data for the Notification object
    notification.update(news_item['title'], news_item['description'])

    # Show notification on screen
    notification.show()

    # Provide a short delay between notifications
    time.sleep(15)
