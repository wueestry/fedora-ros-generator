# Meta Package
Name:           ros-jazzy-fastcdr
Version:        2.2.2
Release:        1%{?dist}
License:        Apache 2.0
URL:            https://www.eprosima.com/
Summary:        Meta package for ros2-jazzy-fastcdr and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-fastcdr
Requires:       ros2-jazzy-fastcdr-devel

Obsoletes: ros-jazzy-fastcdr < 2.2.2-1

%description
*eProsima Fast CDR* is a C++ serialization library implementing the
Common Data Representation (CDR) mechanism defined by the Object
Management Group (OMG) consortium. CDR is the serialization mechanism
used in DDS for the DDS Interoperability Wire Protocol (DDSI-RTPS).

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.2.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.2.1-1
- Update to latest release
