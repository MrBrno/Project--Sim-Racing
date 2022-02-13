################################
# ACKissmyrank AppLink Example App
# Author: Brioche
# License: This app is a Example. No warranty. Do whatever you like :).
################################

# noinspection PyUnresolvedReferences
import ac
# noinspection PyUnresolvedReferences
import acsys
import sys
import os
import platform
import re
import time

if platform.architecture()[0] == "64bit":
    sys.path.insert(len(sys.path), 'apps/python/ac_kissmyrank_applink_example/stdlib64')
else:
    sys.path.insert(len(sys.path), 'apps/python/ac_kissmyrank_applink_example/stdlib')
os.environ['PATH'] = os.environ['PATH'] + ";."

import socket

# import winsound

# globals
kmr_applink_app_id = "ac_kissmyrank_applink_example"
kmr_applink_connected = 0
kmr_applink_ip = ""
kmr_applink_port = 0
kmr_applink_token = ""
kmr_applink_sock = 0
kmr_applink_chat_fail_counter = 99
# and now some app secific stuff
app_on = 1
timer = 0
started = 0
info_label = []


def acMain(ac_version):
    global info_label
    # let's see if we screwed up
    ac.console("ACKissmyrank AppLink Example or nothing.")
    # set it up
    appWindow = ac.newApp("ACKissmyrank AppLink Example")
    ac.setTitle(appWindow, "ACKissmyrank AppLink Example")
    ac.setIconPosition(appWindow, 0, -6000)
    ac.setSize(appWindow, 300, 300)
    ac.drawBorder(appWindow, 0)
    ac.setBackgroundOpacity(appWindow, 1)
    ac.addOnAppActivatedListener(appWindow, onAppOn)
    ac.addOnAppDismissedListener(appWindow, onAppOff)
    # ac.addRenderCallback(appWindow, onRender)
    ac.addOnChatMessageListener(appWindow, onMessage)
    # create some labels to play with
    for i in range(0, 9):
        info_label.append(ac.addLabel(appWindow, "empty"))
        ac.setPosition(info_label[i], 3, 30 + i * 30)
    return "ACKissmyrank AppLink Example"


def acUpdate(deltaT):
    global kmr_applink_sock, kmr_applink_connected, info_label, timer, started
    if kmr_applink_token:
        # AppLink is initialized
        timer += deltaT
        # 33 ms of relax
        if timer > 0.033 and kmr_applink_sock:
            # socket is there
            timer = 0
            try:
                # see if we received something
                data, addr = kmr_applink_sock.recvfrom(4096)
                if data:
                    # parse it
                    r = parseData(data)
                    if r:
                        # if it's an event the result array
                        # contains the event information (first item is the id,
                        # last item is the full message localized in the user language)
                        for i in range(0, len(info_label)):
                            # do something with the result
                            if i < len(r):
                                ac.setText(info_label[i], r[i])
                            else:
                                ac.setText(info_label[i], "empty")
            except:
                pass
    else:
        if not started:
            # app just launched, let's wait 6 seconds before sending the message to the chat
            if timer < 6:
                timer += deltaT
            else:
                # initialize the applink
                KMRAppLinkInitialize()
                started = 1


def onMessage(message, by):
    global kmr_applink_connected, kmr_applink_ip, kmr_applink_port, kmr_applink_token, \
        kmr_applink_sock, kmr_applink_app_id, kmr_applink_chat_fail_counter, timer
    if not kmr_applink_token and not kmr_applink_connected and by == "SERVER" and kmr_applink_chat_fail_counter < 9:
        # AppLink is not initialized but there is still hope (less than 9 messages since the request)
        m = re.search("AppLink: ([^:]+):([\d]+) ([^ ]+)$", message)
        if m:
            # this is the message we're looking for
            kmr_applink_ip = m.group(1)
            kmr_applink_port = int(m.group(2))
            kmr_applink_token = m.group(3)
            if app_on:
                # the app is active let's start the stream
                KMRAppLinkConnect()
        else:
            # too bad the message is not the right one, let's increment the fail counter
            kmr_applink_chat_fail_counter += 1


def parseData(data):
    global kmr_applink_position, kmr_applink_connected
    result = []
    if ord(data[0:1].decode("iso-8859-1")) == 1:
        # keepalive (currently only contains the Kissmyrank position)
        kmr_applink_position = ord(data[1:2].decode("iso-8859-1"))
        # if we're getting the keepalive we're connected
        kmr_applink_connected = 1
        return None
    else:
        # if we're here, it's an event
        start = 1
        while start < len(data):
            # let's parse it
            length = ord(data[start:start + 1].decode("iso-8859-1")) * 4
            ac.log(str(length))
            temp = data[start + 1:start + 1 + length]
            result.append(temp.decode("utf-32le"))
            start += 1 + length
        return result


def onAppOn(*args):
    global app_on
    app_on = 1
    if kmr_applink_token:
        # the AppLink was already initialized
        if not kmr_applink_connected:
            # but we're not connected, let's start the stream
            KMRAppLinkConnect()
    else:
        # the AppLink was not initialized, let's intialize it
        KMRAppLinkInitialize()


def onAppOff(*args):
    global app_on
    app_on = 0
    # let's stop the stream
    KMRAppLinkDisconnect()


def KMRAppLinkConnect():
    KMRAppLinkSetStatus(1)


def KMRAppLinkDisconnect():
    KMRAppLinkSetStatus(0)


def KMRAppLinkSetStatus(new_status):
    global kmr_applink_connected, kmr_applink_app_id, kmr_applink_ip, kmr_applink_port, kmr_applink_token, \
        kmr_applink_sock
    if kmr_applink_connected != new_status and kmr_applink_ip and kmr_applink_port and kmr_applink_token and len(
            kmr_applink_token) == 6:
        # we have everything we need
        if not kmr_applink_sock:
            # socket is not there, we need to create it
            kmr_applink_sock = socket.socket(socket.AF_INET,  # Internet
                                             socket.SOCK_DGRAM)  # UDP
            # we don't want to freeze AC
            kmr_applink_sock.settimeout(0.001)
            # let's leave the port choice to the operating system
            kmr_applink_sock.bind(("", 0))
        # let's create the request
        request = chr(len(kmr_applink_app_id)).encode('iso-8859-1') + kmr_applink_app_id.encode('utf-32le') + chr(
            len(kmr_applink_token)).encode('iso-8859-1') + kmr_applink_token.encode(
            'utf-32le') + chr(new_status).encode('iso-8859-1')
        # send it
        kmr_applink_sock.sendto(request, (kmr_applink_ip, kmr_applink_port))
        if not new_status:
            # if we are stopping the stream let's update the status
            kmr_applink_connected = new_status


def KMRAppLinkInitialize():
    global kmr_applink_chat_fail_counter
    # let's reset the fail counter
    kmr_applink_chat_fail_counter = 0
    # and send the initialization chat message
    ac.sendChatMessage("/kmr applink")
