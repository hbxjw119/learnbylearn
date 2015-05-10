#!/usr/bin/python
# coding=utf-8
__author__ = 'Administrator'

import socket
import select
import sys
import os
from threading import Thread


class ChatClient:
    def __init__(self, host, port, nickname):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.input = self.socket.makefile('rb', 0)
        self.output = self.socket.makefile('wb', 0)

        # send the given name to the server.
        authenticationDemand = self.input.readline()
        if not authenticationDemand.startswith('who are you?'):
            raise Exception('this does not a python chat server!')
        self.output.write(nickname + '\r\n')
        response = self.input.readline().strip()
        if not response.startswith('hello'):
            raise Exception(response)
        print response

        # print the list of members
        self.output.write('/names\r\n')
        print 'currently in the chat room:', self.input.readline().strip()

        self.run()

    def run(self):
        """
        start a thread to gather the input from the keyboard
        :return:
        """
        propagateStandardInput = self.PropagateStandardInput(self.output)
        propagateStandardInput.start()

        inputText = True
        while inputText:
            inputText = self.input.readline()
            if inputText:
                print inputText.strip()

        propagateStandardInput.done = True

    class PropagateStandardInput(Thread):
        """
        a class that mirrors standard input to the chat server
        """

        def __init__(self, output):
            Thread.__init__(self)
            self.setDaemon(True)
            self.output = output
            self.done = False

        def run(self):
            while not self.done:
                inputText = sys.stdin.readline().strip()
                if inputText:
                    self.output.write(inputText + '\r\n')


if __name__ == '__main__':
    import sys

    nickname = sys.argv[1]

    ChatClient('localhost', 8000, nickname)






