# Meta Package
Name:           ros-jazzy-service-msgs
Version:        2.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-service_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-service_msgs
Requires:       ros2-jazzy-service_msgs-devel

Obsoletes: ros-jazzy-service-msgs < 2.0.2-1

%description
Messages definitions common among all ROS services

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.2-1
- Update to latest release
