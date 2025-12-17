---
title: DDD_-_Duet_Module_Download_and_Resolution
---

# DDD - Duet Module Download and Resolution

In order to complete a bind activity, the master’s firmware must load and start
the appropriate Duet module to control the new device.  In the concrete
programming world, these modules are bundled and downloaded with the NetLinx
application.  But with Dynamic Device Discovery, the proper Duet modules are not
known at program time and thus cannot be part of the programming download.  

Currently, Dynamic Device Discovery requires that the necessary modules must be
resident on the master.  The capability has been added to the master’s Web
control to download Duet module .jar files from any networked PC.

Due to Java’s dynamic class loading, it is not safe to swap out a .jar file at
run-time.  This could cause class definition conflicts generating exceptions and
termination of the Duet module.  To avoid this, the downloaded .jar files are
placed in a holding directory on the master.  As each module is started by the
master, it is first copied into a run-time directory to prevent overwrites by
subsequent downloads.  

Each active binding requires the loading and instantiation of an associated Duet
Module.  To determine the correct module to load, the master’s firmware uses a
set of property values to determine the best possible match.  When a new device
is detected in the system, it provides this set of property values.  The master
firmware then searches through its list of modules looking for the one that best
matches the new devices values.  Once a Duet module has been associated with a
binding, that association is persistent throughout the life of that binding as
long as the run-time instance of the module exists.

This persistent association can present problems whenever a new version of the
module is downloaded.  Because newly downloaded modules are placed in a holding
directory, the new module will not be picked up until the old version in the
run-time directory is deleted.  But remember, the run-time version cannot be
deleted while the module is active.

To get around this, a control has been added to the masters Web interface to
purge all run-time modules upon the next system reboot.  With this selected, the
next time the master is restarted, prior to any Duet modules being activated,
all run-time version of the Duet modules will be deleted.  This will force the
master to re-resolve each binding with its appropriate Duet module from the
holding directory.  This mechanism is used both to updated existing modules as
well as to purge old modules from the system for devices that no longer exist.

In future releases of Duet, it is anticipated that module loading may be dynamic
rather than requiring the module be pre-resident on the master.  The module may
be retrieved from AMX’s web site or from a device specified URL.  Or perhaps
even from the device itself provided the device has an HTTP or FTP server.  In
all of these cases, the retrieved module will be placed in the run-time
directory and persist between reboots, thereby eliminating the need to
re-retrieve the module.

See Also

- [Dynamic Device Discovery (DDD)](<Dynamic_Device_Discovery_(DDD).htm>)

- [DDD - Run-Time Dynamic Device Discovery](DDD_-_Run-Time_Dynamic_Device_Discovery.md)

- [DDD - Static Binding vs Dynamic Binding](DDD_-_Static_Binding_vs_Dynamic_Binding.md)

- [DDD - Device SDK Classes and Constants](DDD_-_Device_SDK_Classes_and_Constants.md)
