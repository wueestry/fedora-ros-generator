# Meta Package
Name:           ros-humble-ros2-control
Version:        2.42.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ros2_control and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ros2_control
Requires:       ros2-humble-ros2_control-devel

Obsoletes: ros-humble-ros2-control < 2.42.0-1

%description
Metapackage for ROS2 control related packages

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.42.0-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.41.0-1
- Update to latest release
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.40.0-1
- Update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.39.1-1
- Update to latest release
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.35.1-1
- update to latest upstream
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.33.0-1
- update to latest release
* Mon Apr 17 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.25.1-1
- update to latest release
