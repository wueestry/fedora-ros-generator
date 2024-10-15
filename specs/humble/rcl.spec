# Meta Package
Name:           ros-humble-rcl
Version:        5.3.9
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rcl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rcl
Requires:       ros2-humble-rcl-devel

Obsoletes: ros-humble-rcl < 5.3.9-1

%description
The ROS client library common implementation. This package contains an
API which builds on the ROS middleware API and is optionally built
upon by the other ROS client libraries.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.3.9-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.3.8-1
- Update to latest release
* Mon Feb 12 2024 Tarik Viehmann - humble.5.3.7-1
- update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.3.6-1
- update to latest upstream
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.3.5-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.3.4-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.3.4-1
- update to latest upstream release
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.3.4-1
- update to latest release
* Mon Jun 19 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.3.3-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.3.2-1
- Initial humble build
