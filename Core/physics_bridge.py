import ctypes
import numpy as np
import logging

logger = logging.getLogger(__name__)

class PhysicsBridge:
    def __init__(self, lib_path="Physics/build/libDeltaPhysics.so"):
        try:
            self.lib = ctypes.CDLL(lib_path)
            logger.info("PhysicsBridge: C++ library loaded")
        except OSError as e:
            logger.error(f"Failed to load C++ library: {e}")
            self.lib = None

    def is_available(self) -> bool:
        return self.lib is not None