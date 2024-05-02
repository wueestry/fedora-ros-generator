# Meta Package
Name:           ros-iron-rti-connext-dds-cmake-module
Version:        0.14.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rti_connext_dds_cmake_module and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rti_connext_dds_cmake_module
Requires:       ros2-iron-rti_connext_dds_cmake_module-devel

Obsoletes: ros-iron-rti-connext-dds-cmake-module < 0.14.1-1

%description
Helper module to provide access to RTI products like Connext DDS
Professional

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.14.1-1
- Update to latest release
