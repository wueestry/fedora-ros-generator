# Meta Package
Name:           ros-humble-rmw
Version:        6.1.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rmw and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rmw
Requires:       ros2-humble-rmw-devel

Obsoletes: ros-humble-rmw < 6.1.1-1

%description
Contains the ROS middleware API.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.6.1.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.6.1.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.6.1.1-1
- Initial humble build
