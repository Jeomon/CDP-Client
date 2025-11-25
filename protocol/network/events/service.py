
"""CDP Network Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.network.events.types import *

class NetworkEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_data_received(self, callback: Callable[[dataReceivedEvent,Optional[str]], None]=None) -> None:
        """Fired when data chunk was received over the network."""
        self.events.on('dataReceived', callback)
    
    def on_event_source_message_received(self, callback: Callable[[eventSourceMessageReceivedEvent,Optional[str]], None]=None) -> None:
        """Fired when EventSource message is received."""
        self.events.on('eventSourceMessageReceived', callback)
    
    def on_loading_failed(self, callback: Callable[[loadingFailedEvent,Optional[str]], None]=None) -> None:
        """Fired when HTTP request has failed to load."""
        self.events.on('loadingFailed', callback)
    
    def on_loading_finished(self, callback: Callable[[loadingFinishedEvent,Optional[str]], None]=None) -> None:
        """Fired when HTTP request has finished loading."""
        self.events.on('loadingFinished', callback)
    
    def on_request_intercepted(self, callback: Callable[[requestInterceptedEvent,Optional[str]], None]=None) -> None:
        """Details of an intercepted HTTP request, which must be either allowed, blocked, modified or mocked. Deprecated, use Fetch.requestPaused instead."""
        self.events.on('requestIntercepted', callback)
    
    def on_request_served_from_cache(self, callback: Callable[[requestServedFromCacheEvent,Optional[str]], None]=None) -> None:
        """Fired if request ended up loading from cache."""
        self.events.on('requestServedFromCache', callback)
    
    def on_request_will_be_sent(self, callback: Callable[[requestWillBeSentEvent,Optional[str]], None]=None) -> None:
        """Fired when page is about to send HTTP request."""
        self.events.on('requestWillBeSent', callback)
    
    def on_resource_changed_priority(self, callback: Callable[[resourceChangedPriorityEvent,Optional[str]], None]=None) -> None:
        """Fired when resource loading priority is changed"""
        self.events.on('resourceChangedPriority', callback)
    
    def on_signed_exchange_received(self, callback: Callable[[signedExchangeReceivedEvent,Optional[str]], None]=None) -> None:
        """Fired when a signed exchange was received over the network"""
        self.events.on('signedExchangeReceived', callback)
    
    def on_response_received(self, callback: Callable[[responseReceivedEvent,Optional[str]], None]=None) -> None:
        """Fired when HTTP response is available."""
        self.events.on('responseReceived', callback)
    
    def on_web_socket_closed(self, callback: Callable[[webSocketClosedEvent,Optional[str]], None]=None) -> None:
        """Fired when WebSocket is closed."""
        self.events.on('webSocketClosed', callback)
    
    def on_web_socket_created(self, callback: Callable[[webSocketCreatedEvent,Optional[str]], None]=None) -> None:
        """Fired upon WebSocket creation."""
        self.events.on('webSocketCreated', callback)
    
    def on_web_socket_frame_error(self, callback: Callable[[webSocketFrameErrorEvent,Optional[str]], None]=None) -> None:
        """Fired when WebSocket message error occurs."""
        self.events.on('webSocketFrameError', callback)
    
    def on_web_socket_frame_received(self, callback: Callable[[webSocketFrameReceivedEvent,Optional[str]], None]=None) -> None:
        """Fired when WebSocket message is received."""
        self.events.on('webSocketFrameReceived', callback)
    
    def on_web_socket_frame_sent(self, callback: Callable[[webSocketFrameSentEvent,Optional[str]], None]=None) -> None:
        """Fired when WebSocket message is sent."""
        self.events.on('webSocketFrameSent', callback)
    
    def on_web_socket_handshake_response_received(self, callback: Callable[[webSocketHandshakeResponseReceivedEvent,Optional[str]], None]=None) -> None:
        """Fired when WebSocket handshake response becomes available."""
        self.events.on('webSocketHandshakeResponseReceived', callback)
    
    def on_web_socket_will_send_handshake_request(self, callback: Callable[[webSocketWillSendHandshakeRequestEvent,Optional[str]], None]=None) -> None:
        """Fired when WebSocket is about to initiate handshake."""
        self.events.on('webSocketWillSendHandshakeRequest', callback)
    
    def on_web_transport_created(self, callback: Callable[[webTransportCreatedEvent,Optional[str]], None]=None) -> None:
        """Fired upon WebTransport creation."""
        self.events.on('webTransportCreated', callback)
    
    def on_web_transport_connection_established(self, callback: Callable[[webTransportConnectionEstablishedEvent,Optional[str]], None]=None) -> None:
        """Fired when WebTransport handshake is finished."""
        self.events.on('webTransportConnectionEstablished', callback)
    
    def on_web_transport_closed(self, callback: Callable[[webTransportClosedEvent,Optional[str]], None]=None) -> None:
        """Fired when WebTransport is disposed."""
        self.events.on('webTransportClosed', callback)
    
    def on_direct_tcp_socket_created(self, callback: Callable[[directTCPSocketCreatedEvent,Optional[str]], None]=None) -> None:
        """Fired upon direct_socket.TCPSocket creation."""
        self.events.on('directTCPSocketCreated', callback)
    
    def on_direct_tcp_socket_opened(self, callback: Callable[[directTCPSocketOpenedEvent,Optional[str]], None]=None) -> None:
        """Fired when direct_socket.TCPSocket connection is opened."""
        self.events.on('directTCPSocketOpened', callback)
    
    def on_direct_tcp_socket_aborted(self, callback: Callable[[directTCPSocketAbortedEvent,Optional[str]], None]=None) -> None:
        """Fired when direct_socket.TCPSocket is aborted."""
        self.events.on('directTCPSocketAborted', callback)
    
    def on_direct_tcp_socket_closed(self, callback: Callable[[directTCPSocketClosedEvent,Optional[str]], None]=None) -> None:
        """Fired when direct_socket.TCPSocket is closed."""
        self.events.on('directTCPSocketClosed', callback)
    
    def on_direct_tcp_socket_chunk_sent(self, callback: Callable[[directTCPSocketChunkSentEvent,Optional[str]], None]=None) -> None:
        """Fired when data is sent to tcp direct socket stream."""
        self.events.on('directTCPSocketChunkSent', callback)
    
    def on_direct_tcp_socket_chunk_received(self, callback: Callable[[directTCPSocketChunkReceivedEvent,Optional[str]], None]=None) -> None:
        """Fired when data is received from tcp direct socket stream."""
        self.events.on('directTCPSocketChunkReceived', callback)
    
    def on_direct_udp_socket_joined_multicast_group(self, callback: Callable[[directUDPSocketJoinedMulticastGroupEvent,Optional[str]], None]=None) -> None:
        self.events.on('directUDPSocketJoinedMulticastGroup', callback)
    
    def on_direct_udp_socket_left_multicast_group(self, callback: Callable[[directUDPSocketLeftMulticastGroupEvent,Optional[str]], None]=None) -> None:
        self.events.on('directUDPSocketLeftMulticastGroup', callback)
    
    def on_direct_udp_socket_created(self, callback: Callable[[directUDPSocketCreatedEvent,Optional[str]], None]=None) -> None:
        """Fired upon direct_socket.UDPSocket creation."""
        self.events.on('directUDPSocketCreated', callback)
    
    def on_direct_udp_socket_opened(self, callback: Callable[[directUDPSocketOpenedEvent,Optional[str]], None]=None) -> None:
        """Fired when direct_socket.UDPSocket connection is opened."""
        self.events.on('directUDPSocketOpened', callback)
    
    def on_direct_udp_socket_aborted(self, callback: Callable[[directUDPSocketAbortedEvent,Optional[str]], None]=None) -> None:
        """Fired when direct_socket.UDPSocket is aborted."""
        self.events.on('directUDPSocketAborted', callback)
    
    def on_direct_udp_socket_closed(self, callback: Callable[[directUDPSocketClosedEvent,Optional[str]], None]=None) -> None:
        """Fired when direct_socket.UDPSocket is closed."""
        self.events.on('directUDPSocketClosed', callback)
    
    def on_direct_udp_socket_chunk_sent(self, callback: Callable[[directUDPSocketChunkSentEvent,Optional[str]], None]=None) -> None:
        """Fired when message is sent to udp direct socket stream."""
        self.events.on('directUDPSocketChunkSent', callback)
    
    def on_direct_udp_socket_chunk_received(self, callback: Callable[[directUDPSocketChunkReceivedEvent,Optional[str]], None]=None) -> None:
        """Fired when message is received from udp direct socket stream."""
        self.events.on('directUDPSocketChunkReceived', callback)
    
    def on_request_will_be_sent_extra_info(self, callback: Callable[[requestWillBeSentExtraInfoEvent,Optional[str]], None]=None) -> None:
        """Fired when additional information about a requestWillBeSent event is available from the network stack. Not every requestWillBeSent event will have an additional requestWillBeSentExtraInfo fired for it, and there is no guarantee whether requestWillBeSent or requestWillBeSentExtraInfo will be fired first for the same request."""
        self.events.on('requestWillBeSentExtraInfo', callback)
    
    def on_response_received_extra_info(self, callback: Callable[[responseReceivedExtraInfoEvent,Optional[str]], None]=None) -> None:
        """Fired when additional information about a responseReceived event is available from the network stack. Not every responseReceived event will have an additional responseReceivedExtraInfo for it, and responseReceivedExtraInfo may be fired before or after responseReceived."""
        self.events.on('responseReceivedExtraInfo', callback)
    
    def on_response_received_early_hints(self, callback: Callable[[responseReceivedEarlyHintsEvent,Optional[str]], None]=None) -> None:
        """Fired when 103 Early Hints headers is received in addition to the common response. Not every responseReceived event will have an responseReceivedEarlyHints fired. Only one responseReceivedEarlyHints may be fired for eached responseReceived event."""
        self.events.on('responseReceivedEarlyHints', callback)
    
    def on_trust_token_operation_done(self, callback: Callable[[trustTokenOperationDoneEvent,Optional[str]], None]=None) -> None:
        """Fired exactly once for each Trust Token operation. Depending on the type of the operation and whether the operation succeeded or failed, the event is fired before the corresponding request was sent or after the response was received."""
        self.events.on('trustTokenOperationDone', callback)
    
    def on_policy_updated(self, callback: Callable[[policyUpdatedEvent,Optional[str]], None]=None) -> None:
        """Fired once security policy has been updated."""
        self.events.on('policyUpdated', callback)
    
    def on_reporting_api_report_added(self, callback: Callable[[reportingApiReportAddedEvent,Optional[str]], None]=None) -> None:
        """Is sent whenever a new report is added. And after 'enableReportingApi' for all existing reports."""
        self.events.on('reportingApiReportAdded', callback)
    
    def on_reporting_api_report_updated(self, callback: Callable[[reportingApiReportUpdatedEvent,Optional[str]], None]=None) -> None:
        self.events.on('reportingApiReportUpdated', callback)
    
    def on_reporting_api_endpoints_changed_for_origin(self, callback: Callable[[reportingApiEndpointsChangedForOriginEvent,Optional[str]], None]=None) -> None:
        self.events.on('reportingApiEndpointsChangedForOrigin', callback)
     