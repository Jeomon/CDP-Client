
"""CDP BluetoothEmulation Events"""

from client.events import CDPEvents
from typing import TypedDict, Optional, Callable
from protocol.bluetooth_emulation.events.types import *

class BluetoothEmulationEvents:
    def __init__(self,events:CDPEvents):
        self.events=events
    
    def on_gatt_operation_received(self, callback: Callable[gattOperationReceivedEvent, None]=None) -> None:
        """Event for when a GATT operation of |type| to the peripheral with |address| happened."""
        self.events.on('gattOperationReceived', callback)
    
    def on_characteristic_operation_received(self, callback: Callable[characteristicOperationReceivedEvent, None]=None) -> None:
        """Event for when a characteristic operation of |type| to the characteristic respresented by |characteristicId| happened. |data| and |writeType| is expected to exist when |type| is write."""
        self.events.on('characteristicOperationReceived', callback)
    
    def on_descriptor_operation_received(self, callback: Callable[descriptorOperationReceivedEvent, None]=None) -> None:
        """Event for when a descriptor operation of |type| to the descriptor respresented by |descriptorId| happened. |data| is expected to exist when |type| is write."""
        self.events.on('descriptorOperationReceived', callback)
     