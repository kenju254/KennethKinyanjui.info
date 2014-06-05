Title: Installing  Ubuntu/Debian and ChromeOS on Samsung ChromeBook Series 5
Date: 06-05-2014
Tags: ChromeBook, Ubuntu, ChromeOS, Hardware
Category: ChromeBook, OS, 
Slug: installing ubuntu on Chromebook
Author: Kenneth Kinyanjui
Summary: Brief overview of moving to Dual Boot

## Introduction

I happened to get lucky to own a Chromebook as a gift from [Google](http://google.com) courtesy of  [Sam Dutton](http://www.samdutton.com/). To
imagine how a simple request for Chrome Stickers as Swag(Swag is a word used by Google to mean the Googly stuff) , ended up to a couple of other GDGs and I receiving 
some [Samsung Series 5 Chromebooks](http://www.amazon.com/Samsung-Series-12-1-Inch-Chromebook-Silver/dp/B004Z6NU70) as Swag.  No stickers but I sure did come back to Kenya with a Chromebook.  Thanks [Google](http://www.google.com) and[ GDG](http://developers.google.com/groups)

As a developer, I have always wished to own a super-light weight computer that can do assist me in all my needs. Why not get a MacBook Air? Have
you seen the [pricetag](http://www.apple.com/macbook-air/) on it. So I had started saving up for one and I got the ChromeBook first.

I own a [HP Probook 4530s](http://h20566.www2.hp.com/portal/site/hpsc/public/psi/manualsResults/?lang=en&cc=us&sp4ts.oid=5060880) running both Ubuntu and Windows 8 on Dual boot. Call it an act of having a Swiss Army Knife, having both OSs counts in my situation. So we are on [Chromebooks](http://www.samsung.com/us/computer/chrome-os-devices/XE503C32-K01US) and not my HP. 

ChromeOS is built on top of the Linux Kernel and what a marvelous OS they have built. But for  a developer I could not be able to transform it to my environment when running plainly on ChromeOS. So what next? Two Options. 

 1. Installing CrUbuntu alongside ChromeOS
 2. Installing Ubuntu/Debian based using Crouton

## Installing CrUbuntu alongside ChromeOS

REMEMBER TO REDEEM YOUR 100 GB THAT COMES WITH ALL CHROMEBOOK BEFORE DOING ANYTHING

At the time I got my Chromebook, the only way to do this was installing CrUbuntu which is a customized 12.04 32 Bit for the 
Chromebook. I tried the installation process managed hacking through and though I did it basing on my experience, I will not 
recommend this as the option to take while you want to exploit both ChromeOS and CrUbuntu.

### Success

1. Got Ubuntu working finally
2. Running Ubuntu on its own.

### Down Side

1. Very poor performance
2. Low space since you get 8 GB for ubuntu and cannot access the rest that lives within ChromeOS
3. Constant unresponsiveness due to hardware contraints


With such kind of downside I could not stand working with the machine, since performance happens to be an
important factor when you are a developer. Also I couldn't stand using it with such kind of effects 
especially the unresponsiveness.


If you still want to install CrUbuntu there is plenty of resources I will point out that you can use.

1. [Raywaldo's Ubuntu on Chromebook](http://raywaldo.com/2013/01/howto-ubuntu-on-chromebook/)
2. [Video illustrating the whole process](https://www.youtube.com/watch?v=9I_efUuizFk)

So what next? I opted to recover chrome and find another solution to this problem and found a tool called Crouton

## Using Crouton

So Crouton is a tool that was developed by a Googler, [David Schneider](https://github.com/dnschneid), It is for those,
who would like to run straight Linux from there Chromium OS device and do not care about physical security.
[More](https://github.com/dnschneid/crouton)

### Getting into Developer Mode

While many own this devices, not many know that there is actually a developer mode. For sure, I didn't.

There are two modes 

1. Normal user mode
2. Developer mode

More on *Developer Mode* is [here](http://www.chromium.org/chromium-os/chromiumos-design-docs/developer-mode)

To get into developer mode depend on the device, I will talk about my Samsung Chromebook Series 5. 

PLEASE BE VERY CAREFUL WHEN SWITCHING INTO DEVELOPER MODE AND BACK

![Getting into the Developer mode](/images/developermode.jpg)

After doing this, REBOOT and you will get a warning screen telling you that OS verification is turned off.
Simply, press CTRL+D and you will boot into ChromeOS.

Developer Modes vary and you can check out [here](http://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices)
for the exact way to get into development mode for your device.

####  Install Ubuntu with Crouton

##### (i) Download Crouton

Download Crouton from [here](http://goo.gl/fd3zc) and make sure it is saved in your Downloads folder.

##### (ii) Install Ubuntu

Start the Crosh terminal with CTRL + ALT + T, then type "shell".

Crouton by default, install Ubuntu 12.04 LTS (Precise). You can view a list of supported
Ubuntu flavours by running

```
# sh -e ~/Downloads/crouton -r list
```

While using Developer Mode, you will not be prompted for a passoword while using "sudo" in the Chrome OS terminal. For this, encrypting the chroot with "-e" is highly recommended.


__NOTE__ :
__For ARM chromebooks__ it is important that __Unity only works on Ubuntu 12.04__ . Reason being , __only UNITY 2D __ works
due to Xephyr lacking EGL support. It took me a week to figure this our since everything else kept breaking.



Ubuntu can be installed using __Unity__ or __Xfce__  

__To install Ubuntu 12.04 with Unity (2D)__ enabling ecryption the following commands will be used 

```
# sudo sh -e ~/Downloads/crouton -r precise -t unity -e
```

__ To install Ubuntu 12.04/14.04/ using __Xfce__ enabling encryption the following commands will be used repectively

```
# sudo sh -e ~/Downloads/crouton -r precise xfce -e
```

```
# sudo sh -e ~/Downloads/crouton -r trusty xfce -e
```

You have been able to set up __xfce__ and __Unity__, this is not the end, you can install __gnome(GNOME Shell), cinnamon, kde,lxde__

The commands initiated will start the download and installation process on your chromebook. On completion, you will be 
expected to enter either a username or a password for your new Ubuntu installation

##### (iii) Start Ubuntu

To start __Unity__ :

1.Enter **CTRL + ALT + T**  to enter Chrome OS Terminal
2.type "shell"

```
# sudo startunity
```

Alternatively 

To start __Xfce__ :
1.Enter **CTRL + ALT + T**  to enter Chrome OS Terminal
2.type "shell"

```
# sudo startxfce4
```

You can now switch in between Chrome OS and Ubuntu:

###### ARM-based Chromebooks
```
Ctrl + Alt + Shift + Back
```
```
Ctrl + Alt + Shift + Forward
```

###### x86-Based Chromebooks
```
Ctrl + Alt + Back
```
```
Ctrl + Alt + Forward
```

also
```
Ctrl + Alt + Refresh 
```

To simply __exit Ubuntu Desktop__ , select __Logout__

I will next on write a post on what to do after installing Ubuntu on your Chrombook