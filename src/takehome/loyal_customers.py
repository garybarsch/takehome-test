#
# Problem:
# We have a website that tracks the pages customers are viewing.
# Every time somebody comes to the website, we write a record to a log file
# consisting of the day, page_id, and customer_id. Each field is separated by a
# space delimiter.
#
# Example data:
#   day1 111 page1
#   day1 233 page2
#   day1 410 page2
#   day1 111 page1
#   day2 111 page2
#   day2 233 page1
#
# Given two log files, day1.log and day2.log, read these files and generate a
# list of "loyal customer" customer_ids that match the following criteria:
#   1) they visited the website on both day1 and day2.
#   2) they visited at least two unique pages.
#
# Description:
#   - You will be given a string of log data.
#   - Use this string to find loyal customers that meet both criteria 1 and 2 above.
#   - Return a unique list of loyal customer_ids, sorted ascending order.
#
# TODO: implement find_loyal_customers()
#


def find_loyal_customers(log_data: str) -> list[str]:
    """
    Args:
        log_data (str): The entire contents of a log file as a string.

    Returns:
       list[str]: A sorted list of loyal customer IDs found in the log_data.
    """
    customer_ids = ["example_id1"]
    # TODO: add your code here
    return customer_ids


def hello_world():
    # TODO: remove me or add a new test
    return "Hello, World!"
