# Meta Package
Name:           ros-jazzy-domain-coordinator
Version:        0.12.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-domain_coordinator and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-domain_coordinator
Requires:       ros2-jazzy-domain_coordinator-devel

Obsoletes: ros-jazzy-domain-coordinator < 0.12.0-1

%description
A tool to coordinate unique ROS_DOMAIN_IDs across multiple processes

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.12.0-1
- Update to latest release
