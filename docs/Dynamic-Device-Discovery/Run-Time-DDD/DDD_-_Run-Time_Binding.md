---
title: DDD_-_Run-Time_Binding
---

# DDD - Run-Time Binding

The NetLinx Master can be configured to automatically determine what Dynamic
Application Device a newly discovered Dynamic Physical Device should be bound
to.  The use of this capability requires that a newly discovered physical device
have only one clear choice of Application Device.

Note: An Application Device is a Duet Device (41000-42000) that is used as a
control interface to a physical device.

The Application Device cannot already be bound to another physical device.  In
other words, the Application Device must be “orphaned” awaiting a binding.  The
decision to bind is based on the Application Device’s SDK class.  For example,
if there is only one orphan DUET_DEV_TYPE_VCR in the system and a new VCR is
detected, the two entities will be automatically bound and an associated control
module will be started.  This capability provides a complete hands-free approach
to installation.

If auto-binding is enabled but the master cannot determine which Application
Device to bind, the conflict must be resolved via manual binding through the
master’s Web interface.  For example, if there are two orphan DUET_DEV_TYPE_VCRs
in the system and a new VCR is detected, no binding will occur.  The installer
must (via the master’s Web interface) select which orphan Application Device the
new physical device is to be bound to.  

Automatic binding based on orphan Application Devices is dynamic.  For example,
say there are two orphan application DUET_DEV_TYPE_VCRs and there are two orphan
physical VCRs.  As soon as the installer manually binds one of the Application
Devices with a physical device, the remaining DUET_VCR Application Device will
be automatically bound to the last physical VCR because there is now a clear
one-to-one correspondence.

- Automatic binding can be turned off.  If so, each binding of an orphan
  Application Device to an orphan physical device must be executed manually via
  the master’s Web interface.

- Static bindings, as defined in the NetLinx program via
  [STATIC_PORT_BINDING()](<STATIC_PORT_BINDING().htm>) calls, are not affected
  by automatic or manual binding.

DDD - Binding Persistence

Bindings persist between reboots. The only way a binding can be removed is if :

a\) The binding is manually destroyed via the master’s Web interface

b\) A new/different device is detected on the bound physical port that does not
currently have a control module active.

The first case is self-explanatory but can have some undesired side effects.
 For example, if a running physical device is bound to an Application Device and
the binding is destroyed via the Web interface, the existing binding will be
broken and any running control module will be destroyed.  But because the
physical device is still attached, it will be dynamically detected again and
possibly automatically bound back with the same orphan Application Device that
was just made available via the unbinding process.  Because of this, it is
advised to always disable auto-bind prior to a manual unbind via the Web
interface.

The second case of removing a binding occurs when a different device is detected
on an existing, bound physical port.  The one stipulation is that the existing
binding cannot currently have a running control module.  This could occur either
immediately after a reboot when the existing binding’s physical device has not
been re-acquired or if a running control module terminates itself due to lack of
communication with its physical device.  This case would occur for example, when
a physical device is hot-swapped.  When the old device is removed and its
associated control module terminated due to lack of communication the binding
can be automatically removed when the new device is detected

Bindings with active control modules have precedence and an only be destroyed
manually via the Web interface.

See Also

- [Dynamic Device Discovery (DDD)](<Dynamic_Device_Discovery_(DDD).htm>)

- [DDD - Run-Time Dynamic Device Discovery](DDD_-_Run-Time_Dynamic_Device_Discovery.md)

- [DDD - Static Binding vs Dynamic Binding](DDD_-_Static_Binding_vs_Dynamic_Binding.md)

- [DDD - Duet Module Download and Resolution](DDD_-_Duet_Module_Download_and_Resolution.md)

- [DDD - Device SDK Classes and Constants](DDD_-_Device_SDK_Classes_and_Constants.md)
