# Meta Package
Name:           ros-humble-parameter-traits
Version:        0.3.8
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-parameter_traits and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-parameter_traits
Requires:       ros2-humble-parameter_traits-devel

Obsoletes: ros-humble-parameter-traits < 0.3.8-1

%description
Functions and types for rclcpp::Parameter

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.3.8-1
- update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.3.7-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.3.6-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.3.6-1
- update to latest upstream release
* Fri Aug 11 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.3.6-1
- update to latest upstream
* Sat Apr 15 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.3.3-1
- update to latest release
