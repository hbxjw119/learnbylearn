#!/usr/bin/python
# coding=utf-8
__author__ = 'hbxjw119'

import SocketServer
import re
import socket


class ClientError(Exception):
    pass


class PythonChatServer(SocketServer.ThreadingTCPServer):
    def __init__(self, server_addr, RequestHandlerClass):
        SocketServer.ThreadingTCPServer.__init__(self, server_addr, RequestHandlerClass)
        self.users = {}


class RequestHandler(SocketServer.StreamRequestHandler):
    NICKNAME = re.compile(r'^\w+$')

    def handle(self):
        self.nickname = None

        self.privateMessage('who are you?')
        nickname = self._readline()
        done = False
        try:
            self.nickCommand(nickname)
            self.privateMessage('hello %s,welcome to the chatroom' % nickname)
        except ClientError, e:
            self.privateMessage(e.args[0])
            done = True
        except socket.error:
            done = True

        while not done:
            try:
                done = self.processInput()
            except ClientError, e:
                self.privateMessage(str(e))
            except socket.error:
                done = True

    def finish(self):
        if self.nickname:
            message = '%s has quit: %s.' % (self.nickname, self.partingWords)
            self.broadcast(message, False)

        if self.server.users.get(self.nickname):
            del self.server.users[self.nickname]

        self.request.shutdown(2)
        self.request.close()


    def _readline(self):
        return self.rfile.readline().strip()

    def nickCommand(self, nickname):
        """
        this function allow to change the name
        /nick newname
        """

        if not nickname:
            raise ClientError('no nickname provided!')
        if not self.NICKNAME.match(nickname):
            raise ClientError('invalid nickname!')
        if nickname == self.nickname:
            raise ClientError('you are already known as %s' % nickname)
        if self.server.users.get(nickname, None):
            raise ClientError('there is already a user named %s here!' % nickname)
        oldNickname = None
        if self.nickname:
            oldNickname = self.nickname
            del self.server.users[self.nickname]
        self.server.users[nickname] = self.wfile
        self.nickname = nickname
        if oldNickname:
            self.broadcast('%s is now kown as %s' % (oldNickname, self.nickname))

    def quitCommand(self, partingWords):
        """
        quit the chatroom
        /quit quitmessage
        """

        if partingWords:
            self.partingWords = partingWords
        return True

    def namesCommand(self, ignored):
        """
        show all the person name
        /names
        """

        self.privateMessage(', '.join(self.server.users.keys()))

    def privateCommand(self,arg):
        """
        this function allow to send a message to a choose person
        /private name msg
        """

        name = arg.split(' ')[0]
        message = arg.split(' ')[1]
        message = self._ensureNewline(message)
        if name not in self.server.users.keys():
            raise ClientError('there is nobody named %s' % name)
        for user,output in self.server.users.items():
            if user == name:
                l = '<%s> %s\n' % (self.nickname,message)
                output.write(l)

    def processInput(self):
        done = False
        l = self._readline()
        command, arg = self._parseCommand(l)
        if command:
            done = command(arg)
        else:
            l = '<%s> %s\n' % (self.nickname, l)
            self.broadcast(l)
        return done

    def broadcast(self, message, includeThisUser=False):
        message = self._ensureNewline(message)
        for user, output in self.server.users.items():
            if includeThisUser or user != self.nickname:
                output.write(message)

    def privateMessage(self, message):
        self.wfile.write(self._ensureNewline(message))

    def _parseCommand(self, input):
        commandMethod, arg = None, None
        if input and input[0] == '/':
            if len(input) < 2:
                raise ClientError('invalid command!')
            commandAndArg = input[1:].split(' ', 1)
            if len(commandAndArg) == 2:
                command, arg = commandAndArg
            else:
                command, = commandAndArg

            commandMethod = getattr(self, command + 'Command', None)
            if not commandMethod:
                raise ClientError('no such command!')

        return commandMethod, arg

    def _ensureNewline(self, message):
        if message and message[-1] != '\n':
            message += '\r\n'
        return message


if __name__ == '__main__':
    PythonChatServer(('127.0.0.1', 8000), RequestHandler).serve_forever()
