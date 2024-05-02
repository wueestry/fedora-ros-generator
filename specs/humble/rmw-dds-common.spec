# Meta Package
Name:           ros-humble-rmw-dds-common
Version:        1.6.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rmw_dds_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rmw_dds_common
Requires:       ros2-humble-rmw_dds_common-devel

Obsoletes: ros-humble-rmw-dds-common < 1.6.0-1

%description
Define a common interface between DDS implementations of ROS
middleware.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.6.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.6.0-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.6.0-1
- Initial humble build
