# InfraFinder

Compares any amount of IP addresses to each other by grabbing the JSON output from censys and comparing them for matching values. 
Intended to find related infrastructure. 

Arguments are passed in via command line, can use defanged IPs. 


Script imports a secrets.py file that must be located with the script specifying the api_key and secret variables.

Outputs shared attributes amongst the given IPs in a user friendly search syntax that can be copied and pasted into censys search.

Run using ```./infrafinder.py 8.8.8.8 8.8.8.4 8.8.8.8```

or using the provider dockerfile:
```docker build . -t infrafinder && docker run infrafinder --rm 8.8.8.8 8.8.8[.]4```
