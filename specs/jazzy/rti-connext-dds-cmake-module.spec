# Meta Package
Name:           ros-jazzy-rti-connext-dds-cmake-module
Version:        0.22.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rti_connext_dds_cmake_module and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rti_connext_dds_cmake_module
Requires:       ros2-jazzy-rti_connext_dds_cmake_module-devel

Obsoletes: ros-jazzy-rti-connext-dds-cmake-module < 0.22.1-1

%description
Helper module to provide access to RTI products like Connext DDS
Professional

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.22.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.22.0-1
- Update to latest release
