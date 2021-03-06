# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import plugins_pb2 as plugins__pb2
import project_pb2 as project__pb2


class ProjectStub(object):
    """*
    Paddle's project API service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PrintMessage = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/PrintMessage',
                request_serializer=project__pb2.PrintRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ExecuteCommand = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/ExecuteCommand',
                request_serializer=project__pb2.ExecuteCommandRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetWorkingDirectory = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/GetWorkingDirectory',
                request_serializer=project__pb2.ProjectInfoRequest.SerializeToString,
                response_deserializer=project__pb2.WorkingDir.FromString,
                )
        self.GetDescription = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/GetDescription',
                request_serializer=project__pb2.ProjectInfoRequest.SerializeToString,
                response_deserializer=project__pb2.Description.FromString,
                )
        self.GetRoots = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/GetRoots',
                request_serializer=project__pb2.ProjectInfoRequest.SerializeToString,
                response_deserializer=project__pb2.Roots.FromString,
                )
        self.AddSources = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/AddSources',
                request_serializer=project__pb2.AddPathsRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.AddTests = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/AddTests',
                request_serializer=project__pb2.AddPathsRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.AddResources = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/AddResources',
                request_serializer=project__pb2.AddPathsRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetTasksNames = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/GetTasksNames',
                request_serializer=project__pb2.ProjectInfoRequest.SerializeToString,
                response_deserializer=project__pb2.Tasks.FromString,
                )
        self.RunTask = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/RunTask',
                request_serializer=plugins__pb2.ProcessTaskRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.AddCleanLocation = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/AddCleanLocation',
                request_serializer=project__pb2.AddPathsRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetConfigurationSpecification = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/GetConfigurationSpecification',
                request_serializer=project__pb2.ProjectInfoRequest.SerializeToString,
                response_deserializer=project__pb2.CompositeSpecNode.FromString,
                )
        self.UpdateConfigurationSpecification = channel.unary_unary(
                '/io.paddle.plugin.interop.Project/UpdateConfigurationSpecification',
                request_serializer=project__pb2.UpdateConfigSpecRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ProjectServicer(object):
    """*
    Paddle's project API service definition.
    """

    def PrintMessage(self, request, context):
        """*
        Prints message to the terminal associated with specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteCommand(self, request, context):
        """*
        Executes specified command with passed arguments.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWorkingDirectory(self, request, context):
        """*
        Returns working directory path for specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDescription(self, request, context):
        """*
        Returns description of specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoots(self, request, context):
        """*
        Returns triple consists of list of file paths to project source code,
        list of paths to project test files and list of paths to project resource files.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSources(self, request, context):
        """*
        Add paths to specified project's sources roots.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddTests(self, request, context):
        """*
        Add paths to specified project's tests roots.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddResources(self, request, context):
        """*
        Add paths to specified project's resources roots.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTasksNames(self, request, context):
        """*
        Returns list of tasks names associates with specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunTask(self, request, context):
        """*
        Run task by id associate with specfied project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddCleanLocation(self, request, context):
        """*
        Add specified paths to clean task's location list.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConfigurationSpecification(self, request, context):
        """*
        Returns configuration specification of specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateConfigurationSpecification(self, request, context):
        """*
        Updates configuration specification of specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PrintMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.PrintMessage,
                    request_deserializer=project__pb2.PrintRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ExecuteCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteCommand,
                    request_deserializer=project__pb2.ExecuteCommandRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetWorkingDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWorkingDirectory,
                    request_deserializer=project__pb2.ProjectInfoRequest.FromString,
                    response_serializer=project__pb2.WorkingDir.SerializeToString,
            ),
            'GetDescription': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDescription,
                    request_deserializer=project__pb2.ProjectInfoRequest.FromString,
                    response_serializer=project__pb2.Description.SerializeToString,
            ),
            'GetRoots': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoots,
                    request_deserializer=project__pb2.ProjectInfoRequest.FromString,
                    response_serializer=project__pb2.Roots.SerializeToString,
            ),
            'AddSources': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSources,
                    request_deserializer=project__pb2.AddPathsRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'AddTests': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTests,
                    request_deserializer=project__pb2.AddPathsRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'AddResources': grpc.unary_unary_rpc_method_handler(
                    servicer.AddResources,
                    request_deserializer=project__pb2.AddPathsRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetTasksNames': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTasksNames,
                    request_deserializer=project__pb2.ProjectInfoRequest.FromString,
                    response_serializer=project__pb2.Tasks.SerializeToString,
            ),
            'RunTask': grpc.unary_unary_rpc_method_handler(
                    servicer.RunTask,
                    request_deserializer=plugins__pb2.ProcessTaskRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'AddCleanLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCleanLocation,
                    request_deserializer=project__pb2.AddPathsRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetConfigurationSpecification': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfigurationSpecification,
                    request_deserializer=project__pb2.ProjectInfoRequest.FromString,
                    response_serializer=project__pb2.CompositeSpecNode.SerializeToString,
            ),
            'UpdateConfigurationSpecification': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateConfigurationSpecification,
                    request_deserializer=project__pb2.UpdateConfigSpecRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'io.paddle.plugin.interop.Project', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Project(object):
    """*
    Paddle's project API service definition.
    """

    @staticmethod
    def PrintMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/PrintMessage',
            project__pb2.PrintRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExecuteCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/ExecuteCommand',
            project__pb2.ExecuteCommandRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWorkingDirectory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/GetWorkingDirectory',
            project__pb2.ProjectInfoRequest.SerializeToString,
            project__pb2.WorkingDir.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDescription(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/GetDescription',
            project__pb2.ProjectInfoRequest.SerializeToString,
            project__pb2.Description.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRoots(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/GetRoots',
            project__pb2.ProjectInfoRequest.SerializeToString,
            project__pb2.Roots.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/AddSources',
            project__pb2.AddPathsRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddTests(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/AddTests',
            project__pb2.AddPathsRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/AddResources',
            project__pb2.AddPathsRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTasksNames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/GetTasksNames',
            project__pb2.ProjectInfoRequest.SerializeToString,
            project__pb2.Tasks.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RunTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/RunTask',
            plugins__pb2.ProcessTaskRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddCleanLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/AddCleanLocation',
            project__pb2.AddPathsRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConfigurationSpecification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/GetConfigurationSpecification',
            project__pb2.ProjectInfoRequest.SerializeToString,
            project__pb2.CompositeSpecNode.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateConfigurationSpecification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.paddle.plugin.interop.Project/UpdateConfigurationSpecification',
            project__pb2.UpdateConfigSpecRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
