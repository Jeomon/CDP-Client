
"""CDP Events"""
from typing import TYPE_CHECKING, Callable, Any

if TYPE_CHECKING:
    from .service import CDPClient

class CDPEvents:
    def __init__(self, client: "CDPClient"):
        self.client = client

    def on(self, event: str, callback: Callable[[Any], None]) -> None:
        self.client.on(event, callback)

    @property
    def accessibility(self):
        from protocol.accessibility.events.service import AccessibilityEvents
        return AccessibilityEvents(events=self)

    @property
    def animation(self):
        from protocol.animation.events.service import AnimationEvents
        return AnimationEvents(events=self)

    @property
    def audits(self):
        from protocol.audits.events.service import AuditsEvents
        return AuditsEvents(events=self)

    @property
    def autofill(self):
        from protocol.autofill.events.service import AutofillEvents
        return AutofillEvents(events=self)

    @property
    def background_service(self):
        from protocol.background_service.events.service import BackgroundServiceEvents
        return BackgroundServiceEvents(events=self)

    @property
    def bluetooth_emulation(self):
        from protocol.bluetooth_emulation.events.service import BluetoothEmulationEvents
        return BluetoothEmulationEvents(events=self)

    @property
    def browser(self):
        from protocol.browser.events.service import BrowserEvents
        return BrowserEvents(events=self)

    @property
    def css(self):
        from protocol.css.events.service import CSSEvents
        return CSSEvents(events=self)

    @property
    def cache_storage(self):
        from protocol.cache_storage.events.service import CacheStorageEvents
        return CacheStorageEvents(events=self)

    @property
    def cast(self):
        from protocol.cast.events.service import CastEvents
        return CastEvents(events=self)

    @property
    def dom(self):
        from protocol.dom.events.service import DOMEvents
        return DOMEvents(events=self)

    @property
    def dom_debugger(self):
        from protocol.dom_debugger.events.service import DOMDebuggerEvents
        return DOMDebuggerEvents(events=self)

    @property
    def dom_snapshot(self):
        from protocol.dom_snapshot.events.service import DOMSnapshotEvents
        return DOMSnapshotEvents(events=self)

    @property
    def dom_storage(self):
        from protocol.dom_storage.events.service import DOMStorageEvents
        return DOMStorageEvents(events=self)

    @property
    def device_access(self):
        from protocol.device_access.events.service import DeviceAccessEvents
        return DeviceAccessEvents(events=self)

    @property
    def device_orientation(self):
        from protocol.device_orientation.events.service import DeviceOrientationEvents
        return DeviceOrientationEvents(events=self)

    @property
    def emulation(self):
        from protocol.emulation.events.service import EmulationEvents
        return EmulationEvents(events=self)

    @property
    def event_breakpoints(self):
        from protocol.event_breakpoints.events.service import EventBreakpointsEvents
        return EventBreakpointsEvents(events=self)

    @property
    def extensions(self):
        from protocol.extensions.events.service import ExtensionsEvents
        return ExtensionsEvents(events=self)

    @property
    def fed_cm(self):
        from protocol.fed_cm.events.service import FedCmEvents
        return FedCmEvents(events=self)

    @property
    def fetch(self):
        from protocol.fetch.events.service import FetchEvents
        return FetchEvents(events=self)

    @property
    def file_system(self):
        from protocol.file_system.events.service import FileSystemEvents
        return FileSystemEvents(events=self)

    @property
    def headless_experimental(self):
        from protocol.headless_experimental.events.service import HeadlessExperimentalEvents
        return HeadlessExperimentalEvents(events=self)

    @property
    def io(self):
        from protocol.io.events.service import IOEvents
        return IOEvents(events=self)

    @property
    def indexed_db(self):
        from protocol.indexed_db.events.service import IndexedDBEvents
        return IndexedDBEvents(events=self)

    @property
    def input(self):
        from protocol.input.events.service import InputEvents
        return InputEvents(events=self)

    @property
    def inspector(self):
        from protocol.inspector.events.service import InspectorEvents
        return InspectorEvents(events=self)

    @property
    def layer_tree(self):
        from protocol.layer_tree.events.service import LayerTreeEvents
        return LayerTreeEvents(events=self)

    @property
    def log(self):
        from protocol.log.events.service import LogEvents
        return LogEvents(events=self)

    @property
    def media(self):
        from protocol.media.events.service import MediaEvents
        return MediaEvents(events=self)

    @property
    def memory(self):
        from protocol.memory.events.service import MemoryEvents
        return MemoryEvents(events=self)

    @property
    def network(self):
        from protocol.network.events.service import NetworkEvents
        return NetworkEvents(events=self)

    @property
    def overlay(self):
        from protocol.overlay.events.service import OverlayEvents
        return OverlayEvents(events=self)

    @property
    def pwa(self):
        from protocol.pwa.events.service import PWAEvents
        return PWAEvents(events=self)

    @property
    def page(self):
        from protocol.page.events.service import PageEvents
        return PageEvents(events=self)

    @property
    def performance(self):
        from protocol.performance.events.service import PerformanceEvents
        return PerformanceEvents(events=self)

    @property
    def performance_timeline(self):
        from protocol.performance_timeline.events.service import PerformanceTimelineEvents
        return PerformanceTimelineEvents(events=self)

    @property
    def preload(self):
        from protocol.preload.events.service import PreloadEvents
        return PreloadEvents(events=self)

    @property
    def security(self):
        from protocol.security.events.service import SecurityEvents
        return SecurityEvents(events=self)

    @property
    def service_worker(self):
        from protocol.service_worker.events.service import ServiceWorkerEvents
        return ServiceWorkerEvents(events=self)

    @property
    def storage(self):
        from protocol.storage.events.service import StorageEvents
        return StorageEvents(events=self)

    @property
    def system_info(self):
        from protocol.system_info.events.service import SystemInfoEvents
        return SystemInfoEvents(events=self)

    @property
    def target(self):
        from protocol.target.events.service import TargetEvents
        return TargetEvents(events=self)

    @property
    def tethering(self):
        from protocol.tethering.events.service import TetheringEvents
        return TetheringEvents(events=self)

    @property
    def tracing(self):
        from protocol.tracing.events.service import TracingEvents
        return TracingEvents(events=self)

    @property
    def web_audio(self):
        from protocol.web_audio.events.service import WebAudioEvents
        return WebAudioEvents(events=self)

    @property
    def web_authn(self):
        from protocol.web_authn.events.service import WebAuthnEvents
        return WebAuthnEvents(events=self)

    @property
    def debugger(self):
        from protocol.debugger.events.service import DebuggerEvents
        return DebuggerEvents(events=self)

    @property
    def heap_profiler(self):
        from protocol.heap_profiler.events.service import HeapProfilerEvents
        return HeapProfilerEvents(events=self)

    @property
    def profiler(self):
        from protocol.profiler.events.service import ProfilerEvents
        return ProfilerEvents(events=self)

    @property
    def runtime(self):
        from protocol.runtime.events.service import RuntimeEvents
        return RuntimeEvents(events=self)

