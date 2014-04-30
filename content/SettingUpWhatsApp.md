Title: Setting Up WhatsApp on Your Computer
Date: 30-04-2014
Tags: WhatsApp, Yowsup, Ubuntu, Pidgin, Terminal
Categoyry: Blog,Pelican,Digital Ocean, VPS
Slug: whatsapp-on-laptop
Author: Kenneth Kinyanjui


## WhatsApp on your terminal


Two weeks ago I was using my dear [S3 mini](http://www.samsung.com/uk/consumer/mobile-devices/smartphones/android/GT-I8190RWABTU) but the unfortunate happended and it started restarting itself. Common 
problem with this phone model. So I took it to Samsung, hoping for a quick recovery. Unfortunately, this is the second time,
and I don't want any more Samsung products, especially after the experience with my S3 Mini.

With this situation, I had no other option but to go back to the only phone that has never let me down. Always been there
when times were hard and 2 months ago it turned 5. My [Nokia 2330c-2](http://www.gsmarena.com/nokia_2330_classic-2570.php). But apparently, I need a "smarter" phone, I 
borrowed my Mom's [Nokia Asha 200](http://www.gsmarena.com/nokia_asha_200-4281.php) , My main goal at least to get going with the trend Whatsapp. Everyone is using Whatsapp 
and its cheap to communicate using it. Groups are fun and its easier to talk to people on Whatsapp.

Unfortuantely, there is no WhatsApp support for the Nokia Asha 200. So what next? I don't want to be disconnected in the next couple of weeks.
I am sure you can picture this situation. So I "Googled" around and stumbled upon [OpenWhatsapp](http://openwhatsapp.org/) which happens to be a project that was 
opening up WhatsApp with their API. It is powered by [Yowsup](https://github.com/tgalal/yowsup) which is written in Python.

##Yowsup

This wonderful platform opened up with a couple of features:

1. Yowsup-cli
2. Yowsup-Library
3. The Documentation


What caught my attention was [Yowsup-cli](https://github.com/tgalal/yowsup/wiki/yowsup-cli) which is the command-line front-end that allows you to jump into using Whatsapp
service directly from the terminal. So yes if you are not afraid of the terminal then you will get your hands dirty with this on
the fly. 

With the current documentation, it might be a bit tricky to get going, so I will try to make it simple for you to set up the 
yowsup-cli on your terminal and start chatting with your friends if you don't have WhatsApp installed.


## Requirements

 * python 2.6+
 * [python-dateutil](http://labix.org/python-dateutil)
 * [argparse](http://code.google.com/p/argparse/) for python < 2.7
 * [libxml2](http://www.xmlsoft.org/python.html) only if using --v1 flag

Get an extra sim card that you are not using since Whatsapp does not allow you to sign in on
multiple accounts simultaneously. 

I will walk you through the installation and configuration process


## Installation

```
# apt-get install python python-dateutil python-argparse
# wget https://github.com/tgalal/yowsup/archive/master.zip
# unzip master.zip
# cd yowsup-master/src
```

## Configuration

You will need a configuration file that has your login details and we get this from the src/ directory 
which contains the config.example file

```
# cp config.example yowsup-cli.config
# cat yowsup-cli.config
```

### Details of the Config file

```
cc=254  -----> This is the Country code, do not include the "+" sign
phone=254123456789 ----> This is the Phone number with no "+" sign
id= -----> This is where you insert your  IMEI number
password=  -----> Password goes here, wait we will get there in the next steps
```

### Requesting the Registatation Code

You will need to change the mode of the config file to executable. Then, request for the code

```
# chmod +x yowsup-cli
# ./yowsup-cli --requestcode sms --config yowsup-cli.config
```

You should receive this on your terminal
```
status: sent
retry_after: 3605
length: 6
method: sms
```

### Registering the Code 

You will receive a message with the registration code and it will be in this format XXX-XXX

```
# ./yowsup-cli --register XXX-XXX --config yowsup-cli.config
```

Immedaitely, you will receive something on your terminal close to what is below here
```
status: ok
kind: free
pw: Q2nBGCvZhb7TBQrcm2sQCfSLgXM=     -----> Finally here is your password
price: 0,89
price_expiration: 1362803446
currency: EUR
cost: 0.89
expiration: 1391344106
login: 34123456789
type: new
```

There you have it now you have a WhatsApp password 

So go back to your yowsup.config file and put in the new password

```
# cat yowsup-cli.config
```

Then 

```
cc=254 
phone=254123456789 
id=
password= Q2nBGCvZhb7TBQrcm2sQCfSLgXM=

```


With that you can now send a message .

## Sending a message

I read the docs and found added the command and have this one liner that you can use to send messages

```
./yowsup-cli --send 254111222333 "Test message" --wait --config yowsup-cli.config
```

You should see this

```
Connecting to c.whatsapp.net
Authed 254123456789
Sent message
Got sent receipt
```


Receiving messages

You will receive all messages that have been sent to you directly

```
# ./yowsup-cli --listen --autoack --keepalive --config yowsup-cli.config
```

This should appear follow by a stream of messages sent you 

```
Connecting to c.whatsapp.net
Authed 254123456789
2544111222333@s.whatsapp.net [02-02-2013 14:14]:I have received a test message
```


## Interactive messaging

So you want to chat with your friend and instantly reply to them then use this script

```
./yowsup-cli --interactive 254111222333 --wait --autoack --keepalive --config
 yowsup-cli.config
```

```
Connecting to c.whatsapp.net
Authed 2544123456789
Starting Interactive chat with 254111222333
Enter Message or command: (/available, /lastseen, /unavailable)
Hi, I am talking via my terminal
254123456789 [02-02-2013 14:15]:Hi, I am talking via my terminal
Enter Message or command: (/available, /lastseen, /unavailable)
254111222333@s.whatsapp.net [02-02-2013 14:16]:What?
Enter Message or command: (/available, /lastseen, /unavailable)
Testing a new application
254123456789 [02-02-2013 14:16]:Testing out WhatsApp on my terminal
Enter Message or command: (/available, /lastseen, /unavailable)
/unavailable
```


## Pidgin Whatsapp


While many of you do not enjoy using the terminal there was someone who built a 
pidgin plugin that allows you to chat easily using Pidgin


Simply run through the process using Yowsup.
Username = 25412345678
Password = Q2nBGCvZhb7TBQrcm2sQCfSLgXM=


Download Pidgin on your machine.


### Ubuntu Users

```
sudo add-apt-repository ppa:whatsapp-purple/ppa
sudo apt-get update
sudo apt-get install pidgin-whatsapp
```

Simply sign in on whatsapp with the credentials and you are good to go


## References

[Yowsup on Github](https://github.com/tgalal/yowsup/wiki/yowsup-cli)

[Article on Setting up](Securityandrisk.blogspot.com/2013/07/whatsapp-via-python-open-security.html)

[WhatApp with Pidgin](http://samtinkers.wordpress.com/2014/01/11/install-whatsapp-on-ubuntu-12-04-12-10-13-04-13-10-mint-13141516)