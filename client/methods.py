
"""CDP Methods"""
from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from .service import CDPClient

class CDPMethods:
    def __init__(self, client: "CDPClient"):
        self.client = client

    @property
    def accessibility(self):
        from protocol.accessibility.methods.service import AccessibilityMethods
        return AccessibilityMethods(client=self.client)

    @property
    def animation(self):
        from protocol.animation.methods.service import AnimationMethods
        return AnimationMethods(client=self.client)

    @property
    def audits(self):
        from protocol.audits.methods.service import AuditsMethods
        return AuditsMethods(client=self.client)

    @property
    def autofill(self):
        from protocol.autofill.methods.service import AutofillMethods
        return AutofillMethods(client=self.client)

    @property
    def background_service(self):
        from protocol.background_service.methods.service import BackgroundServiceMethods
        return BackgroundServiceMethods(client=self.client)

    @property
    def bluetooth_emulation(self):
        from protocol.bluetooth_emulation.methods.service import BluetoothEmulationMethods
        return BluetoothEmulationMethods(client=self.client)

    @property
    def browser(self):
        from protocol.browser.methods.service import BrowserMethods
        return BrowserMethods(client=self.client)

    @property
    def css(self):
        from protocol.css.methods.service import CSSMethods
        return CSSMethods(client=self.client)

    @property
    def cache_storage(self):
        from protocol.cache_storage.methods.service import CacheStorageMethods
        return CacheStorageMethods(client=self.client)

    @property
    def cast(self):
        from protocol.cast.methods.service import CastMethods
        return CastMethods(client=self.client)

    @property
    def dom(self):
        from protocol.dom.methods.service import DOMMethods
        return DOMMethods(client=self.client)

    @property
    def dom_debugger(self):
        from protocol.dom_debugger.methods.service import DOMDebuggerMethods
        return DOMDebuggerMethods(client=self.client)

    @property
    def dom_snapshot(self):
        from protocol.dom_snapshot.methods.service import DOMSnapshotMethods
        return DOMSnapshotMethods(client=self.client)

    @property
    def dom_storage(self):
        from protocol.dom_storage.methods.service import DOMStorageMethods
        return DOMStorageMethods(client=self.client)

    @property
    def device_access(self):
        from protocol.device_access.methods.service import DeviceAccessMethods
        return DeviceAccessMethods(client=self.client)

    @property
    def device_orientation(self):
        from protocol.device_orientation.methods.service import DeviceOrientationMethods
        return DeviceOrientationMethods(client=self.client)

    @property
    def emulation(self):
        from protocol.emulation.methods.service import EmulationMethods
        return EmulationMethods(client=self.client)

    @property
    def event_breakpoints(self):
        from protocol.event_breakpoints.methods.service import EventBreakpointsMethods
        return EventBreakpointsMethods(client=self.client)

    @property
    def extensions(self):
        from protocol.extensions.methods.service import ExtensionsMethods
        return ExtensionsMethods(client=self.client)

    @property
    def fed_cm(self):
        from protocol.fed_cm.methods.service import FedCmMethods
        return FedCmMethods(client=self.client)

    @property
    def fetch(self):
        from protocol.fetch.methods.service import FetchMethods
        return FetchMethods(client=self.client)

    @property
    def file_system(self):
        from protocol.file_system.methods.service import FileSystemMethods
        return FileSystemMethods(client=self.client)

    @property
    def headless_experimental(self):
        from protocol.headless_experimental.methods.service import HeadlessExperimentalMethods
        return HeadlessExperimentalMethods(client=self.client)

    @property
    def io(self):
        from protocol.io.methods.service import IOMethods
        return IOMethods(client=self.client)

    @property
    def indexed_db(self):
        from protocol.indexed_db.methods.service import IndexedDBMethods
        return IndexedDBMethods(client=self.client)

    @property
    def input(self):
        from protocol.input.methods.service import InputMethods
        return InputMethods(client=self.client)

    @property
    def inspector(self):
        from protocol.inspector.methods.service import InspectorMethods
        return InspectorMethods(client=self.client)

    @property
    def layer_tree(self):
        from protocol.layer_tree.methods.service import LayerTreeMethods
        return LayerTreeMethods(client=self.client)

    @property
    def log(self):
        from protocol.log.methods.service import LogMethods
        return LogMethods(client=self.client)

    @property
    def media(self):
        from protocol.media.methods.service import MediaMethods
        return MediaMethods(client=self.client)

    @property
    def memory(self):
        from protocol.memory.methods.service import MemoryMethods
        return MemoryMethods(client=self.client)

    @property
    def network(self):
        from protocol.network.methods.service import NetworkMethods
        return NetworkMethods(client=self.client)

    @property
    def overlay(self):
        from protocol.overlay.methods.service import OverlayMethods
        return OverlayMethods(client=self.client)

    @property
    def pwa(self):
        from protocol.pwa.methods.service import PWAMethods
        return PWAMethods(client=self.client)

    @property
    def page(self):
        from protocol.page.methods.service import PageMethods
        return PageMethods(client=self.client)

    @property
    def performance(self):
        from protocol.performance.methods.service import PerformanceMethods
        return PerformanceMethods(client=self.client)

    @property
    def performance_timeline(self):
        from protocol.performance_timeline.methods.service import PerformanceTimelineMethods
        return PerformanceTimelineMethods(client=self.client)

    @property
    def preload(self):
        from protocol.preload.methods.service import PreloadMethods
        return PreloadMethods(client=self.client)

    @property
    def security(self):
        from protocol.security.methods.service import SecurityMethods
        return SecurityMethods(client=self.client)

    @property
    def service_worker(self):
        from protocol.service_worker.methods.service import ServiceWorkerMethods
        return ServiceWorkerMethods(client=self.client)

    @property
    def storage(self):
        from protocol.storage.methods.service import StorageMethods
        return StorageMethods(client=self.client)

    @property
    def system_info(self):
        from protocol.system_info.methods.service import SystemInfoMethods
        return SystemInfoMethods(client=self.client)

    @property
    def target(self):
        from protocol.target.methods.service import TargetMethods
        return TargetMethods(client=self.client)

    @property
    def tethering(self):
        from protocol.tethering.methods.service import TetheringMethods
        return TetheringMethods(client=self.client)

    @property
    def tracing(self):
        from protocol.tracing.methods.service import TracingMethods
        return TracingMethods(client=self.client)

    @property
    def web_audio(self):
        from protocol.web_audio.methods.service import WebAudioMethods
        return WebAudioMethods(client=self.client)

    @property
    def web_authn(self):
        from protocol.web_authn.methods.service import WebAuthnMethods
        return WebAuthnMethods(client=self.client)

    @property
    def debugger(self):
        from protocol.debugger.methods.service import DebuggerMethods
        return DebuggerMethods(client=self.client)

    @property
    def heap_profiler(self):
        from protocol.heap_profiler.methods.service import HeapProfilerMethods
        return HeapProfilerMethods(client=self.client)

    @property
    def profiler(self):
        from protocol.profiler.methods.service import ProfilerMethods
        return ProfilerMethods(client=self.client)

    @property
    def runtime(self):
        from protocol.runtime.methods.service import RuntimeMethods
        return RuntimeMethods(client=self.client)

