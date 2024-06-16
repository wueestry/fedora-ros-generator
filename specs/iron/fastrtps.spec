# Meta Package
Name:           ros-iron-fastrtps
Version:        2.10.4
Release:        1%{?dist}
License:        Apache 2.0
URL:            https://www.eprosima.com/
Summary:        Meta package for ros2-iron-fastrtps and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-fastrtps
Requires:       ros2-iron-fastrtps-devel

Obsoletes: ros-iron-fastrtps < 2.10.4-1

%description
*eprosima Fast DDS* (formerly Fast RTPS) is a C++ implementation of
the DDS (Data Distribution Service) standard of the OMG (Object
Management Group). eProsima Fast DDS implements the RTPS (Real Time
Publish Subscribe) protocol, which provides publisher-subscriber
communications over unreliable transports such as UDP, as defined and
maintained by the Object Management Group (OMG) consortium. RTPS is
also the wire interoperability protocol defined for the Data
Distribution Service (DDS) standard. *eProsima Fast DDS* expose an API
to access directly the RTPS protocol, giving the user full access to
the protocol internals.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.10.4-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.10.3-1
- Update to latest release
