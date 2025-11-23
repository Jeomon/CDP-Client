
"""CDP Emulation Methods"""

from cdp_client.methods import CDPMethods
from typing import TypedDict,Optional
from emulation.methods.types import *

class EmulationMethods:
    def __init__(self, methods:CDPMethods):
        self.methods = methods

    async def clear_device_metrics_override(self, params: None=None) -> Dict[str, Any]:
        """Clears the overridden device metrics."""
        return await self.methods.send(method="Emulation.clearDeviceMetricsOverride", params=params)

    async def clear_geolocation_override(self, params: None=None) -> Dict[str, Any]:
        """Clears the overridden Geolocation Position and Error."""
        return await self.methods.send(method="Emulation.clearGeolocationOverride", params=params)

    async def reset_page_scale_factor(self, params: None=None) -> Dict[str, Any]:
        """Requests that page scale factor is reset to initial values."""
        return await self.methods.send(method="Emulation.resetPageScaleFactor", params=params)

    async def set_focus_emulation_enabled(self, params: Optional[setFocusEmulationEnabledParameters]=None) -> Dict[str, Any]:
        """Enables or disables simulating a focused and active page."""
        return await self.methods.send(method="Emulation.setFocusEmulationEnabled", params=params)

    async def set_auto_dark_mode_override(self, params: Optional[setAutoDarkModeOverrideParameters]=None) -> Dict[str, Any]:
        """Automatically render all web contents using a dark theme."""
        return await self.methods.send(method="Emulation.setAutoDarkModeOverride", params=params)

    async def set_cpu_throttling_rate(self, params: Optional[setCPUThrottlingRateParameters]=None) -> Dict[str, Any]:
        """Enables CPU throttling to emulate slow CPUs."""
        return await self.methods.send(method="Emulation.setCPUThrottlingRate", params=params)

    async def set_default_background_color_override(self, params: Optional[setDefaultBackgroundColorOverrideParameters]=None) -> Dict[str, Any]:
        """Sets or clears an override of the default background color of the frame. This override is used if the content does not specify one."""
        return await self.methods.send(method="Emulation.setDefaultBackgroundColorOverride", params=params)

    async def set_safe_area_insets_override(self, params: Optional[setSafeAreaInsetsOverrideParameters]=None) -> Dict[str, Any]:
        """Overrides the values for env(safe-area-inset-*) and env(safe-area-max-inset-*). Unset values will cause the respective variables to be undefined, even if previously overridden."""
        return await self.methods.send(method="Emulation.setSafeAreaInsetsOverride", params=params)

    async def set_device_metrics_override(self, params: Optional[setDeviceMetricsOverrideParameters]=None) -> Dict[str, Any]:
        """Overrides the values of device screen dimensions (window.screen.width, window.screen.height, window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media query results)."""
        return await self.methods.send(method="Emulation.setDeviceMetricsOverride", params=params)

    async def set_device_posture_override(self, params: Optional[setDevicePostureOverrideParameters]=None) -> Dict[str, Any]:
        """Start reporting the given posture value to the Device Posture API. This override can also be set in setDeviceMetricsOverride()."""
        return await self.methods.send(method="Emulation.setDevicePostureOverride", params=params)

    async def clear_device_posture_override(self, params: None=None) -> Dict[str, Any]:
        """Clears a device posture override set with either setDeviceMetricsOverride() or setDevicePostureOverride() and starts using posture information from the platform again. Does nothing if no override is set."""
        return await self.methods.send(method="Emulation.clearDevicePostureOverride", params=params)

    async def set_display_features_override(self, params: Optional[setDisplayFeaturesOverrideParameters]=None) -> Dict[str, Any]:
        """Start using the given display features to pupulate the Viewport Segments API. This override can also be set in setDeviceMetricsOverride()."""
        return await self.methods.send(method="Emulation.setDisplayFeaturesOverride", params=params)

    async def clear_display_features_override(self, params: None=None) -> Dict[str, Any]:
        """Clears the display features override set with either setDeviceMetricsOverride() or setDisplayFeaturesOverride() and starts using display features from the platform again. Does nothing if no override is set."""
        return await self.methods.send(method="Emulation.clearDisplayFeaturesOverride", params=params)

    async def set_scrollbars_hidden(self, params: Optional[setScrollbarsHiddenParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="Emulation.setScrollbarsHidden", params=params)

    async def set_document_cookie_disabled(self, params: Optional[setDocumentCookieDisabledParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="Emulation.setDocumentCookieDisabled", params=params)

    async def set_emit_touch_events_for_mouse(self, params: Optional[setEmitTouchEventsForMouseParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="Emulation.setEmitTouchEventsForMouse", params=params)

    async def set_emulated_media(self, params: Optional[setEmulatedMediaParameters]=None) -> Dict[str, Any]:
        """Emulates the given media type or media feature for CSS media queries."""
        return await self.methods.send(method="Emulation.setEmulatedMedia", params=params)

    async def set_emulated_vision_deficiency(self, params: Optional[setEmulatedVisionDeficiencyParameters]=None) -> Dict[str, Any]:
        """Emulates the given vision deficiency."""
        return await self.methods.send(method="Emulation.setEmulatedVisionDeficiency", params=params)

    async def set_emulated_os_text_scale(self, params: Optional[setEmulatedOSTextScaleParameters]=None) -> Dict[str, Any]:
        """Emulates the given OS text scale."""
        return await self.methods.send(method="Emulation.setEmulatedOSTextScale", params=params)

    async def set_geolocation_override(self, params: Optional[setGeolocationOverrideParameters]=None) -> Dict[str, Any]:
        """Overrides the Geolocation Position or Error. Omitting latitude, longitude or accuracy emulates position unavailable."""
        return await self.methods.send(method="Emulation.setGeolocationOverride", params=params)

    async def get_overridden_sensor_information(self, params: Optional[getOverriddenSensorInformationParameters]=None) -> getOverriddenSensorInformationReturns:
        return await self.methods.send(method="Emulation.getOverriddenSensorInformation", params=params)

    async def set_sensor_override_enabled(self, params: Optional[setSensorOverrideEnabledParameters]=None) -> Dict[str, Any]:
        """Overrides a platform sensor of a given type. If |enabled| is true, calls to Sensor.start() will use a virtual sensor as backend rather than fetching data from a real hardware sensor. Otherwise, existing virtual sensor-backend Sensor objects will fire an error event and new calls to Sensor.start() will attempt to use a real sensor instead."""
        return await self.methods.send(method="Emulation.setSensorOverrideEnabled", params=params)

    async def set_sensor_override_readings(self, params: Optional[setSensorOverrideReadingsParameters]=None) -> Dict[str, Any]:
        """Updates the sensor readings reported by a sensor type previously overridden by setSensorOverrideEnabled."""
        return await self.methods.send(method="Emulation.setSensorOverrideReadings", params=params)

    async def set_pressure_source_override_enabled(self, params: Optional[setPressureSourceOverrideEnabledParameters]=None) -> Dict[str, Any]:
        """Overrides a pressure source of a given type, as used by the Compute Pressure API, so that updates to PressureObserver.observe() are provided via setPressureStateOverride instead of being retrieved from platform-provided telemetry data."""
        return await self.methods.send(method="Emulation.setPressureSourceOverrideEnabled", params=params)

    async def set_pressure_state_override(self, params: Optional[setPressureStateOverrideParameters]=None) -> Dict[str, Any]:
        """TODO: OBSOLETE: To remove when setPressureDataOverride is merged. Provides a given pressure state that will be processed and eventually be delivered to PressureObserver users. |source| must have been previously overridden by setPressureSourceOverrideEnabled."""
        return await self.methods.send(method="Emulation.setPressureStateOverride", params=params)

    async def set_pressure_data_override(self, params: Optional[setPressureDataOverrideParameters]=None) -> Dict[str, Any]:
        """Provides a given pressure data set that will be processed and eventually be delivered to PressureObserver users. |source| must have been previously overridden by setPressureSourceOverrideEnabled."""
        return await self.methods.send(method="Emulation.setPressureDataOverride", params=params)

    async def set_idle_override(self, params: Optional[setIdleOverrideParameters]=None) -> Dict[str, Any]:
        """Overrides the Idle state."""
        return await self.methods.send(method="Emulation.setIdleOverride", params=params)

    async def clear_idle_override(self, params: None=None) -> Dict[str, Any]:
        """Clears Idle state overrides."""
        return await self.methods.send(method="Emulation.clearIdleOverride", params=params)

    async def set_page_scale_factor(self, params: Optional[setPageScaleFactorParameters]=None) -> Dict[str, Any]:
        """Sets a specified page scale factor."""
        return await self.methods.send(method="Emulation.setPageScaleFactor", params=params)

    async def set_script_execution_disabled(self, params: Optional[setScriptExecutionDisabledParameters]=None) -> Dict[str, Any]:
        """Switches script execution in the page."""
        return await self.methods.send(method="Emulation.setScriptExecutionDisabled", params=params)

    async def set_touch_emulation_enabled(self, params: Optional[setTouchEmulationEnabledParameters]=None) -> Dict[str, Any]:
        """Enables touch on platforms which do not support them."""
        return await self.methods.send(method="Emulation.setTouchEmulationEnabled", params=params)

    async def set_virtual_time_policy(self, params: Optional[setVirtualTimePolicyParameters]=None) -> setVirtualTimePolicyReturns:
        """Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets the current virtual time policy.  Note this supersedes any previous time budget."""
        return await self.methods.send(method="Emulation.setVirtualTimePolicy", params=params)

    async def set_locale_override(self, params: Optional[setLocaleOverrideParameters]=None) -> Dict[str, Any]:
        """Overrides default host system locale with the specified one."""
        return await self.methods.send(method="Emulation.setLocaleOverride", params=params)

    async def set_timezone_override(self, params: Optional[setTimezoneOverrideParameters]=None) -> Dict[str, Any]:
        """Overrides default host system timezone with the specified one."""
        return await self.methods.send(method="Emulation.setTimezoneOverride", params=params)

    async def set_disabled_image_types(self, params: Optional[setDisabledImageTypesParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="Emulation.setDisabledImageTypes", params=params)

    async def set_data_saver_override(self, params: Optional[setDataSaverOverrideParameters]=None) -> Dict[str, Any]:
        """Override the value of navigator.connection.saveData"""
        return await self.methods.send(method="Emulation.setDataSaverOverride", params=params)

    async def set_hardware_concurrency_override(self, params: Optional[setHardwareConcurrencyOverrideParameters]=None) -> Dict[str, Any]:
        return await self.methods.send(method="Emulation.setHardwareConcurrencyOverride", params=params)

    async def set_user_agent_override(self, params: Optional[setUserAgentOverrideParameters]=None) -> Dict[str, Any]:
        """Allows overriding user agent with the given string. `userAgentMetadata` must be set for Client Hint headers to be sent."""
        return await self.methods.send(method="Emulation.setUserAgentOverride", params=params)

    async def set_automation_override(self, params: Optional[setAutomationOverrideParameters]=None) -> Dict[str, Any]:
        """Allows overriding the automation flag."""
        return await self.methods.send(method="Emulation.setAutomationOverride", params=params)

    async def set_small_viewport_height_difference_override(self, params: Optional[setSmallViewportHeightDifferenceOverrideParameters]=None) -> Dict[str, Any]:
        """Allows overriding the difference between the small and large viewport sizes, which determine the value of the `svh` and `lvh` unit, respectively. Only supported for top-level frames."""
        return await self.methods.send(method="Emulation.setSmallViewportHeightDifferenceOverride", params=params)

    async def get_screen_infos(self, params: None=None) -> getScreenInfosReturns:
        """Returns device's screen configuration."""
        return await self.methods.send(method="Emulation.getScreenInfos", params=params)

    async def add_screen(self, params: Optional[addScreenParameters]=None) -> addScreenReturns:
        """Add a new screen to the device. Only supported in headless mode."""
        return await self.methods.send(method="Emulation.addScreen", params=params)

    async def remove_screen(self, params: Optional[removeScreenParameters]=None) -> Dict[str, Any]:
        """Remove screen from the device. Only supported in headless mode."""
        return await self.methods.send(method="Emulation.removeScreen", params=params)
