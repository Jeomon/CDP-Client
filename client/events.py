
"""CDP Events"""
from typing import TYPE_CHECKING, Callable, Any

if TYPE_CHECKING:
    from .service import CDPClient

class CDPEvents:
    def __init__(self, client: "CDPClient"):
        self.client = client

    @property
    def accessibility(self):
        from protocol.accessibility.events.service import AccessibilityEvents
        return AccessibilityEvents(client=self.client)

    @property
    def animation(self):
        from protocol.animation.events.service import AnimationEvents
        return AnimationEvents(client=self.client)

    @property
    def audits(self):
        from protocol.audits.events.service import AuditsEvents
        return AuditsEvents(client=self.client)

    @property
    def autofill(self):
        from protocol.autofill.events.service import AutofillEvents
        return AutofillEvents(client=self.client)

    @property
    def background_service(self):
        from protocol.background_service.events.service import BackgroundServiceEvents
        return BackgroundServiceEvents(client=self.client)

    @property
    def bluetooth_emulation(self):
        from protocol.bluetooth_emulation.events.service import BluetoothEmulationEvents
        return BluetoothEmulationEvents(client=self.client)

    @property
    def browser(self):
        from protocol.browser.events.service import BrowserEvents
        return BrowserEvents(client=self.client)

    @property
    def css(self):
        from protocol.css.events.service import CSSEvents
        return CSSEvents(client=self.client)

    @property
    def cache_storage(self):
        from protocol.cache_storage.events.service import CacheStorageEvents
        return CacheStorageEvents(client=self.client)

    @property
    def cast(self):
        from protocol.cast.events.service import CastEvents
        return CastEvents(client=self.client)

    @property
    def dom(self):
        from protocol.dom.events.service import DOMEvents
        return DOMEvents(client=self.client)

    @property
    def dom_debugger(self):
        from protocol.dom_debugger.events.service import DOMDebuggerEvents
        return DOMDebuggerEvents(client=self.client)

    @property
    def dom_snapshot(self):
        from protocol.dom_snapshot.events.service import DOMSnapshotEvents
        return DOMSnapshotEvents(client=self.client)

    @property
    def dom_storage(self):
        from protocol.dom_storage.events.service import DOMStorageEvents
        return DOMStorageEvents(client=self.client)

    @property
    def device_access(self):
        from protocol.device_access.events.service import DeviceAccessEvents
        return DeviceAccessEvents(client=self.client)

    @property
    def device_orientation(self):
        from protocol.device_orientation.events.service import DeviceOrientationEvents
        return DeviceOrientationEvents(client=self.client)

    @property
    def emulation(self):
        from protocol.emulation.events.service import EmulationEvents
        return EmulationEvents(client=self.client)

    @property
    def event_breakpoints(self):
        from protocol.event_breakpoints.events.service import EventBreakpointsEvents
        return EventBreakpointsEvents(client=self.client)

    @property
    def extensions(self):
        from protocol.extensions.events.service import ExtensionsEvents
        return ExtensionsEvents(client=self.client)

    @property
    def fed_cm(self):
        from protocol.fed_cm.events.service import FedCmEvents
        return FedCmEvents(client=self.client)

    @property
    def fetch(self):
        from protocol.fetch.events.service import FetchEvents
        return FetchEvents(client=self.client)

    @property
    def file_system(self):
        from protocol.file_system.events.service import FileSystemEvents
        return FileSystemEvents(client=self.client)

    @property
    def headless_experimental(self):
        from protocol.headless_experimental.events.service import HeadlessExperimentalEvents
        return HeadlessExperimentalEvents(client=self.client)

    @property
    def io(self):
        from protocol.io.events.service import IOEvents
        return IOEvents(client=self.client)

    @property
    def indexed_db(self):
        from protocol.indexed_db.events.service import IndexedDBEvents
        return IndexedDBEvents(client=self.client)

    @property
    def input(self):
        from protocol.input.events.service import InputEvents
        return InputEvents(client=self.client)

    @property
    def inspector(self):
        from protocol.inspector.events.service import InspectorEvents
        return InspectorEvents(client=self.client)

    @property
    def layer_tree(self):
        from protocol.layer_tree.events.service import LayerTreeEvents
        return LayerTreeEvents(client=self.client)

    @property
    def log(self):
        from protocol.log.events.service import LogEvents
        return LogEvents(client=self.client)

    @property
    def media(self):
        from protocol.media.events.service import MediaEvents
        return MediaEvents(client=self.client)

    @property
    def memory(self):
        from protocol.memory.events.service import MemoryEvents
        return MemoryEvents(client=self.client)

    @property
    def network(self):
        from protocol.network.events.service import NetworkEvents
        return NetworkEvents(client=self.client)

    @property
    def overlay(self):
        from protocol.overlay.events.service import OverlayEvents
        return OverlayEvents(client=self.client)

    @property
    def pwa(self):
        from protocol.pwa.events.service import PWAEvents
        return PWAEvents(client=self.client)

    @property
    def page(self):
        from protocol.page.events.service import PageEvents
        return PageEvents(client=self.client)

    @property
    def performance(self):
        from protocol.performance.events.service import PerformanceEvents
        return PerformanceEvents(client=self.client)

    @property
    def performance_timeline(self):
        from protocol.performance_timeline.events.service import PerformanceTimelineEvents
        return PerformanceTimelineEvents(client=self.client)

    @property
    def preload(self):
        from protocol.preload.events.service import PreloadEvents
        return PreloadEvents(client=self.client)

    @property
    def security(self):
        from protocol.security.events.service import SecurityEvents
        return SecurityEvents(client=self.client)

    @property
    def service_worker(self):
        from protocol.service_worker.events.service import ServiceWorkerEvents
        return ServiceWorkerEvents(client=self.client)

    @property
    def storage(self):
        from protocol.storage.events.service import StorageEvents
        return StorageEvents(client=self.client)

    @property
    def system_info(self):
        from protocol.system_info.events.service import SystemInfoEvents
        return SystemInfoEvents(client=self.client)

    @property
    def target(self):
        from protocol.target.events.service import TargetEvents
        return TargetEvents(client=self.client)

    @property
    def tethering(self):
        from protocol.tethering.events.service import TetheringEvents
        return TetheringEvents(client=self.client)

    @property
    def tracing(self):
        from protocol.tracing.events.service import TracingEvents
        return TracingEvents(client=self.client)

    @property
    def web_audio(self):
        from protocol.web_audio.events.service import WebAudioEvents
        return WebAudioEvents(client=self.client)

    @property
    def web_authn(self):
        from protocol.web_authn.events.service import WebAuthnEvents
        return WebAuthnEvents(client=self.client)

    @property
    def debugger(self):
        from protocol.debugger.events.service import DebuggerEvents
        return DebuggerEvents(client=self.client)

    @property
    def heap_profiler(self):
        from protocol.heap_profiler.events.service import HeapProfilerEvents
        return HeapProfilerEvents(client=self.client)

    @property
    def profiler(self):
        from protocol.profiler.events.service import ProfilerEvents
        return ProfilerEvents(client=self.client)

    @property
    def runtime(self):
        from protocol.runtime.events.service import RuntimeEvents
        return RuntimeEvents(client=self.client)

