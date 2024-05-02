# Meta Package
Name:           ros-iron-service-msgs
Version:        1.6.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-service_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-service_msgs
Requires:       ros2-iron-service_msgs-devel

Obsoletes: ros-iron-service-msgs < 1.6.0-1

%description
Messages definitions common among all ROS services

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.6.0-1
- Update to latest release
