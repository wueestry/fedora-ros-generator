# Meta Package
Name:           ros-iron-controller-manager-msgs
Version:        3.24.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-controller_manager_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-controller_manager_msgs
Requires:       ros2-iron-controller_manager_msgs-devel

Obsoletes: ros-iron-controller-manager-msgs < 3.24.0-1

%description
Messages and services for the controller manager.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.24.0-1
- Update to latest release
