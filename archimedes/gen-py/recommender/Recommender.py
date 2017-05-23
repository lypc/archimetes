#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport


class Iface(object):
    def ping(self):
        pass

    def fetchRecByItem(self, req):
        """
        Parameters:
         - req
        """
        pass

    def fetchRecByUser(self, req):
        """
        Parameters:
         - req
        """
        pass

    def fetchRecByMult(self, req):
        """
        Parameters:
         - req
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def ping(self):
        self.send_ping()
        return self.recv_ping()

    def send_ping(self):
        self._oprot.writeMessageBegin('ping', TMessageType.CALL, self._seqid)
        args = ping_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_ping(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = ping_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "ping failed: unknown result")

    def fetchRecByItem(self, req):
        """
        Parameters:
         - req
        """
        self.send_fetchRecByItem(req)
        return self.recv_fetchRecByItem()

    def send_fetchRecByItem(self, req):
        self._oprot.writeMessageBegin('fetchRecByItem', TMessageType.CALL, self._seqid)
        args = fetchRecByItem_args()
        args.req = req
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_fetchRecByItem(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = fetchRecByItem_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.sys_exc is not None:
            raise result.sys_exc
        if result.code_exc is not None:
            raise result.code_exc
        raise TApplicationException(TApplicationException.MISSING_RESULT, "fetchRecByItem failed: unknown result")

    def fetchRecByUser(self, req):
        """
        Parameters:
         - req
        """
        self.send_fetchRecByUser(req)
        return self.recv_fetchRecByUser()

    def send_fetchRecByUser(self, req):
        self._oprot.writeMessageBegin('fetchRecByUser', TMessageType.CALL, self._seqid)
        args = fetchRecByUser_args()
        args.req = req
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_fetchRecByUser(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = fetchRecByUser_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.sys_exc is not None:
            raise result.sys_exc
        if result.code_exc is not None:
            raise result.code_exc
        raise TApplicationException(TApplicationException.MISSING_RESULT, "fetchRecByUser failed: unknown result")

    def fetchRecByMult(self, req):
        """
        Parameters:
         - req
        """
        self.send_fetchRecByMult(req)
        return self.recv_fetchRecByMult()

    def send_fetchRecByMult(self, req):
        self._oprot.writeMessageBegin('fetchRecByMult', TMessageType.CALL, self._seqid)
        args = fetchRecByMult_args()
        args.req = req
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_fetchRecByMult(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = fetchRecByMult_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.sys_exc is not None:
            raise result.sys_exc
        if result.code_exc is not None:
            raise result.code_exc
        raise TApplicationException(TApplicationException.MISSING_RESULT, "fetchRecByMult failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["ping"] = Processor.process_ping
        self._processMap["fetchRecByItem"] = Processor.process_fetchRecByItem
        self._processMap["fetchRecByUser"] = Processor.process_fetchRecByUser
        self._processMap["fetchRecByMult"] = Processor.process_fetchRecByMult

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_ping(self, seqid, iprot, oprot):
        args = ping_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ping_result()
        try:
            result.success = self._handler.ping()
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("ping", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_fetchRecByItem(self, seqid, iprot, oprot):
        args = fetchRecByItem_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = fetchRecByItem_result()
        try:
            result.success = self._handler.fetchRecByItem(args.req)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except SystemException as sys_exc:
            msg_type = TMessageType.REPLY
            result.sys_exc = sys_exc
        except CodeException as code_exc:
            msg_type = TMessageType.REPLY
            result.code_exc = code_exc
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("fetchRecByItem", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_fetchRecByUser(self, seqid, iprot, oprot):
        args = fetchRecByUser_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = fetchRecByUser_result()
        try:
            result.success = self._handler.fetchRecByUser(args.req)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except SystemException as sys_exc:
            msg_type = TMessageType.REPLY
            result.sys_exc = sys_exc
        except CodeException as code_exc:
            msg_type = TMessageType.REPLY
            result.code_exc = code_exc
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("fetchRecByUser", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_fetchRecByMult(self, seqid, iprot, oprot):
        args = fetchRecByMult_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = fetchRecByMult_result()
        try:
            result.success = self._handler.fetchRecByMult(args.req)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except SystemException as sys_exc:
            msg_type = TMessageType.REPLY
            result.sys_exc = sys_exc
        except CodeException as code_exc:
            msg_type = TMessageType.REPLY
            result.code_exc = code_exc
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("fetchRecByMult", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class ping_args(object):

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ping_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ping_result(object):
    """
    Attributes:
     - success
    """

    thrift_spec = (
        (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    )

    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ping_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class fetchRecByItem_args(object):
    """
    Attributes:
     - req
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'req', (ItemRequest, ItemRequest.thrift_spec), None, ),  # 1
    )

    def __init__(self, req=None,):
        self.req = req

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.req = ItemRequest()
                    self.req.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('fetchRecByItem_args')
        if self.req is not None:
            oprot.writeFieldBegin('req', TType.STRUCT, 1)
            self.req.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class fetchRecByItem_result(object):
    """
    Attributes:
     - success
     - sys_exc
     - code_exc
    """

    thrift_spec = (
        (0, TType.STRUCT, 'success', (RecResponse, RecResponse.thrift_spec), None, ),  # 0
        (1, TType.STRUCT, 'sys_exc', (SystemException, SystemException.thrift_spec), None, ),  # 1
        (2, TType.STRUCT, 'code_exc', (CodeException, CodeException.thrift_spec), None, ),  # 2
    )

    def __init__(self, success=None, sys_exc=None, code_exc=None,):
        self.success = success
        self.sys_exc = sys_exc
        self.code_exc = code_exc

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = RecResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.sys_exc = SystemException()
                    self.sys_exc.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.code_exc = CodeException()
                    self.code_exc.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('fetchRecByItem_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.sys_exc is not None:
            oprot.writeFieldBegin('sys_exc', TType.STRUCT, 1)
            self.sys_exc.write(oprot)
            oprot.writeFieldEnd()
        if self.code_exc is not None:
            oprot.writeFieldBegin('code_exc', TType.STRUCT, 2)
            self.code_exc.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class fetchRecByUser_args(object):
    """
    Attributes:
     - req
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'req', (UserRequest, UserRequest.thrift_spec), None, ),  # 1
    )

    def __init__(self, req=None,):
        self.req = req

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.req = UserRequest()
                    self.req.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('fetchRecByUser_args')
        if self.req is not None:
            oprot.writeFieldBegin('req', TType.STRUCT, 1)
            self.req.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class fetchRecByUser_result(object):
    """
    Attributes:
     - success
     - sys_exc
     - code_exc
    """

    thrift_spec = (
        (0, TType.STRUCT, 'success', (RecResponse, RecResponse.thrift_spec), None, ),  # 0
        (1, TType.STRUCT, 'sys_exc', (SystemException, SystemException.thrift_spec), None, ),  # 1
        (2, TType.STRUCT, 'code_exc', (CodeException, CodeException.thrift_spec), None, ),  # 2
    )

    def __init__(self, success=None, sys_exc=None, code_exc=None,):
        self.success = success
        self.sys_exc = sys_exc
        self.code_exc = code_exc

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = RecResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.sys_exc = SystemException()
                    self.sys_exc.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.code_exc = CodeException()
                    self.code_exc.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('fetchRecByUser_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.sys_exc is not None:
            oprot.writeFieldBegin('sys_exc', TType.STRUCT, 1)
            self.sys_exc.write(oprot)
            oprot.writeFieldEnd()
        if self.code_exc is not None:
            oprot.writeFieldBegin('code_exc', TType.STRUCT, 2)
            self.code_exc.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class fetchRecByMult_args(object):
    """
    Attributes:
     - req
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'req', (MultRequest, MultRequest.thrift_spec), None, ),  # 1
    )

    def __init__(self, req=None,):
        self.req = req

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.req = MultRequest()
                    self.req.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('fetchRecByMult_args')
        if self.req is not None:
            oprot.writeFieldBegin('req', TType.STRUCT, 1)
            self.req.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class fetchRecByMult_result(object):
    """
    Attributes:
     - success
     - sys_exc
     - code_exc
    """

    thrift_spec = (
        (0, TType.STRUCT, 'success', (RecResponse, RecResponse.thrift_spec), None, ),  # 0
        (1, TType.STRUCT, 'sys_exc', (SystemException, SystemException.thrift_spec), None, ),  # 1
        (2, TType.STRUCT, 'code_exc', (CodeException, CodeException.thrift_spec), None, ),  # 2
    )

    def __init__(self, success=None, sys_exc=None, code_exc=None,):
        self.success = success
        self.sys_exc = sys_exc
        self.code_exc = code_exc

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = RecResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.sys_exc = SystemException()
                    self.sys_exc.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.code_exc = CodeException()
                    self.code_exc.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('fetchRecByMult_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.sys_exc is not None:
            oprot.writeFieldBegin('sys_exc', TType.STRUCT, 1)
            self.sys_exc.write(oprot)
            oprot.writeFieldEnd()
        if self.code_exc is not None:
            oprot.writeFieldBegin('code_exc', TType.STRUCT, 2)
            self.code_exc.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
