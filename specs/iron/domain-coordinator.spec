# Meta Package
Name:           ros-iron-domain-coordinator
Version:        0.11.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-domain_coordinator and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-domain_coordinator
Requires:       ros2-iron-domain_coordinator-devel

Obsoletes: ros-iron-domain-coordinator < 0.11.2-1

%description
A tool to coordinate unique ROS_DOMAIN_IDs across multiple processes

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.11.2-1
- Update to latest release
