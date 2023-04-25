import re
import argparse

def commit_check(message, regex):

    try:
        #find the match using regex with the latest commit message
        if re.search(fr"{regex}", message):
            print("validation successful")
            print("pattern " + regex + " is available in the commit message " + message )
        else:
            print("validation not successful")
            print("pattern " + regex + " is not available in the commit message " + message )
            output = "pattern " + regex + " is not available in the commit message " + message
            raise ValueError(output)
            
    except Exception as e:
        return('Error: ' + str(e))


parser = argparse.ArgumentParser(description="Commit message validation. Send regex and message to validate")
parser.add_argument("regex", type=str)
parser.add_argument("message", type=str)
args = parser.parse_args()
commit_check(args.message, args.regex)
