import boto3
import sys
# for pretty printing
from pprint import pprint

# create main method
def main(argv):

    # create a session to retrieve '<USER>' credentials from ~/.aws/credentials
    session = boto3.Session(profile_name='<USER>')

    # create a client with KMS
    kms = session.client('kms', region_name='us-east-1')

    # generate a temporary encryption/data key
    data_key = kms.generate_data_key(
        KeyId='<ARN OF YOUR KEY>',
        KeySpec='AES_256',
    )

    # Extract just the plaintext key
    plaintext_key = data_key["Plaintext"]

    print('')
    pprint(data_key)
    print('')
    print('')
    print(str(plaintext_key))
    print('')
    print('')
    # takes the 1st argument of the list
    print(argv[0])
    print('')
    print('')


# Execute this code only if you're running this program stand-alone,
# so don't run it if its being used as part of another program
if __name__ == "__main__":
    # Call the "main" function, pass all the command line arguments in order
    main(sys.argv[1:])
