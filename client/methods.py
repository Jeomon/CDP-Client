
"""CDP Methods"""
from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from .service import CDPClient

class CDPMethods:
    def __init__(self, client: "CDPClient"):
        self.client = client

    async def send(self, method: str, params: Optional[Dict[str, Any]] = None,session_id: Optional[str] = None) -> Any:
        return await self.client.send(method, params,session_id)

    @property
    def accessibility(self):
        from protocol.accessibility.methods.service import AccessibilityMethods
        return AccessibilityMethods(methods=self)

    @property
    def animation(self):
        from protocol.animation.methods.service import AnimationMethods
        return AnimationMethods(methods=self)

    @property
    def audits(self):
        from protocol.audits.methods.service import AuditsMethods
        return AuditsMethods(methods=self)

    @property
    def autofill(self):
        from protocol.autofill.methods.service import AutofillMethods
        return AutofillMethods(methods=self)

    @property
    def background_service(self):
        from protocol.background_service.methods.service import BackgroundServiceMethods
        return BackgroundServiceMethods(methods=self)

    @property
    def bluetooth_emulation(self):
        from protocol.bluetooth_emulation.methods.service import BluetoothEmulationMethods
        return BluetoothEmulationMethods(methods=self)

    @property
    def browser(self):
        from protocol.browser.methods.service import BrowserMethods
        return BrowserMethods(methods=self)

    @property
    def css(self):
        from protocol.css.methods.service import CSSMethods
        return CSSMethods(methods=self)

    @property
    def cache_storage(self):
        from protocol.cache_storage.methods.service import CacheStorageMethods
        return CacheStorageMethods(methods=self)

    @property
    def cast(self):
        from protocol.cast.methods.service import CastMethods
        return CastMethods(methods=self)

    @property
    def dom(self):
        from protocol.dom.methods.service import DOMMethods
        return DOMMethods(methods=self)

    @property
    def dom_debugger(self):
        from protocol.dom_debugger.methods.service import DOMDebuggerMethods
        return DOMDebuggerMethods(methods=self)

    @property
    def dom_snapshot(self):
        from protocol.dom_snapshot.methods.service import DOMSnapshotMethods
        return DOMSnapshotMethods(methods=self)

    @property
    def dom_storage(self):
        from protocol.dom_storage.methods.service import DOMStorageMethods
        return DOMStorageMethods(methods=self)

    @property
    def device_access(self):
        from protocol.device_access.methods.service import DeviceAccessMethods
        return DeviceAccessMethods(methods=self)

    @property
    def device_orientation(self):
        from protocol.device_orientation.methods.service import DeviceOrientationMethods
        return DeviceOrientationMethods(methods=self)

    @property
    def emulation(self):
        from protocol.emulation.methods.service import EmulationMethods
        return EmulationMethods(methods=self)

    @property
    def event_breakpoints(self):
        from protocol.event_breakpoints.methods.service import EventBreakpointsMethods
        return EventBreakpointsMethods(methods=self)

    @property
    def extensions(self):
        from protocol.extensions.methods.service import ExtensionsMethods
        return ExtensionsMethods(methods=self)

    @property
    def fed_cm(self):
        from protocol.fed_cm.methods.service import FedCmMethods
        return FedCmMethods(methods=self)

    @property
    def fetch(self):
        from protocol.fetch.methods.service import FetchMethods
        return FetchMethods(methods=self)

    @property
    def file_system(self):
        from protocol.file_system.methods.service import FileSystemMethods
        return FileSystemMethods(methods=self)

    @property
    def headless_experimental(self):
        from protocol.headless_experimental.methods.service import HeadlessExperimentalMethods
        return HeadlessExperimentalMethods(methods=self)

    @property
    def io(self):
        from protocol.io.methods.service import IOMethods
        return IOMethods(methods=self)

    @property
    def indexed_db(self):
        from protocol.indexed_db.methods.service import IndexedDBMethods
        return IndexedDBMethods(methods=self)

    @property
    def input(self):
        from protocol.input.methods.service import InputMethods
        return InputMethods(methods=self)

    @property
    def inspector(self):
        from protocol.inspector.methods.service import InspectorMethods
        return InspectorMethods(methods=self)

    @property
    def layer_tree(self):
        from protocol.layer_tree.methods.service import LayerTreeMethods
        return LayerTreeMethods(methods=self)

    @property
    def log(self):
        from protocol.log.methods.service import LogMethods
        return LogMethods(methods=self)

    @property
    def media(self):
        from protocol.media.methods.service import MediaMethods
        return MediaMethods(methods=self)

    @property
    def memory(self):
        from protocol.memory.methods.service import MemoryMethods
        return MemoryMethods(methods=self)

    @property
    def network(self):
        from protocol.network.methods.service import NetworkMethods
        return NetworkMethods(methods=self)

    @property
    def overlay(self):
        from protocol.overlay.methods.service import OverlayMethods
        return OverlayMethods(methods=self)

    @property
    def pwa(self):
        from protocol.pwa.methods.service import PWAMethods
        return PWAMethods(methods=self)

    @property
    def page(self):
        from protocol.page.methods.service import PageMethods
        return PageMethods(methods=self)

    @property
    def performance(self):
        from protocol.performance.methods.service import PerformanceMethods
        return PerformanceMethods(methods=self)

    @property
    def performance_timeline(self):
        from protocol.performance_timeline.methods.service import PerformanceTimelineMethods
        return PerformanceTimelineMethods(methods=self)

    @property
    def preload(self):
        from protocol.preload.methods.service import PreloadMethods
        return PreloadMethods(methods=self)

    @property
    def security(self):
        from protocol.security.methods.service import SecurityMethods
        return SecurityMethods(methods=self)

    @property
    def service_worker(self):
        from protocol.service_worker.methods.service import ServiceWorkerMethods
        return ServiceWorkerMethods(methods=self)

    @property
    def storage(self):
        from protocol.storage.methods.service import StorageMethods
        return StorageMethods(methods=self)

    @property
    def system_info(self):
        from protocol.system_info.methods.service import SystemInfoMethods
        return SystemInfoMethods(methods=self)

    @property
    def target(self):
        from protocol.target.methods.service import TargetMethods
        return TargetMethods(methods=self)

    @property
    def tethering(self):
        from protocol.tethering.methods.service import TetheringMethods
        return TetheringMethods(methods=self)

    @property
    def tracing(self):
        from protocol.tracing.methods.service import TracingMethods
        return TracingMethods(methods=self)

    @property
    def web_audio(self):
        from protocol.web_audio.methods.service import WebAudioMethods
        return WebAudioMethods(methods=self)

    @property
    def web_authn(self):
        from protocol.web_authn.methods.service import WebAuthnMethods
        return WebAuthnMethods(methods=self)

    @property
    def debugger(self):
        from protocol.debugger.methods.service import DebuggerMethods
        return DebuggerMethods(methods=self)

    @property
    def heap_profiler(self):
        from protocol.heap_profiler.methods.service import HeapProfilerMethods
        return HeapProfilerMethods(methods=self)

    @property
    def profiler(self):
        from protocol.profiler.methods.service import ProfilerMethods
        return ProfilerMethods(methods=self)

    @property
    def runtime(self):
        from protocol.runtime.methods.service import RuntimeMethods
        return RuntimeMethods(methods=self)

