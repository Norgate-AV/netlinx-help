---
title: Dynamic_Device_Discovery_(DDD)
---

# Dynamic Device Discovery (DDD)

In Dynamic Device Discovery (DDD), physical devices are detected in the system at run-time.  

There are two methods of detection; via Dynamic Device Discovery Protocol (DDDP) or user defined via the master’s Web interface.  

## Programming in Concrete

In the current NetLinx/Duet programming environment, the developer must know exactly what devices will be connected to the system, what physical interfaces these devices will be connected to and what control/protocol module is to be used to communicate with the device (be it NetLinx or Duet Module).  As is obvious, this is rather limiting.  If the device for whatever reason needs to be moved to a different physical interface, for example a different serial port, the NetLinx “ glue code” program must be modified, re-compiled, downloaded to the master and the master rebooted.

Note: “Glue code”, is the developer defined NetLinx program that runs on a master and controls a system.

Or let’s say, a physical device breaks and must be swapped out with a comparable, yet different device that talks a different protocol.  The “glue code” would need to be re-compiled with a different control/protocol module in order to talk to the new device.  At an off-site installation, this may require either bringing the “glue code” source code to the site or pulling the source from the master (provided it was stored on the master in the first palace”) not to mention the service call itself.

## Programming in Motion

Dynamic Device Discovery (DDD) was created to take advantage of  Java’s Dynamic Class Loading and the Duet Standard NetLinx API (SNAPI).  Java loads classes as they are needed.  Therefore it is feasible to load a Duet control/protocol module on the fly as each new device is discovered. SNAPI provides a fixed interface for communicating with a certain type of device.  

Take for example a VCR. The majority of control features are common to all VCRs (play, stop, pause, etc.).  SNAPI provides the “glue code” developer the ability to write common code that will control any type of VCR having an associated Duet module.  The underlying Duet module could be swapped in and out based on the actual physical device with no changes needed to the higher level “glue code”.

## Programming Using Dynamic Device Discovery

In the DDD world, all of the existing capabilities of NetLinx and Duet remain.  For those portions of the system that will never change, concrete programming using [DEFINE_MODULE](DEFINE_MODULE.md) continues to provide simple, modular control of a peripheral device.  But with DDD the developer now has the ability to program for the future.

## DDD - NetLinx Programming Interface

Just as the current concrete programming utilizes [DEFINE_MODULE](DEFINE_MODULE.md) to define its peripheral control, DDD introduces additional NetLinx APIs for the definition of dynamic facilities.

See Also

- [DDD - Run-Time Dynamic Device Discovery](DDD_-_Run-Time_Dynamic_Device_Discovery.md)

- [DDD - Run-Time Binding](DDD_-_Run-Time_Binding.md)

- [DDD - Static Binding vs Dynamic Binding](DDD_-_Static_Binding_vs_Dynamic_Binding.md)

- [DDD - Duet Module Download and Resolution](DDD_-_Duet_Module_Download_and_Resolution.md)

- [DDD - Device SDK Classes and Constants](DDD_-_Device_SDK_Classes_and_Constants.md)

