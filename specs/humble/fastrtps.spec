# Meta Package
Name:           ros-humble-fastrtps
Version:        2.6.7
Release:        1%{?dist}
License:        Apache 2.0
URL:            https://www.eprosima.com/
Summary:        Meta package for ros2-humble-fastrtps and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-fastrtps
Requires:       ros2-humble-fastrtps-devel

Obsoletes: ros-humble-fastrtps < 2.6.7-1

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
* Mon Feb 12 2024 Tarik Viehmann - humble.2.6.7-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.6-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.6-1
- update to latest upstream release
* Tue Aug 08 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.6-1
- update to latest upstream
* Thu Jun 29 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.5-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.6.4-1
- Initial humble build
