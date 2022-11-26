class Item():
    
    def __init__():
        ...
    #define method to convert an item to a json or dict 
    

    #   // Option 3: "message"
    #   // Only one of "trace", "trace_chain", "message", or "crash_report" should be present.
    #   // Presence of a "message" key means that this payload is a log message.
    #   "message": {

    #     // Required: body
    #     // The primary message text, as a string
    #     "body": "Request over threshold of 10 seconds",

    #     // Can also contain any arbitrary keys of metadata. Their values can be any valid JSON.
    #     // For example:

    #     "route": "home#index",
    #     "time_elapsed": 15.23

    #   }
    # // Optional: level
    # // The severity level. One of: "critical", "error", "warning", "info", "debug"
    # // Defaults to "error" for exceptions and "info" for messages.
    # // The level of the *first* occurrence of an item is used as the item's level.
    # "level": "error",

    # // Optional: timestamp
    # // When this occurred, as a unix timestamp.
    # "timestamp": 1369188822,

    # // Optional: code_version
    # // A string, up to 40 characters, describing the version of the application code
    # // Rollbar understands these formats:
    # // - semantic version (i.e. "2.1.12")
    # // - integer (i.e. "45")
    # // - git SHA (i.e. "3da541559918a808c2402bba5012f6c60b27661c")
    # // If you have multiple code versions that are relevant, those can be sent inside "client" and "server"
    # // (see those sections below)
    # // For most cases, just send it here.
    # "code_version": "3da541559918a808c2402bba5012f6c60b27661c",

    # // Optional: platform
    # // The platform on which this occurred. Meaningful platform names:
    # // "browser", "android", "ios", "flash", "client", "heroku", "google-app-engine"
    # // If this is a client-side event, be sure to specify the platform and use a post_client_item access token.
    # "platform": "linux",

    # // Optional: language
    # // The name of the language your code is written in.
    # // This can affect the order of the frames in the stack trace. The following languages set the most
    # // recent call first - 'ruby', 'javascript', 'php', 'java', 'objective-c', 'lua'
    # // It will also change the way the individual frames are displayed, with what is most consistent with
    # // users of the language.
    # "language": "python",

    # // Optional: framework
    # // The name of the framework your code uses
    # "framework": "pyramid",

    # // Optional: context
    # // An identifier for which part of your application this event came from.
    # // Items can be searched by context (prefix search)
    # // For example, in a Rails app, this could be `controller#action`.
    # // In a single-page javascript app, it could be the name of the current screen or route.
    # "context": "project#index",

class Report():
    ...