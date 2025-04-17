# Meta Package
Name:           ros-jazzy-fastrtps
Version:        2.14.4
Release:        1%{?dist}
License:        Apache 2.0
URL:            https://www.eprosima.com/
Summary:        Meta package for ros2-jazzy-fastrtps and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-fastrtps
Requires:       ros2-jazzy-fastrtps-devel

Obsoletes: ros-jazzy-fastrtps < 2.14.4-1

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
* Wed Dec 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.14.4-1
- Update to latest release
* Tue Oct 22 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.14.3-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.14.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.14.0-1
- Update to latest release
