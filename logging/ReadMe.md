# Logging

## Description

This set of samples show how easy it is to use the logger instead of a print statement, for debugging. This is especially useful for running script that run on a schedule, or big ETL.

## Content

 - `simple_logging.py`: A basic logging configuration, that does not have to catch exceptions.
 - `simple_logging_error.py`: A basic logging configuration, that shows the best way to log exceptions.
 - `logging\simple_logging_from_config.py`: A demonstration of how to configure your logging from a configuration file.

## Why logging over print?

 - Logging can be configured to write to a file.
 - Logging allows you to easily control the level of detail returns by your logger without updating your code. No need to comment print statement to hide them.
 - Logging give you tons of information write from the get go. It can print out:
     - What file generated the logging message.
     - What line of code generated the message.
     - What function generated the message.

Logging also enables you to log all the exception and its stack trace in a single line of code, unlike print.

```Python
    try:
        dummy_module.dummy_error()
    except Exception as ex:
        logging.error(ex, exc_info=True)
        return -1
```

In a single line of code will return all of this information, that would be a lot more complicated to generate using a print statement.

```
2020-05-05 15:53:04,432-simple_logging_error.py-Line: 13 - Function: main-ERROR-Run into dummy error!
Traceback (most recent call last):
  File "d:/git/esri-canada-tech-trek-2020/logging/simple_logging_error.py", line 11, in main
    dummy_module.dummy_error()
  File "d:\git\esri-canada-tech-trek-2020\logging\dummy_module.py", line 8, in dummy_error
    raise Exception ("Run into dummy error!")
Exception: Run into dummy error!
```