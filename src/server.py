#!/usr/bin/python

import sys

sys.path.append('./gen-py')

from recommenderservice import Recommender
from recommenderservice.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class RecommenderHandler(object):
    def __init__(self):
        pass

    def ping(self):
        print('ping()')

    def fetchRec(self,req):

        print("get the rec request ...")
        # TODO 调用离线推荐列表数据

        # TODO 调用用户画像数据
        return [req.ad_id,req.user_id, req.cityName, req.category]

def main():
    handler = RecommenderHandler()
    processor = Recommender.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    #server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    server = TServer.TThreadPoolServer(processor,transport,tfactory, pfactory)
    server.serve()

if __name__ == '__main__':
    main()