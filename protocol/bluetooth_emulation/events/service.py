
"""CDP BluetoothEmulation Events"""

from client.service import CDPClient
from typing import TypedDict, Optional, Callable
from protocol.bluetooth_emulation.events.types import *

class BluetoothEmulationEvents:
    def __init__(self,client:CDPClient):
        self.client=client
    
    def on_gatt_operation_received(self, callback: Callable[[gattOperationReceivedEvent,Optional[str]], None]=None) -> None:
        """Event for when a GATT operation of |type| to the peripheral with |address| happened."""
        self.client.on('gattOperationReceived', callback)
    
    def on_characteristic_operation_received(self, callback: Callable[[characteristicOperationReceivedEvent,Optional[str]], None]=None) -> None:
        """Event for when a characteristic operation of |type| to the characteristic respresented by |characteristicId| happened. |data| and |writeType| is expected to exist when |type| is write."""
        self.client.on('characteristicOperationReceived', callback)
    
    def on_descriptor_operation_received(self, callback: Callable[[descriptorOperationReceivedEvent,Optional[str]], None]=None) -> None:
        """Event for when a descriptor operation of |type| to the descriptor respresented by |descriptorId| happened. |data| is expected to exist when |type| is write."""
        self.client.on('descriptorOperationReceived', callback)
     