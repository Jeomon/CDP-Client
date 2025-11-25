
"""CDP BluetoothEmulation Methods"""

from client.methods import CDPMethods
from typing import TypedDict,Optional
from protocol.bluetooth_emulation.methods.types import *

class BluetoothEmulationMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def enable(self, params: Optional[enableParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Enable the BluetoothEmulation domain."""
        return await self.methods.send(method="BluetoothEmulation.enable", params=params,session_id=session_id)

    async def set_simulated_central_state(self, params: Optional[setSimulatedCentralStateParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Set the state of the simulated central."""
        return await self.methods.send(method="BluetoothEmulation.setSimulatedCentralState", params=params,session_id=session_id)

    async def disable(self, params: None=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Disable the BluetoothEmulation domain."""
        return await self.methods.send(method="BluetoothEmulation.disable", params=params,session_id=session_id)

    async def simulate_preconnected_peripheral(self, params: Optional[simulatePreconnectedPeripheralParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Simulates a peripheral with |address|, |name| and |knownServiceUuids| that has already been connected to the system."""
        return await self.methods.send(method="BluetoothEmulation.simulatePreconnectedPeripheral", params=params,session_id=session_id)

    async def simulate_advertisement(self, params: Optional[simulateAdvertisementParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Simulates an advertisement packet described in |entry| being received by the central."""
        return await self.methods.send(method="BluetoothEmulation.simulateAdvertisement", params=params,session_id=session_id)

    async def simulate_gatt_operation_response(self, params: Optional[simulateGATTOperationResponseParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Simulates the response code from the peripheral with |address| for a GATT operation of |type|. The |code| value follows the HCI Error Codes from Bluetooth Core Specification Vol 2 Part D 1.3 List Of Error Codes."""
        return await self.methods.send(method="BluetoothEmulation.simulateGATTOperationResponse", params=params,session_id=session_id)

    async def simulate_characteristic_operation_response(self, params: Optional[simulateCharacteristicOperationResponseParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Simulates the response from the characteristic with |characteristicId| for a characteristic operation of |type|. The |code| value follows the Error Codes from Bluetooth Core Specification Vol 3 Part F 3.4.1.1 Error Response. The |data| is expected to exist when simulating a successful read operation response."""
        return await self.methods.send(method="BluetoothEmulation.simulateCharacteristicOperationResponse", params=params,session_id=session_id)

    async def simulate_descriptor_operation_response(self, params: Optional[simulateDescriptorOperationResponseParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Simulates the response from the descriptor with |descriptorId| for a descriptor operation of |type|. The |code| value follows the Error Codes from Bluetooth Core Specification Vol 3 Part F 3.4.1.1 Error Response. The |data| is expected to exist when simulating a successful read operation response."""
        return await self.methods.send(method="BluetoothEmulation.simulateDescriptorOperationResponse", params=params,session_id=session_id)

    async def add_service(self, params: Optional[addServiceParameters]=None,session_id: Optional[str] = None) -> addServiceReturns:
        """Adds a service with |serviceUuid| to the peripheral with |address|."""
        return await self.methods.send(method="BluetoothEmulation.addService", params=params,session_id=session_id)

    async def remove_service(self, params: Optional[removeServiceParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Removes the service respresented by |serviceId| from the simulated central."""
        return await self.methods.send(method="BluetoothEmulation.removeService", params=params,session_id=session_id)

    async def add_characteristic(self, params: Optional[addCharacteristicParameters]=None,session_id: Optional[str] = None) -> addCharacteristicReturns:
        """Adds a characteristic with |characteristicUuid| and |properties| to the service represented by |serviceId|."""
        return await self.methods.send(method="BluetoothEmulation.addCharacteristic", params=params,session_id=session_id)

    async def remove_characteristic(self, params: Optional[removeCharacteristicParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Removes the characteristic respresented by |characteristicId| from the simulated central."""
        return await self.methods.send(method="BluetoothEmulation.removeCharacteristic", params=params,session_id=session_id)

    async def add_descriptor(self, params: Optional[addDescriptorParameters]=None,session_id: Optional[str] = None) -> addDescriptorReturns:
        """Adds a descriptor with |descriptorUuid| to the characteristic respresented by |characteristicId|."""
        return await self.methods.send(method="BluetoothEmulation.addDescriptor", params=params,session_id=session_id)

    async def remove_descriptor(self, params: Optional[removeDescriptorParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Removes the descriptor with |descriptorId| from the simulated central."""
        return await self.methods.send(method="BluetoothEmulation.removeDescriptor", params=params,session_id=session_id)

    async def simulate_gatt_disconnection(self, params: Optional[simulateGATTDisconnectionParameters]=None,session_id: Optional[str] = None) -> Dict[str, Any]:
        """Simulates a GATT disconnection from the peripheral with |address|."""
        return await self.methods.send(method="BluetoothEmulation.simulateGATTDisconnection", params=params,session_id=session_id)
