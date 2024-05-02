# Meta Package
Name:           ros-humble-rti-connext-dds-cmake-module
Version:        0.11.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rti_connext_dds_cmake_module and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rti_connext_dds_cmake_module
Requires:       ros2-humble-rti_connext_dds_cmake_module-devel

Obsoletes: ros-humble-rti-connext-dds-cmake-module < 0.11.2-1

%description
Helper module to provide access to RTI products like Connext DDS
Professional

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.11.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.11.2-1
- update to latest upstream release
* Tue Aug 08 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.11.2-1
- update to latest upstream
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.11.1-1
- Initial humble build
