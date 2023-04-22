import re
import json

def commit_check(message, regex):

    try:
        #find the match using regex with the latest commit message
        result = re.search(r"{regex}", message)
        if result:
            print("validation not successful")
            output = "pattern" + regex + " is not available in the commit message " + message
            raise ValueError(output)
        else:
            print("validation successful")
            print("pattern" + regex + " is available in the commit message " + message )
                
    except Exception as e:
        return('Error')
        raise e
